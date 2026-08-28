#!/usr/bin/env python3
"""Finite-chaos regression checks for the harmonic Langevin proof packet.

The proof itself is analytic.  This script builds the generator in the
orthonormal product-Hermite basis, checks its spectrum against the symmetric
tensor formula, checks the exact tensor-power semigroup norms, and verifies
the rank-one Mori compression and memory-kernel identities.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.linalg import expm, svdvals


def first_chaos_generator(gamma: float) -> np.ndarray:
    """Matrix of K on (q,p), with columns representing images of basis vectors."""
    return np.array([[0.0, -1.0], [1.0, -gamma]])


def chaos_generator(total_degree: int, gamma: float) -> np.ndarray:
    """Matrix of K on normalized He_m(q) He_n(p), m+n=total_degree."""
    # Order by increasing p-degree, so degree one is exactly (q,p).
    basis = [(total_degree - n, n) for n in range(total_degree + 1)]
    index = {pair: i for i, pair in enumerate(basis)}
    matrix = np.zeros((total_degree + 1, total_degree + 1))

    for column, (m, n) in enumerate(basis):
        matrix[column, column] -= gamma * n
        if m:
            target = (m - 1, n + 1)
            matrix[index[target], column] += math.sqrt(m * (n + 1))
        if n:
            target = (m + 1, n - 1)
            matrix[index[target], column] -= math.sqrt(n * (m + 1))
    return matrix


def check_gamma(gamma: float, max_degree: int, tolerance: float) -> None:
    discriminant = math.sqrt(gamma * gamma - 4.0)
    slow_gap = (gamma - discriminant) / 2.0
    fast_gap = (gamma + discriminant) / 2.0
    first = first_chaos_generator(gamma)

    assert np.allclose(chaos_generator(1, gamma), first, atol=tolerance)

    times = (0.07, 0.4, 1.3)
    for degree in range(1, max_degree + 1):
        generator = chaos_generator(degree, gamma)
        actual = np.sort(np.real_if_close(np.linalg.eigvals(generator)).real)
        expected = np.sort(
            np.array(
                [-(k * slow_gap + (degree - k) * fast_gap) for k in range(degree + 1)]
            )
        )
        error = np.max(np.abs(actual - expected))
        assert error < tolerance, (gamma, degree, error, actual, expected)

        for time in times:
            first_norm = svdvals(expm(time * first))[0]
            chaos_norm = svdvals(expm(time * generator))[0]
            tensor_error = abs(chaos_norm - first_norm**degree)
            assert tensor_error < 20.0 * tolerance, (
                gamma,
                degree,
                time,
                tensor_error,
            )

    q = np.array([1.0, 0.0])
    p = np.array([0.0, 1.0])
    projection_q = np.outer(q, q)
    complement = np.eye(2) - projection_q
    compressed = complement @ first @ complement
    assert np.allclose(complement @ first @ q, p, atol=tolerance)
    assert np.allclose(compressed @ p, -gamma * p, atol=tolerance)

    for time in times:
        force = expm(time * compressed) @ p
        expected_force = math.exp(-gamma * time) * p
        assert np.allclose(force, expected_force, atol=tolerance)
        memory = q @ first @ force
        assert abs(memory + math.exp(-gamma * time)) < tolerance

    retained_edges = [-gamma]
    for degree in range(2, max_degree + 1):
        retained_edges.extend(np.linalg.eigvals(chaos_generator(degree, gamma)).real)
    numerical_edge = max(retained_edges)
    assert abs(numerical_edge + 2.0 * slow_gap) < tolerance

    print(
        f"gamma={gamma:g}: original gap={slow_gap:.12g}, "
        f"orthogonal gap={2.0 * slow_gap:.12g}, "
        f"force/memory rate={gamma:g}; checked degrees 1..{max_degree}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=8)
    parser.add_argument(
        "--gammas",
        type=float,
        nargs="+",
        default=(2.1, 2.5, 3.0, 5.0, 10.0),
    )
    parser.add_argument("--tolerance", type=float, default=1e-6)
    args = parser.parse_args()

    if args.max_degree < 2:
        raise ValueError("--max-degree must be at least 2")
    for gamma in args.gammas:
        if gamma <= 2.0:
            raise ValueError("all friction parameters must satisfy gamma > 2")
        check_gamma(gamma, args.max_degree, args.tolerance)
    print("all finite-chaos regression checks passed")


if __name__ == "__main__":
    main()
