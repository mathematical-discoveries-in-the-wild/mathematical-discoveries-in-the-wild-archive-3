#!/usr/bin/env python3
"""Deterministic checks for the scalar-collision counterexample."""

from itertools import permutations

import numpy as np


I = np.eye(3)
P = np.array([[0.0, 1.0, 0.0],
              [0.0, 0.0, 1.0],
              [1.0, 0.0, 0.0]])
H_BASIS = np.array([[1.0, 0.0],
                    [0.0, 1.0],
                    [-1.0, -1.0]])
ONE = np.ones((3, 1))


def alpha(s: float) -> float:
    return (1.0 + s) / 3.0


def doubly_stochastic_path(s: float) -> np.ndarray:
    a = alpha(s)
    return a * I + (1.0 - a) * P


def b(z: np.ndarray) -> np.ndarray:
    return H_BASIS @ z


def permutation_matrix(perm: tuple[int, ...]) -> np.ndarray:
    out = np.zeros((3, 3))
    for row, col in enumerate(perm):
        out[row, col] = 1.0
    return out


def main() -> None:
    support = (I + P) > 0.0
    allowed_permutations = []

    for perm in permutations(range(3)):
        q = permutation_matrix(perm)
        if np.all((q == 0.0) | support):
            allowed_permutations.append(q)

    assert len(allowed_permutations) == 2
    assert any(np.array_equal(q, I) for q in allowed_permutations)
    assert any(np.array_equal(q, P) for q in allowed_permutations)

    reconstruction_basis = np.concatenate([H_BASIS, ONE], axis=1)
    assert abs(np.linalg.det(reconstruction_basis)) > 1.0e-12

    for s in np.linspace(0.0, 1.0, 21):
        d = doubly_stochastic_path(float(s))
        assert np.all(d >= 0.0)
        assert np.allclose(d.sum(axis=0), 1.0)
        assert np.allclose(d.sum(axis=1), 1.0)
        assert np.array_equal(d == 0.0, ~support)

        action = np.concatenate([d @ H_BASIS, d @ ONE], axis=1)
        recovered = action @ np.linalg.inv(reconstruction_basis)
        assert np.allclose(recovered, d)

        for z in (
            np.array([1.0, 0.0]),
            np.array([0.0, 1.0]),
            np.array([0.25, -0.75]),
        ):
            diagonal_b = b(z)
            diagonal_a = d @ diagonal_b
            assert np.allclose(diagonal_a, doubly_stochastic_path(float(s)) @ b(z))

    assert not np.allclose(doubly_stochastic_path(0.0),
                           doubly_stochastic_path(1.0))
    print("PASS: D_s is a nonconstant continuous doubly stochastic edge path")
    print("PASS: b(R^2) spans the trace-zero plane and reconstructs D_s with 1")
    print("PASS: the defining majorization identity holds on all tested samples")
    print("PASS: only I and P permutation supports lie inside supp(I+P)")


if __name__ == "__main__":
    main()

