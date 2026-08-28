#!/usr/bin/env python3
"""Finite-block regression checks for the unbounded rotation construction.

The packet contains an exact proof. This script only guards against sign,
matrix-exponential, and asymptotic-normalization errors.
"""

from __future__ import annotations

import numpy as np


Q2 = np.array([[0.0, 0.0], [0.0, 1.0]])


def block_matrix(n: int, k: float) -> np.ndarray:
    return np.array([[-k, -float(n)], [float(n), 0.0]])


def block_exponential(n: int, k: float, t: float) -> np.ndarray:
    matrix = block_matrix(n, k)
    half_k = 0.5 * k
    if n > half_k:
        omega = np.sqrt(n * n - half_k * half_k)
        return np.exp(-half_k * t) * (
            np.cos(omega * t) * np.eye(2)
            + np.sin(omega * t) / omega * (matrix + half_k * np.eye(2))
        )

    delta = np.sqrt(half_k * half_k - n * n)
    if delta == 0.0:
        return np.exp(-half_k * t) * (
            np.eye(2) + t * (matrix + half_k * np.eye(2))
        )
    slow = np.exp((-half_k + delta) * t)
    fast = np.exp((-half_k - delta) * t)
    return 0.5 * (slow + fast) * np.eye(2) + (
        0.5 * (slow - fast) / delta * (matrix + half_k * np.eye(2))
    )


def operator_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False)[0])


def main() -> None:
    worst_contraction_excess = 0.0
    worst_fixed_mode_error = 0.0
    smallest_high_mode_margin = float("inf")

    for t in (0.2, 0.7, 1.5):
        for n in (1, 3, 10):
            errors = []
            for k in (100.0, 1_000.0, 10_000.0):
                exponential = block_exponential(n, k, t)
                errors.append(operator_norm(exponential - Q2))
                worst_contraction_excess = max(
                    worst_contraction_excess, operator_norm(exponential) - 1.0
                )
            assert errors[2] < errors[1] < errors[0]
            worst_fixed_mode_error = max(worst_fixed_mode_error, errors[-1])

        e2 = np.array([0.0, 1.0])
        for k in (5.0, 10.0, 20.0, 40.0):
            n = max(100_000, int(10_000 * k))
            exponential = block_exponential(n, k, t)
            damped_norm = float(np.linalg.norm(exponential @ e2))
            expected = float(np.exp(-0.5 * k * t))
            assert abs(damped_norm - expected) < 2e-5

            actual_error = float(np.linalg.norm(exponential @ e2 - e2))
            lower_bound = 1.0 - expected
            margin = actual_error - lower_bound
            assert margin > -2e-5
            smallest_high_mode_margin = min(smallest_high_mode_margin, margin)
            worst_contraction_excess = max(
                worst_contraction_excess, operator_norm(exponential) - 1.0
            )

    assert worst_contraction_excess < 2e-12
    assert worst_fixed_mode_error < 0.02
    print("fixed_modes=(1,3,10)")
    print("k_values=(5,10,20,40,100,1000,10000)")
    print("t_values=(0.2,0.7,1.5)")
    print(f"worst_fixed_mode_error_at_k_10000={worst_fixed_mode_error:.3e}")
    print(f"worst_contraction_excess={worst_contraction_excess:.3e}")
    print(f"smallest_high_mode_lower_bound_margin={smallest_high_mode_margin:.3e}")
    print("status=PASS")


if __name__ == "__main__":
    main()
