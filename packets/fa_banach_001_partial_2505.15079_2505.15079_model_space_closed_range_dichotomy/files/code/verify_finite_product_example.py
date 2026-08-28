#!/usr/bin/env python3
"""Finite Blaschke-product sanity checks for the packet theorem."""

from __future__ import annotations

import numpy as np


def blaschke(a: complex, z: complex) -> complex:
    return (z - a) / (1.0 - np.conjugate(a) * z)


def mw_value(zeros: np.ndarray, k: int, z: complex) -> complex:
    """The k-th Malmquist-Walsh basis function at z."""
    a = zeros[k]
    value = np.sqrt(1.0 - abs(a) ** 2) / (1.0 - np.conjugate(a) * z)
    for previous in zeros[:k]:
        value *= blaschke(previous, z)
    return value


def one_trial(rng: np.random.Generator) -> tuple[float, float, int]:
    n = int(rng.integers(2, 9))
    m = int(rng.integers(1, 6))
    radii = rng.uniform(0.05, 0.82, n + m)
    angles = rng.uniform(0.0, 2.0 * np.pi, n + m)
    zeros = radii * np.exp(1j * angles)
    z = zeros[:n]

    evaluation = np.empty((n, n + m), dtype=complex)
    for i, point in enumerate(z):
        for k in range(n + m):
            evaluation[i, k] = mw_value(zeros, k, point)

    weights = 1.0 - np.abs(z) ** 2
    restriction = np.sqrt(weights)[:, None] * evaluation
    rank = int(np.linalg.matrix_rank(restriction, tol=1e-9))
    if rank != n:
        raise AssertionError(("row rank", rank, n))

    gram_from_restriction = restriction @ restriction.conjugate().T
    gram_from_kernels = np.empty((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            gram_from_kernels[i, j] = (
                np.sqrt(weights[i] * weights[j])
                / (1.0 - np.conjugate(z[j]) * z[i])
            )

    residual = float(
        np.linalg.norm(gram_from_restriction - gram_from_kernels, ord=np.inf)
    )
    smallest = float(np.linalg.svd(restriction, compute_uv=False)[-1])
    nullity = n + m - rank
    if nullity != m:
        raise AssertionError(("nullity", nullity, m))
    return residual, smallest, nullity


def main() -> None:
    rng = np.random.default_rng(250515079)
    max_residual = 0.0
    min_singular = float("inf")
    max_nullity = 0
    trials = 500
    for _ in range(trials):
        residual, smallest, nullity = one_trial(rng)
        max_residual = max(max_residual, residual)
        min_singular = min(min_singular, smallest)
        max_nullity = max(max_nullity, nullity)
    if max_residual > 2e-10:
        raise AssertionError(("Gram residual", max_residual))
    print("trials", trials)
    print("max_gram_residual", f"{max_residual:.3e}")
    print("min_row_singular_value", f"{min_singular:.3e}")
    print("max_verified_nullity", max_nullity)
    print("PASS")


if __name__ == "__main__":
    main()
