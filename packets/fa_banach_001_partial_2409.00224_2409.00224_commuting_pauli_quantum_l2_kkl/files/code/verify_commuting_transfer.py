#!/usr/bin/env python3
"""Finite checks for the commuting-Pauli-to-classical influence transfer."""

from __future__ import annotations

import itertools
import random

import numpy as np


def rank2(rows: np.ndarray) -> int:
    a = (rows.copy() % 2).astype(np.uint8)
    rank = 0
    for col in range(a.shape[1]):
        pivots = np.flatnonzero(a[rank:, col])
        if not len(pivots):
            continue
        pivot = rank + int(pivots[0])
        a[[rank, pivot]] = a[[pivot, rank]]
        for row in range(a.shape[0]):
            if row != rank and a[row, col]:
                a[row] ^= a[rank]
        rank += 1
        if rank == a.shape[0]:
            break
    return rank


def symplectic(u: np.ndarray, v: np.ndarray, n: int) -> int:
    return int((u[:n] @ v[n:] + u[n:] @ v[:n]) % 2)


def random_isotropic_generators(n: int, m: int, rng: random.Random) -> np.ndarray:
    generators: list[np.ndarray] = []
    while len(generators) < m:
        v = np.array([rng.randrange(2) for _ in range(2 * n)], dtype=np.uint8)
        if not v.any() or any(symplectic(v, u, n) for u in generators):
            continue
        trial = np.array(generators + [v], dtype=np.uint8)
        if rank2(trial) == len(generators) + 1:
            generators.append(v)
    return np.array(generators, dtype=np.uint8)


def selected_dual_basis(generators: np.ndarray, n: int) -> tuple[np.ndarray, list[int]]:
    chosen: list[np.ndarray] = []
    qubits: list[int] = []
    for col in range(2 * n):
        functional = generators[:, col]
        trial = np.array(chosen + [functional], dtype=np.uint8)
        if rank2(trial) > len(chosen):
            chosen.append(functional.copy())
            qubits.append(col if col < n else col - n)
        if len(chosen) == generators.shape[0]:
            break
    # Columns are the selected functionals: eta = xi @ transform.
    return np.column_stack(chosen), qubits


def walsh_coefficients(values: np.ndarray) -> np.ndarray:
    coeffs = values.astype(float).copy()
    width = 1
    while width < len(coeffs):
        for start in range(0, len(coeffs), 2 * width):
            for offset in range(width):
                i, j = start + offset, start + offset + width
                x, y = coeffs[i], coeffs[j]
                coeffs[i], coeffs[j] = x + y, x - y
        width *= 2
    return coeffs / len(coeffs)


def bits(index: int, m: int) -> np.ndarray:
    return np.array([(index >> r) & 1 for r in range(m)], dtype=np.uint8)


def check_instance(generators: np.ndarray, values: np.ndarray) -> None:
    m, twice_n = generators.shape
    n = twice_n // 2
    transform, qubits = selected_dual_basis(generators, n)
    assert rank2(transform) == m

    hat_f = walsh_coefficients(values)
    q = np.zeros(n)
    hat_g_sq = np.zeros_like(hat_f)
    for xi_index, coefficient in enumerate(hat_f):
        xi = bits(xi_index, m)
        physical = (xi @ generators) % 2
        for j in range(n):
            if physical[j] or physical[n + j]:
                q[j] += coefficient**2
        eta = (xi @ transform) % 2
        eta_index = sum(int(eta[r]) << r for r in range(m))
        hat_g_sq[eta_index] = coefficient**2

    for r, qubit in enumerate(qubits):
        classical = sum(
            hat_g_sq[index] for index in range(1 << m) if (index >> r) & 1
        )
        assert classical <= q[qubit] + 1e-12


def main() -> None:
    rng = random.Random(240900224)
    checked = 0
    for n in range(1, 6):
        for m in range(1, n + 1):
            for _ in range(20):
                generators = random_isotropic_generators(n, m, rng)
                if m <= 3:
                    samples = list(itertools.combinations(range(1 << m), 1 << (m - 1)))
                else:
                    samples = [
                        tuple(rng.sample(range(1 << m), 1 << (m - 1)))
                        for _ in range(30)
                    ]
                for positive in samples:
                    values = -np.ones(1 << m)
                    values[list(positive)] = 1
                    check_instance(generators, values)
                    checked += 1
    print(f"verified {checked} balanced commuting-Pauli instances")


if __name__ == "__main__":
    main()
