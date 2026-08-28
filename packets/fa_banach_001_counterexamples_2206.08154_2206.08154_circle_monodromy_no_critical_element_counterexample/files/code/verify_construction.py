#!/usr/bin/env python3
"""Numerical regression checks for the C(S^1) cubic counterexample.

The winding-number proof in the packet is exact. This script only guards
against sign, coefficient, and normalization mistakes in the construction.
"""

from __future__ import annotations

import numpy as np


def winding_number(values: np.ndarray) -> int:
    ratios = np.roll(values, -1) / values
    total_angle = np.angle(ratios).sum()
    return int(np.rint(total_angle / (2.0 * np.pi)))


def main() -> None:
    sample_count = 16_384
    epsilon = 0.25
    rho = np.exp(1j * np.pi / 3.0)
    theta = 2.0 * np.pi * np.arange(sample_count) / sample_count
    u = np.exp(1j * theta)
    c = rho + epsilon * u

    q_direct = c * c - c + 1.0
    q_factored = epsilon * u * (1j * np.sqrt(3.0) + epsilon * u)
    factorization_error = float(np.max(np.abs(q_direct - q_factored)))
    assert factorization_error < 2e-15

    min_abs_c = float(np.min(np.abs(c)))
    min_abs_q = float(np.min(np.abs(q_direct)))
    assert min_abs_c >= 0.75 - 1e-12
    assert min_abs_q >= epsilon * (np.sqrt(3.0) - epsilon) - 1e-12

    winding_q = winding_number(q_direct)
    assert winding_q == 1

    # Each scalar fiber does have two critical points; the obstruction is that
    # neither choice can be made continuously around the circle.
    sqrt_q = np.sqrt(q_direct)
    roots = ((1.0 + c) + sqrt_q) / 3.0, ((1.0 + c) - sqrt_q) / 3.0
    root_residual = max(
        float(np.max(np.abs(3.0 * w * w - 2.0 * (1.0 + c) * w + c)))
        for w in roots
    )
    assert root_residual < 2e-15

    print(f"samples={sample_count}")
    print(f"max_factorization_error={factorization_error:.3e}")
    print(f"min_abs_c={min_abs_c:.12f}")
    print(f"min_abs_q={min_abs_q:.12f}")
    print(f"winding_q={winding_q}")
    print(f"max_fiberwise_root_residual={root_residual:.3e}")
    print("status=PASS")


if __name__ == "__main__":
    main()
