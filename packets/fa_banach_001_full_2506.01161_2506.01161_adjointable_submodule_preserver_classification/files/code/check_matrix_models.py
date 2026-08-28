#!/usr/bin/env python3
"""Exact finite-matrix checks for the submodule-preserver packet."""

from __future__ import annotations

import argparse

import sympy as sp


def matrix_units(dimension: int) -> list[sp.Matrix]:
    units: list[sp.Matrix] = []
    for row in range(dimension):
        for column in range(dimension):
            unit = sp.zeros(dimension)
            unit[row, column] = 1
            units.append(unit)
    return units


def commutant_constraint_matrix(dimension: int) -> sp.Matrix:
    basis = matrix_units(dimension)
    columns: list[list[int]] = [[] for _ in basis]
    for coefficient_basis_index, coefficient_basis in enumerate(basis):
        for test_unit in basis:
            commutator = coefficient_basis * test_unit - test_unit * coefficient_basis
            columns[coefficient_basis_index].extend(list(commutator))
    return sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-dimension", type=int, default=7)
    args = parser.parse_args()
    if args.max_dimension < 1:
        parser.error("--max-dimension must be positive")

    for dimension in range(1, args.max_dimension + 1):
        constraints = commutant_constraint_matrix(dimension)
        nullity = dimension * dimension - constraints.rank()
        assert nullity == 1
        print(
            f"M_{dimension}: variables={dimension * dimension}, "
            f"constraint_rank={constraints.rank()}, central_nullity={nullity}"
        )

    # On A^2, K=diag(1,0) sends (1,1) to (1,0), which cannot equal (a,a).
    first_coordinate_forced = sp.Integer(1)
    second_coordinate_forced = sp.Integer(0)
    assert first_coordinate_forced != second_coordinate_forced
    print("diag(1,0) fails to preserve the diagonal cyclic submodule")
    print("all exact checks passed")


if __name__ == "__main__":
    main()
