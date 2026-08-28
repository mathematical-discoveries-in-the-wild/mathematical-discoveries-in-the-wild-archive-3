#!/usr/bin/env python3
"""Regression checks for the real-hexablock height formula.

The exact proof is in main.tex.  This script independently compares the
source's nested-radical formula with the closed form and probes Jensen
concavity on random points of the real tetrablock tetrahedron.
"""

from __future__ import annotations

import argparse
import numpy as np


VERTICES = np.array(
    [
        [1.0, 1.0, 1.0],
        [1.0, -1.0, -1.0],
        [-1.0, 1.0, -1.0],
        [-1.0, -1.0, 1.0],
    ]
)


def sample_tetrahedron(
    rng: np.random.Generator, count: int
) -> np.ndarray:
    weights = rng.exponential(size=(count, 4))
    weights /= weights.sum(axis=1, keepdims=True)
    return weights @ VERTICES


def source_height(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate source Proposition 6.3 and return K,z1,z2."""
    x1, x2, p = np.moveaxis(np.asarray(x, dtype=float), -1, 0)
    beta1 = (x1 - p * x2) / (1.0 - p * p)
    beta2 = (x2 - p * x1) / (1.0 - p * p)

    a1 = 1.0 + beta1 * beta1 - beta2 * beta2
    a2 = 1.0 + beta2 * beta2 - beta1 * beta1
    common = np.maximum(
        (1.0 - (beta1 + beta2) ** 2)
        * (1.0 - (beta1 - beta2) ** 2),
        0.0,
    )
    root = np.sqrt(common)
    z1 = 2.0 * beta1 / (a1 + root)
    z2 = 2.0 * beta2 / (a2 + root)
    numerator = 1.0 - x1 * z1 - x2 * z2 + p * z1 * z2
    denominator = np.sqrt((1.0 - z1 * z1) * (1.0 - z2 * z2))
    return numerator / denominator, z1, z2


def closed_height(x: np.ndarray) -> np.ndarray:
    x1, x2, p = np.moveaxis(np.asarray(x, dtype=float), -1, 0)
    first = np.maximum((1.0 + p) ** 2 - (x1 + x2) ** 2, 0.0)
    second = np.maximum((1.0 - p) ** 2 - (x1 - x2) ** 2, 0.0)
    return 0.5 * (np.sqrt(first) + np.sqrt(second))


def half_angle_points(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x1, x2, p = np.moveaxis(np.asarray(x, dtype=float), -1, 0)
    beta1 = (x1 - p * x2) / (1.0 - p * p)
    beta2 = (x2 - p * x1) / (1.0 - p * p)
    u = beta1 + beta2
    v = beta1 - beta2
    u = np.clip(u, -1.0 + 1e-15, 1.0 - 1e-15)
    v = np.clip(v, -1.0 + 1e-15, 1.0 - 1e-15)
    U = np.arctanh(u)
    V = np.arctanh(v)
    return np.tanh(0.5 * (U + V)), np.tanh(0.5 * (U - V))


def main(cases: int, seed: int) -> None:
    rng = np.random.default_rng(seed)

    x = sample_tetrahedron(rng, cases)
    source, z1, z2 = source_height(x)
    closed = closed_height(x)
    hz1, hz2 = half_angle_points(x)
    identity_error = float(np.max(np.abs(source - closed)))
    z_error = float(max(np.max(np.abs(z1 - hz1)), np.max(np.abs(z2 - hz2))))

    y = sample_tetrahedron(rng, cases)
    t = rng.uniform(0.0, 1.0, size=cases)
    midpoint = t[:, None] * x + (1.0 - t)[:, None] * y
    gap = (
        closed_height(midpoint)
        - t * closed_height(x)
        - (1.0 - t) * closed_height(y)
    )
    min_gap = float(np.min(gap))

    print("cases", cases)
    print("seed", seed)
    print("max_source_closed_error", repr(identity_error))
    print("max_half_angle_error", repr(z_error))
    print("minimum_jensen_gap", repr(min_gap))

    if identity_error > 5e-11:
        raise SystemExit("source/closed-form identity check failed")
    if z_error > 5e-11:
        raise SystemExit("half-angle check failed")
    if min_gap < -5e-12:
        raise SystemExit("Jensen check failed")
    print("PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=250_615_149)
    args = parser.parse_args()
    main(args.cases, args.seed)
