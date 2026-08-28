#!/usr/bin/env python3
"""Finite-graph regression for the half-gasket reflection identity.

This is not the proof.  It builds level-m graph approximations of SG_l from
the standard triangular IFS, checks reflection invariance of the edge set, and
tests E_m(Eu) = 2 E_{m,half}(u) for seeded random symmetric vertex data.
"""

from __future__ import annotations

from fractions import Fraction
import random


Point = tuple[Fraction, Fraction]
Edge = frozenset[Point]

Q0: Point = (Fraction(0), Fraction(1))
Q1: Point = (Fraction(-1), Fraction(0))
Q2: Point = (Fraction(1), Fraction(0))


def add(x: Point, y: Point) -> Point:
    return (x[0] + y[0], x[1] + y[1])


def scale(a: Fraction, x: Point) -> Point:
    return (a * x[0], a * x[1])


def reflect(x: Point) -> Point:
    return (-x[0], x[1])


def first_level_offsets(level_l: int) -> list[Point]:
    """Offsets d for F_d(x)=x/l+d, indexed by i+j+k=l-1."""
    ans: list[Point] = []
    for i in range(level_l):
        for j in range(level_l - i):
            k = level_l - 1 - i - j
            numerator = add(add(scale(Fraction(i), Q0), scale(Fraction(j), Q1)),
                            scale(Fraction(k), Q2))
            ans.append(scale(Fraction(1, level_l), numerator))
    return ans


def graph_edges(level_l: int, depth: int) -> set[Edge]:
    # Each affine cell map is x |-> a*x+b.
    cells: list[tuple[Fraction, Point]] = [(Fraction(1), (Fraction(0), Fraction(0)))]
    offsets = first_level_offsets(level_l)
    for _ in range(depth):
        next_cells: list[tuple[Fraction, Point]] = []
        for a, b in cells:
            for d in offsets:
                next_cells.append((a / level_l, add(b, scale(a, d))))
        cells = next_cells

    edges: set[Edge] = set()
    for a, b in cells:
        vertices = [add(b, scale(a, q)) for q in (Q0, Q1, Q2)]
        edges.update({frozenset((vertices[0], vertices[1])),
                      frozenset((vertices[1], vertices[2])),
                      frozenset((vertices[2], vertices[0]))})
    return edges


def reflected_edge(edge: Edge) -> Edge:
    return frozenset(reflect(x) for x in edge)


def midpoint_x(edge: Edge) -> Fraction:
    x, y = tuple(edge)
    return (x[0] + y[0]) / 2


def run() -> None:
    rng = random.Random(170202419)
    cases = 0
    for level_l in range(2, 7):
        max_depth = 3 if level_l <= 4 else 2
        for depth in range(1, max_depth + 1):
            edges = graph_edges(level_l, depth)
            assert all(reflected_edge(e) in edges for e in edges)
            vertices = {x for e in edges for x in e}

            # There are no nontrivial graph edges contained in the vertical
            # symmetry axis.  Every setwise-fixed edge crosses the axis and
            # has its endpoints exchanged by reflection.
            for edge in edges:
                if reflected_edge(edge) == edge:
                    x, y = tuple(edge)
                    assert reflect(x) == y

            for _ in range(20):
                values: dict[Point, int] = {}
                for x in vertices:
                    key = min(x, reflect(x))
                    if key not in values:
                        values[key] = rng.randrange(-50, 51)

                def value(x: Point) -> int:
                    return values[min(x, reflect(x))]

                full = sum((value(x) - value(y)) ** 2 for x, y in map(tuple, edges))
                left = sum(
                    (value(x) - value(y)) ** 2
                    for edge in edges
                    if midpoint_x(edge) < 0
                    for x, y in [tuple(edge)]
                )
                assert full == 2 * left, (level_l, depth, full, left)
                cases += 1

    print(f"verified {cases} seeded finite-graph cases")
    print("exact identity E_m(Eu) = 2 E_{m,half}(u) held in every case")


if __name__ == "__main__":
    run()
