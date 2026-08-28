#!/usr/bin/env python3
"""Construct and verify the Wronskian recurrence for a small row.

This imports the exact Burnside formula from the promoted partial packet.  It
chooses a basis of the fixed-subset polynomials Q_{lambda,eta}, constructs the
minimal-order Wronskian differential operator attached to that basis, and
checks that the resulting scalar operator annihilates F_n(x).
"""

from __future__ import annotations

import importlib.util
from functools import reduce
from pathlib import Path

import sympy as sp


REPO_ROOT = Path(__file__).resolve().parents[3]
LOCAL_VERIFIER = Path(__file__).resolve().with_name("verifier.py")
BASE_VERIFIER = (
    LOCAL_VERIFIER
    if LOCAL_VERIFIER.exists()
    else REPO_ROOT
    / "runs/fa_banach_001/solutions/full/"
    / "2503.09542_orbit_count_cycle_index_formula/code/verifier.py"
)


def load_base_verifier():
    spec = importlib.util.spec_from_file_location("orbit_verifier", BASE_VERIFIER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {BASE_VERIFIER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixed_subset_polynomials(base, n: int, x: sp.Symbol) -> list[sp.Poly]:
    degree = sp.factorial(n)
    output: list[sp.Poly] = []
    for left_type in base.partitions(n):
        for right_type in base.partitions(n):
            coefficients = base.fixed_subset_polynomial(
                base.action_cycle_counts(left_type, right_type), degree
            )
            expression = sum(value * x**power for power, value in enumerate(coefficients))
            polynomial = sp.Poly(expression, x, domain=sp.QQ)
            if polynomial not in output:
                output.append(polynomial)
    return output


def polynomial_basis(polynomials: list[sp.Poly], x: sp.Symbol) -> list[sp.Expr]:
    maximum_degree = max(poly.degree() for poly in polynomials)
    columns = sp.Matrix(
        maximum_degree + 1,
        len(polynomials),
        lambda row, column: polynomials[column].nth(row),
    )
    _, pivot_columns = columns.rref()
    return [polynomials[index].as_expr() for index in pivot_columns]


def wronskian_operator_coefficients(
    basis: list[sp.Expr], x: sp.Symbol
) -> list[sp.Poly]:
    """Return A_j such that sum_j A_j(x) y^(j)(x) kills the basis."""
    order = len(basis)
    derivative_matrix = sp.Matrix(
        order + 1,
        order,
        lambda row, column: sp.diff(basis[column], x, row),
    )
    coefficients: list[sp.Poly] = []
    for derivative_order in range(order + 1):
        minor = derivative_matrix.copy()
        minor.row_del(derivative_order)
        cofactor = (-1) ** (derivative_order + order) * minor.det(method="domain-ge")
        coefficients.append(sp.Poly(sp.expand(cofactor), x, domain=sp.QQ))

    common = reduce(sp.gcd, coefficients)
    if common.degree() >= 0 and not common.is_one:
        coefficients = [poly.exquo(common) for poly in coefficients]
    leading_coefficient = coefficients[-1].LC()
    coefficients = [sp.Poly(poly.as_expr() / leading_coefficient, x) for poly in coefficients]
    return coefficients


def main() -> None:
    base = load_base_verifier()
    x = sp.Symbol("x")
    for rank_n in range(1, 6):
        rank_polynomials = fixed_subset_polynomials(base, rank_n, x)
        rank_basis = polynomial_basis(rank_polynomials, x)
        print(
            f"n={rank_n}: distinct fixed-subset polynomials="
            f"{len(rank_polynomials)}, span dimension={len(rank_basis)}"
        )

    n = 3
    polynomials = fixed_subset_polynomials(base, n, x)
    basis = polynomial_basis(polynomials, x)
    coefficients = wronskian_operator_coefficients(basis, x)

    orbit_row = base.orbit_counts(n, sp.factorial(n))
    generating_polynomial = sum(value * x**power for power, value in enumerate(orbit_row))
    residual = sp.expand(
        sum(
            coefficient.as_expr() * sp.diff(generating_polynomial, x, order)
            for order, coefficient in enumerate(coefficients)
        )
    )
    assert residual == 0

    maximum_coefficient_degree = max(poly.degree() for poly in coefficients)
    for recurrence_index in range(sp.factorial(n) + maximum_coefficient_degree + 1):
        recurrence_residual = 0
        for derivative_order, coefficient in enumerate(coefficients):
            for power, scalar in enumerate(reversed(coefficient.all_coeffs())):
                sequence_index = recurrence_index + derivative_order - power
                if not 0 <= sequence_index < len(orbit_row):
                    continue
                if sequence_index < derivative_order:
                    continue
                falling = sp.prod(
                    sequence_index - offset for offset in range(derivative_order)
                )
                recurrence_residual += scalar * falling * orbit_row[sequence_index]
        assert recurrence_residual == 0, recurrence_index

    print(f"n={n}")
    print(f"distinct fixed-subset polynomials={len(polynomials)}")
    print(f"basis dimension / recurrence differential order={len(basis)}")
    for order, coefficient in enumerate(coefficients):
        print(f"A_{order}(x) = {sp.factor(coefficient.as_expr())}")
    print(f"F_{n}(x) = {sp.factor(generating_polynomial)}")
    print("Wronskian differential equation and scalar coefficient recurrence verified exactly.")


if __name__ == "__main__":
    main()
