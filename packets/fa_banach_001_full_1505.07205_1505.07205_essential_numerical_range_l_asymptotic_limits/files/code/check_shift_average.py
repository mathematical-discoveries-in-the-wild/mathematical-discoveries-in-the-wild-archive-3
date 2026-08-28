"""Sanity checks for the balanced diagonal construction (not a proof)."""

from __future__ import annotations

import numpy as np


def mechanical_word(q: float, length: int) -> np.ndarray:
    n = np.arange(length, dtype=float)
    return np.floor((n + 1.0) * q) - np.floor(n * q)


def max_interval_discrepancy(word: np.ndarray, q: float, width: int) -> float:
    prefix = np.concatenate(([0.0], np.cumsum(word)))
    counts = prefix[width:] - prefix[:-width]
    return float(np.max(np.abs(counts - q * width)))


def max_moving_average_error(values: np.ndarray, target: float, width: int) -> float:
    kernel = np.ones(width, dtype=float) / width
    averages = np.convolve(values, kernel, mode="valid")
    return float(np.max(np.abs(averages - target)))


def main() -> None:
    low, high, target = 0.5, 2.0, 1.0
    q = (target - low) / (high - low)
    length = 200_000
    word = mechanical_word(q, length)

    # Add decaying perturbations to model diagonal subsequences converging to
    # the two essential spectral points.
    indices = np.arange(length, dtype=float)
    perturbation = 0.08 * np.sin(indices) / np.sqrt(indices + 1.0)
    values = np.where(word > 0.5, high, low) + perturbation

    widths = (10, 100, 1_000, 10_000)
    errors = []
    for width in widths:
        discrepancy = max_interval_discrepancy(word, q, width)
        error = max_moving_average_error(values, target, width)
        errors.append(error)
        print(
            f"width={width:5d} discrepancy={discrepancy:.6f} "
            f"max_average_error={error:.8f}"
        )
        assert discrepancy <= 1.000001

    assert all(later < earlier for earlier, later in zip(errors, errors[1:]))
    assert errors[-1] < 2.0e-4
    print("balanced-shift sanity checks passed")


if __name__ == "__main__":
    main()
