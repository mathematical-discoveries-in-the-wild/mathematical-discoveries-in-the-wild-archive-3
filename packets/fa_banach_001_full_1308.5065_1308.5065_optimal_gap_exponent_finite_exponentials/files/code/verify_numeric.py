#!/usr/bin/env python3
"""High-precision checks for the Legendre--barycentric asymptotic."""

from math import comb, factorial

import mpmath as mp


mp.mp.dps = 90


def gram_matrix(frequencies: list[mp.mpf]) -> mp.matrix:
    size = len(frequencies)
    matrix = mp.matrix(size)
    for row in range(size):
        for column in range(size):
            difference = frequencies[row] - frequencies[column]
            matrix[row, column] = (
                2 * mp.pi
                if difference == 0
                else 2 * mp.sin(mp.pi * difference) / difference
            )
    return matrix


def least_eigenvalue(frequencies: list[mp.mpf]) -> mp.mpf:
    eigenvalues = mp.eigsy(gram_matrix(frequencies), eigvals_only=True)
    return eigenvalues[0]


def monic_legendre_norm(degree: int) -> mp.mpf:
    return (
        2
        * mp.pi ** (2 * degree + 1)
        * 4**degree
        / ((2 * degree + 1) * comb(2 * degree, degree) ** 2)
    )


def shape_constant(shape: tuple[int, ...]) -> mp.mpf:
    degree = len(shape) - 1
    weight_energy = mp.mpf("0")
    for j, node in enumerate(shape):
        denominator = mp.mpf("1")
        for k, other in enumerate(shape):
            if j != k:
                denominator *= node - other
        weight_energy += 1 / denominator**2
    return monic_legendre_norm(degree) / (factorial(degree) ** 2 * weight_energy)


def extremal_constant(n_terms: int) -> mp.mpf:
    degree = n_terms - 1
    return (
        2
        * mp.pi ** (2 * degree + 1)
        * 4**degree
        / ((2 * degree + 1) * comb(2 * degree, degree) ** 3)
    )


def run() -> None:
    shapes = {
        2: ((0, 1),),
        3: ((0, 1, 2), (0, 1, 3)),
        4: ((0, 1, 2, 3), (0, 1, 2, 4)),
    }
    delta = mp.mpf("0.02")

    for n_terms, family in shapes.items():
        sharp = extremal_constant(n_terms)
        arithmetic = family[0]
        assert mp.almosteq(shape_constant(arithmetic), sharp)

        for shape in family:
            predicted = shape_constant(shape)
            frequencies = [delta * node for node in shape]
            observed = least_eigenvalue(frequencies) / delta ** (2 * n_terms - 2)
            relative_error = abs(observed / predicted - 1)
            assert relative_error < mp.mpf("0.015")
            if shape != arithmetic:
                assert predicted > sharp
            print(
                f"N={n_terms} shape={shape} "
                f"observed={mp.nstr(observed, 16)} "
                f"predicted={mp.nstr(predicted, 16)} "
                f"relative_error={mp.nstr(relative_error, 5)}"
            )

    # A hierarchical three-node configuration has a much larger normalized
    # value than the single arithmetic cluster, as the multi-cluster lemma predicts.
    for delta_text in ("0.02", "0.01", "0.005"):
        hierarchical_delta = mp.mpf(delta_text)
        frequencies = [mp.mpf("0"), hierarchical_delta, mp.sqrt(hierarchical_delta)]
        normalized = least_eigenvalue(frequencies) / hierarchical_delta**4
        print(
            f"N=3 hierarchical delta={delta_text} "
            f"normalized={mp.nstr(normalized, 16)}"
        )
    print("PASS")


if __name__ == "__main__":
    run()
