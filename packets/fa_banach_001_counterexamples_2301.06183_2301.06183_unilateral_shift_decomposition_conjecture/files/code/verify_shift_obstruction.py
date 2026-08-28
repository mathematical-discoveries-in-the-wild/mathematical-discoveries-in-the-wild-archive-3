#!/usr/bin/env python3
"""Finite-dimensional sanity checks for the unilateral-shift obstruction.

The proof in the packet is infinite-dimensional and exact.  These computations
only check its finite nilpotent-shift analogue and the matrix bookkeeping.
"""

from __future__ import annotations

import numpy as np


def truncated_shift(size: int) -> np.ndarray:
    shift = np.zeros((size, size), dtype=float)
    for index in range(size - 1):
        shift[index + 1, index] = 1.0
    return shift


def joint_commutant_nullity(shift: np.ndarray) -> int:
    """Dimension of matrices commuting with both S and S*."""
    size = shift.shape[0]
    identity = np.eye(size)
    # Column-major vectorization: vec(AS-SA) =
    # (S^T tensor I - I tensor S) vec(A).
    commute_s = np.kron(shift.T, identity) - np.kron(identity, shift)
    adjoint = shift.T
    commute_s_star = np.kron(adjoint.T, identity) - np.kron(identity, adjoint)
    constraints = np.vstack([commute_s, commute_s_star])
    rank = np.linalg.matrix_rank(constraints, tol=1e-10)
    return size * size - rank


def main() -> None:
    tested = 0
    for size in range(2, 41):
        shift = truncated_shift(size)

        # The orbit of e_0 through time size-1 is the standard ONB.
        e0 = np.eye(size)[:, 0]
        orbit = []
        vector = e0.copy()
        for _ in range(size):
            orbit.append(vector)
            vector = shift @ vector
        orbit_matrix = np.column_stack(orbit)
        assert np.allclose(orbit_matrix.T @ orbit_matrix, np.eye(size))

        # Only scalar matrices commute with both the shift and its adjoint.
        assert joint_commutant_nullity(shift) == 1
        tested += 1

    print(f"truncated shifts tested: {tested} (dimensions 2 through 40)")
    print("orbit Gram matrices: all identity")
    print("joint commutant dimensions: all equal to 1")


if __name__ == "__main__":
    main()
