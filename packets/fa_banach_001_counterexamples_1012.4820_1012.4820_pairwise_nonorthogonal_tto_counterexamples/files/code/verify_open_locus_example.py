#!/usr/bin/env python3
"""Numerical sanity check for the explicit nonempty-locus construction.

This does not verify the semialgebraic dimension theorem.  It checks the
elementary construction used to prove that the pairwise-nonorthogonal,
simple-spectrum locus is nonempty and checks the numerical dimension gap.
"""

import numpy as np
from scipy.linalg import expm


def main() -> None:
    n = 10
    t = 1.0e-2
    k = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            k[i, j] = 1.0
            k[j, i] = -1.0

    q = expm(1j * t * k)
    lambdas = np.arange(1, n + 1, dtype=float)
    s = q @ np.diag(lambdas) @ q.T
    gram = q.conj().T @ q
    offdiag = gram - np.diag(np.diag(gram))
    nonzero_offdiag = np.abs(offdiag[np.triu_indices(n, 1)])

    tto_bound = 7 * n - 6 + n * (n - 1) // 2
    ambient_dimension = n * (n + 1)

    print(f"n={n}, t={t}")
    print(f"max ||Q^T Q-I|| entry = {np.max(np.abs(q.T @ q - np.eye(n))):.3e}")
    print(f"max ||S^T-S|| entry = {np.max(np.abs(s.T - s)):.3e}")
    print(f"min |<q_i,q_j>|, i<j = {np.min(nonzero_offdiag):.12f}")
    print(f"max eigenvector residual = {np.max(np.abs(s @ q - q @ np.diag(lambdas))):.3e}")
    print(f"TTO-locus dimension bound = {tto_bound}")
    print(f"ambient/full-open-locus dimension = {ambient_dimension}")
    print(f"strict dimension gap = {ambient_dimension - tto_bound}")

    assert np.max(np.abs(q.T @ q - np.eye(n))) < 1e-12
    assert np.max(np.abs(s.T - s)) < 1e-12
    assert np.min(nonzero_offdiag) > 0
    assert np.max(np.abs(s @ q - q @ np.diag(lambdas))) < 1e-11
    assert tto_bound < ambient_dimension


if __name__ == "__main__":
    main()
