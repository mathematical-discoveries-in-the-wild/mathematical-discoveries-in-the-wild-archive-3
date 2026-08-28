#!/usr/bin/env python3
"""Regression checks for mixed-norm order and monotonicity reductions."""

from __future__ import annotations

import itertools
import numpy as np


def mixed_norm(array: np.ndarray, exponents: tuple[float, ...]) -> float:
    """Nested norm with axis 0 outermost and the last axis innermost."""
    value = np.asarray(array, dtype=float)
    for exponent in reversed(exponents):
        value = np.sum(value**exponent, axis=-1) ** (1.0 / exponent)
    return float(value)


def sorted_vertex_bound(
    array: np.ndarray, exponents: tuple[int, ...]
) -> tuple[np.ndarray, tuple[int, ...]]:
    """Move exponent-1 axes outside exponent-2 axes."""
    permutation = tuple(
        i for value in (1, 2) for i, exponent in enumerate(exponents)
        if exponent == value
    )
    sorted_array = np.transpose(array, permutation)
    sorted_exponents = tuple(exponents[i] for i in permutation)
    return sorted_array, sorted_exponents


def sylvester(order: int) -> np.ndarray:
    """Sylvester Hadamard matrix of power-of-two order."""
    matrix = np.ones((1, 1), dtype=float)
    while matrix.shape[0] < order:
        matrix = np.block([[matrix, matrix], [matrix, -matrix]])
    return matrix


def run() -> None:
    rng = np.random.default_rng(190404549)
    tests = 0
    worst_swap = 0.0
    worst_sort = 0.0
    worst_monotone = 0.0
    hadamard_checks = 0

    for dimension in range(2, 6):
        shape = (3,) * dimension
        for _ in range(2000):
            array = rng.lognormal(size=shape)

            # Adjacent outer-2/inner-1 Minkowski swap.
            location = int(rng.integers(0, dimension - 1))
            exponents = [2] * dimension
            exponents[location + 1] = 1
            original = mixed_norm(array, tuple(exponents))
            permutation = list(range(dimension))
            permutation[location], permutation[location + 1] = (
                permutation[location + 1], permutation[location]
            )
            swapped_array = np.transpose(array, permutation)
            swapped_exponents = list(exponents)
            swapped_exponents[location], swapped_exponents[location + 1] = (
                swapped_exponents[location + 1],
                swapped_exponents[location],
            )
            swapped = mixed_norm(swapped_array, tuple(swapped_exponents))
            worst_swap = max(worst_swap, original - swapped)
            if original > swapped * (1.0 + 2e-12):
                raise SystemExit("adjacent Minkowski direction failed")

            # Full sorting for every 1/2 pattern.
            pattern = tuple(int(x) for x in rng.integers(1, 3, dimension))
            sorted_array, sorted_pattern = sorted_vertex_bound(array, pattern)
            before = mixed_norm(array, pattern)
            after = mixed_norm(sorted_array, sorted_pattern)
            worst_sort = max(worst_sort, before - after)
            if before > after * (1.0 + 3e-12):
                raise SystemExit("vertex sorting direction failed")

            # Increasing exponents must decrease the mixed norm.
            lower = tuple(float(x) for x in rng.uniform(1.0, 2.0, dimension))
            upper = tuple(
                float(x) for x in (
                    np.asarray(lower) + rng.uniform(0.0, 3.0, dimension)
                )
            )
            low_norm = mixed_norm(array, lower)
            high_norm = mixed_norm(array, upper)
            worst_monotone = max(worst_monotone, high_norm - low_norm)
            if high_norm > low_norm * (1.0 + 3e-12):
                raise SystemExit("coordinatewise monotonicity failed")
            tests += 1

    for order in (2, 4, 8, 16, 32, 64):
        matrix = sylvester(order)
        residual = np.max(np.abs(matrix @ matrix.T - order * np.eye(order)))
        if residual != 0.0:
            raise SystemExit("Sylvester orthogonality failed")
        for exponent in (1.0, 1.5, 2.0, 3.0, 10.0):
            bound = order ** max(1.0 / exponent - 0.5, 0.0)
            for _ in range(200):
                vector = rng.uniform(-1.0, 1.0, order)
                weak_value = np.linalg.norm(matrix @ vector, ord=exponent) / order
                if weak_value > bound * (1.0 + 3e-12):
                    raise SystemExit("Hadamard weak-norm bound failed")
                hadamard_checks += 1

    print("arrays_checked", tests)
    print("worst_swap_residual", repr(worst_swap))
    print("worst_sort_residual", repr(worst_sort))
    print("worst_monotonicity_residual", repr(worst_monotone))
    print("patterns", len(tuple(itertools.product((1, 2), repeat=5))))
    print("hadamard_checks", hadamard_checks)
    print("PASS")


if __name__ == "__main__":
    run()
