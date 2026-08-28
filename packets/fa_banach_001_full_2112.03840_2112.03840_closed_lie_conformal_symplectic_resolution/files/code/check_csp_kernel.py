#!/usr/bin/env python3
"""Sanity checks for the conformal-symplectic kernel packet.

This script is not part of the proof. It checks elementary conformal-symplectic
matrices, determinant scaling, kernel covariance, and swap parity for m=1,2,3.
"""

from __future__ import annotations

import numpy as np


def symplectic_form_matrix(m: int) -> np.ndarray:
    eye = np.eye(m)
    zero = np.zeros((m, m))
    return np.block([[zero, eye], [-eye, zero]])


def random_symplectic(rng: np.random.Generator, m: int) -> np.ndarray:
    while True:
        a = rng.normal(size=(m, m))
        if abs(np.linalg.det(a)) > 0.2:
            break
    block = np.block(
        [[a, np.zeros((m, m))], [np.zeros((m, m)), np.linalg.inv(a).T]]
    )
    b = rng.normal(size=(m, m))
    b = (b + b.T) / 2.0
    shear = np.block([[np.eye(m), b], [np.zeros((m, m)), np.eye(m)]])
    return shear @ block


def run_checks() -> None:
    rng = np.random.default_rng(20260827)
    trials = 200
    for m in (1, 2, 3):
        j = symplectic_form_matrix(m)
        for _ in range(trials):
            s = random_symplectic(rng, m)
            r = float(np.exp(rng.normal(scale=0.4)))
            g = r * s
            c = r * r
            assert np.allclose(g.T @ j @ g, c * j, rtol=1e-9, atol=1e-9)
            assert np.isclose(np.linalg.det(g), c**m, rtol=1e-9, atol=1e-9)

            x = rng.normal(size=2 * m)
            y = rng.normal(size=2 * m)
            omega = float(x @ j @ y)
            if abs(omega) < 1e-6:
                continue
            transformed = float((g @ x) @ j @ (g @ y))
            kernel = omega ** (-m)
            transformed_kernel = transformed ** (-m)
            assert np.isclose(
                transformed_kernel,
                kernel / np.linalg.det(g),
                rtol=1e-8,
                atol=1e-8,
            )
            swapped_kernel = (-omega) ** (-m)
            assert np.isclose(swapped_kernel, ((-1) ** m) * kernel)
        print(f"m={m}: {trials} determinant/covariance/parity trials passed")


if __name__ == "__main__":
    run_checks()

