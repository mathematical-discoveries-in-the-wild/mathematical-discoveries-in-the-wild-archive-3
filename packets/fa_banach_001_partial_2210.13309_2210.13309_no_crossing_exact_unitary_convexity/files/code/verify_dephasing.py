"""Numerical sanity checks for the equal-weight dephasing construction."""

from __future__ import annotations

import numpy as np


def random_unitary(rng: np.random.Generator, n: int) -> np.ndarray:
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = np.where(np.abs(phases) > 0, phases / np.abs(phases), 1.0)
    return q @ np.diag(np.conjugate(phases))


def check_size(rng: np.random.Generator, n: int) -> tuple[float, float, float]:
    b = np.sort(rng.normal(size=n))[::-1]
    # Make accidental near-collisions irrelevant to the numerical check.
    b += 0.31 * np.arange(n, 0, -1)
    db = np.diag(b)

    q = random_unitary(rng, n)
    v = random_unitary(rng, n)
    w = random_unitary(rng, n)
    h = q @ db @ q.conj().T
    da = np.diag(np.diag(h))
    a = v.conj().T @ da @ v
    big_b = w.conj().T @ db @ w

    omega = np.exp(2j * np.pi / n)
    phase = np.diag(omega ** np.arange(n))
    dephased = sum(
        np.linalg.matrix_power(phase, -k)
        @ h
        @ np.linalg.matrix_power(phase, k)
        for k in range(n)
    ) / n

    unitaries = [
        w.conj().T @ q.conj().T @ np.linalg.matrix_power(phase, k) @ v
        for k in range(n)
    ]
    reconstructed = sum(u.conj().T @ big_b @ u for u in unitaries) / n
    unitary_residual = max(
        np.linalg.norm(u.conj().T @ u - np.eye(n), ord="fro")
        for u in unitaries
    )
    return (
        float(np.linalg.norm(dephased - da, ord="fro")),
        float(unitary_residual),
        float(np.linalg.norm(reconstructed - a, ord="fro")),
    )


def main() -> None:
    rng = np.random.default_rng(221013309)
    for n in range(2, 9):
        residuals = np.array([check_size(rng, n) for _ in range(20)])
        maxima = residuals.max(axis=0)
        assert np.all(maxima < 1.0e-12), (n, maxima)
        print(
            f"n={n}: dephase={maxima[0]:.3e} "
            f"unitary={maxima[1]:.3e} reconstruction={maxima[2]:.3e}"
        )
    print("all dephasing and conjugation checks passed")


if __name__ == "__main__":
    main()
