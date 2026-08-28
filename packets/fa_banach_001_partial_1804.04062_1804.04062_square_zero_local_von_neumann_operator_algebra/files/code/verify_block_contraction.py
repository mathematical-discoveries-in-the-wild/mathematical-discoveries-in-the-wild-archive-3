"""Numerical check for the upper-triangular block norm used in the proof.

This is a regression check, not part of the proof.  For random complex matrices
S and scalars lambda it compares the computed norm of

    [[lambda I, S], [0, lambda I]]

with the closed formula depending only on |lambda| and ||S||.
"""

from __future__ import annotations

import numpy as np


def operator_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False)[0])


def predicted_norm(lam: complex, s_norm: float) -> float:
    return 0.5 * (s_norm + np.sqrt(s_norm * s_norm + 4.0 * abs(lam) ** 2))


def main() -> None:
    rng = np.random.default_rng(180404062)
    worst_error = 0.0
    trials = 2000
    for _ in range(trials):
        n = int(rng.integers(1, 8))
        raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        raw_norm = operator_norm(raw)
        scale = float(rng.uniform(0.0, 2.5))
        s = raw * (scale / raw_norm)
        lam = complex(*rng.uniform(-1.25, 1.25, size=2))

        identity = np.eye(n, dtype=complex)
        zero = np.zeros((n, n), dtype=complex)
        block = np.block([[lam * identity, s], [zero, lam * identity]])

        actual = operator_norm(block)
        predicted = predicted_norm(lam, operator_norm(s))
        error = abs(actual - predicted)
        worst_error = max(worst_error, error)
        if error > 2.0e-11:
            raise AssertionError((n, lam, actual, predicted, error))

    print(f"verified {trials} random cases; worst absolute error {worst_error:.3e}")


if __name__ == "__main__":
    main()
