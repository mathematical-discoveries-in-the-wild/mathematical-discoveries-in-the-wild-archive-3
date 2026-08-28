#!/usr/bin/env python3
"""Finite matrix diagnostics for the in-tree constant-two proof."""

from __future__ import annotations

import itertools
import numpy as np


def ancestors(parent: list[int], vertex: int) -> list[int]:
    out = [vertex]
    while out[-1] != 0:
        out.append(parent[out[-1]])
    return out


def path_model(parent: list[int]):
    """Return paths (range, source) and their left-regular matrices."""
    n = len(parent)
    paths = []
    for source in range(n):
        paths.extend((target, source) for target in ancestors(parent, source))
    index = {path: i for i, path in enumerate(paths)}
    matrices = {}
    for target, source in paths:
        mat = np.zeros((len(paths), len(paths)), dtype=complex)
        for q_target, q_source in paths:
            if q_target == source:
                mat[index[(target, q_source)], index[(q_target, q_source)]] = 1
        matrices[(target, source)] = mat
    return paths, index, matrices


def one_trial(rng: np.random.Generator, n: int) -> tuple[float, float]:
    parent = [0] + [int(rng.integers(0, vertex)) for vertex in range(1, n)]
    paths, index, mats = path_model(parent)
    coeff = {
        path: rng.normal() + 1j * rng.normal()
        for path in paths
    }
    vertex_paths = [(v, v) for v in range(n)]
    positive_paths = [path for path in paths if path[0] != path[1]]
    diagonal = sum((coeff[p] * mats[p] for p in vertex_paths),
                   np.zeros_like(next(iter(mats.values()))))
    off_diagonal = sum((coeff[p] * mats[p] for p in positive_paths),
                       np.zeros_like(diagonal))
    implementer = diagonal + off_diagonal

    averaged_difference = np.zeros_like(implementer)
    max_commutator_norm = 0.0
    for signs in itertools.product((-1.0, 1.0), repeat=n):
        unitary = sum((signs[v] * mats[(v, v)] for v in range(n)),
                      np.zeros_like(implementer))
        commutator = unitary @ implementer - implementer @ unitary
        averaged_difference += implementer - unitary @ implementer @ unitary.conj().T
        max_commutator_norm = max(
            max_commutator_norm, np.linalg.norm(commutator, 2)
        )
    averaged_difference /= 2**n
    if not np.allclose(averaged_difference, off_diagonal, atol=2e-10):
        raise AssertionError("sign average did not recover the off-diagonal part")
    if np.linalg.norm(off_diagonal, 2) > max_commutator_norm + 2e-10:
        raise AssertionError("off-diagonal norm exceeded sign-commutator bound")

    max_coefficient_error = 0.0
    max_endpoint_difference = 0.0
    for target, source in positive_paths:
        lp = mats[(target, source)]
        delta_lp = lp @ implementer - implementer @ lp
        source_vector = np.zeros(len(paths), dtype=complex)
        source_vector[index[(source, source)]] = 1
        path_vector = np.zeros(len(paths), dtype=complex)
        path_vector[index[(target, source)]] = 1
        extracted = np.vdot(path_vector, delta_lp @ source_vector)
        expected = coeff[(source, source)] - coeff[(target, target)]
        max_coefficient_error = max(
            max_coefficient_error, abs(extracted - expected)
        )
        max_endpoint_difference = max(max_endpoint_difference, abs(expected))
    if max_coefficient_error > 2e-10:
        raise AssertionError("path coefficient identity failed")

    root_spread = max(abs(coeff[(v, v)] - coeff[(0, 0)]) for v in range(n))
    if root_spread > max_endpoint_difference + 2e-10:
        raise AssertionError("root path did not control the diagonal spread")
    return max_coefficient_error, np.linalg.norm(
        averaged_difference - off_diagonal, 2
    )


def main() -> None:
    rng = np.random.default_rng(250722508)
    trials = 0
    worst_coefficient_error = 0.0
    worst_average_error = 0.0
    for n in range(2, 8):
        for _ in range(25):
            coefficient_error, average_error = one_trial(rng, n)
            worst_coefficient_error = max(worst_coefficient_error, coefficient_error)
            worst_average_error = max(worst_average_error, average_error)
            trials += 1
    print(f"PASS: {trials} random rooted in-tree matrix models")
    print(f"PASS: worst path-coefficient error = {worst_coefficient_error:.3e}")
    print(f"PASS: worst sign-average error = {worst_average_error:.3e}")


if __name__ == "__main__":
    main()
