"""Independent finite-dimensional sanity checks for the counterexample.

The exact norm lower bounds are proved in the packet; this script checks the
matrix identities, the Hilbert--Schmidt operator norm, and sampled positivity.
"""

import numpy as np


def matrix_unit(i: int, j: int) -> np.ndarray:
    result = np.zeros((4, 4), dtype=complex)
    result[i, j] = 1
    return result


J = np.array([[0, 1], [-1, 0]], dtype=complex)
U = np.block([[J, np.zeros((2, 2))], [np.zeros((2, 2)), J]])
I4 = np.eye(4, dtype=complex)


def T(x: np.ndarray) -> np.ndarray:
    return (np.trace(x) * I4 - x - U @ x.T @ U.conj().T) / 2


def main() -> None:
    E = matrix_unit
    xs = [E(3, 0) - E(1, 2), -(E(0, 0) + E(1, 1)), E(2, 0) + E(1, 3)]
    ys = [-xs[0], -(E(2, 2) + E(3, 3)), -xs[2]]
    residuals = [np.linalg.norm(T(x) - y) for x, y in zip(xs, ys)]
    assert max(residuals) < 1e-12

    basis = [E(i, j) for i in range(4) for j in range(4)]
    superoperator = np.column_stack([T(e).reshape(-1) for e in basis])
    singular_values = np.linalg.svd(superoperator, compute_uv=False)
    assert np.allclose(singular_values[:6], 1)
    assert np.allclose(singular_values[6:], 0)

    rng = np.random.default_rng(190703995)
    for _ in range(500):
        xi = rng.normal(size=4) + 1j * rng.normal(size=4)
        image = T(np.outer(xi, xi.conj()))
        assert np.linalg.eigvalsh(image).min() > -1e-10

    ratio = 2 * np.sqrt(3) / np.sqrt(6 * np.sqrt(3))
    assert ratio > 1
    print("output residuals:", residuals)
    print("singular values:", np.round(singular_values, 12))
    print("amplification ratio:", ratio)
    print("sampled rank-one positivity checks: 500")


if __name__ == "__main__":
    main()
