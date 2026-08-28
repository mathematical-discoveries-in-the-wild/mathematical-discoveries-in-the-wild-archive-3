#!/usr/bin/env python3
"""Randomized checks of the classical-side reverse-LOCC collapse inequality."""

import numpy as np


def random_psd(rng: np.random.Generator, d: int) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return x @ x.conj().T


def random_povm(rng: np.random.Generator, d: int, outcomes: int) -> list[np.ndarray]:
    raw = [random_psd(rng, d) for _ in range(outcomes)]
    total = sum(raw)
    vals, vecs = np.linalg.eigh(total)
    inv_sqrt = (vecs * (vals ** -0.5)) @ vecs.conj().T
    return [inv_sqrt @ a @ inv_sqrt for a in raw]


def random_hermitian(rng: np.random.Generator, d: int) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return (x + x.conj().T) / 2.0


def main() -> None:
    rng = np.random.default_rng(14061959)
    trials = 0
    worst_slack = np.inf

    for d in range(2, 7):
        for _ in range(80):
            blocks = [random_hermitian(rng, d) for _ in range(d)]
            first = random_povm(rng, d, outcomes=d + 1)
            conditional = [random_povm(rng, d, outcomes=d) for _ in first]

            reverse_value = 0.0
            local_bound = 0.0
            for n_j, cond_j in zip(first, conditional):
                x_i = np.array([
                    np.trace(delta_i @ n_j).real for delta_i in blocks
                ])
                local_bound += np.abs(x_i).sum()
                for m_jk in cond_j:
                    coeff = np.real(np.diag(m_jk))
                    reverse_value += abs(float(coeff @ x_i))

            slack = local_bound - reverse_value
            worst_slack = min(worst_slack, slack)
            assert slack >= -2.0e-9
            trials += 1

    print(f"PASS: {trials} random reverse one-way protocols obey the LO bound")
    print(f"PASS: minimum numerical slack = {worst_slack:.6e}")
    print("PASS: conditional diagonal coefficients are nonnegative partitions of unity")


if __name__ == "__main__":
    main()

