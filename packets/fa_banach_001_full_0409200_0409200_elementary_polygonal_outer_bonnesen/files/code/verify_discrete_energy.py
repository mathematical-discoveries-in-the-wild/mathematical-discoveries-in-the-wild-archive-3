#!/usr/bin/env python3
"""Consistency checks for the polygonal outer-anticircle proof packet."""

from __future__ import annotations

import argparse
import math
import random


def edge_energy(alpha: float, x: float, y: float) -> float:
    return (math.cos(alpha) * (x * x + y * y) - 2 * x * y) / math.sin(alpha)


def merge_remainder(a: float, b: float, x: float, z: float, y: float) -> float:
    center = (x * math.sin(b) + y * math.sin(a)) / math.sin(a + b)
    return math.sin(a + b) / (math.sin(a) * math.sin(b)) * (z - center) ** 2


def support_area(angles: list[float], support: list[float]) -> float:
    n = len(angles)
    gaps = [(angles[(i + 1) % n] - angles[i]) % (2 * math.pi) for i in range(n)]
    adjacent = sum(
        support[i] * support[(i + 1) % n] / math.sin(gaps[i]) for i in range(n)
    )
    diagonal = 0.5 * sum(
        support[i] ** 2
        * (1 / math.tan(gaps[i - 1]) + 1 / math.tan(gaps[i]))
        for i in range(n)
    )
    return adjacent - diagonal


def support_vertices(angles: list[float], support: list[float]) -> list[tuple[float, float]]:
    vertices: list[tuple[float, float]] = []
    n = len(angles)
    for i in range(n):
        j = (i + 1) % n
        a, b = angles[i], angles[j]
        determinant = math.sin(b - a)
        vertices.append(
            (
                (support[i] * math.sin(b) - support[j] * math.sin(a)) / determinant,
                (-support[i] * math.cos(b) + support[j] * math.cos(a)) / determinant,
            )
        )
    return vertices


def signed_shoelace(vertices: list[tuple[float, float]]) -> float:
    return 0.5 * sum(
        vertices[i][0] * vertices[(i + 1) % len(vertices)][1]
        - vertices[i][1] * vertices[(i + 1) % len(vertices)][0]
        for i in range(len(vertices))
    )


def path_quadratic(gaps: list[float], values: list[float]) -> float:
    assert len(values) == len(gaps) + 1
    cross = sum(
        values[i] * values[i + 1] / math.sin(gaps[i]) for i in range(len(gaps))
    )
    diagonal = 0.5 * sum(
        values[i] ** 2
        * (1 / math.tan(gaps[i - 1]) + 1 / math.tan(gaps[i]))
        for i in range(1, len(values) - 1)
    )
    return cross - diagonal


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=20260826)
    args = parser.parse_args()
    if args.trials < 1:
        parser.error("--trials must be positive")
    rng = random.Random(args.seed)

    max_merge_error = 0.0
    min_path_energy = math.inf
    max_area_error = 0.0
    max_q_energy_error = 0.0

    for _ in range(args.trials):
        a = rng.uniform(1e-3, 1.4)
        b = rng.uniform(1e-3, math.pi - a - 1e-3)
        x, z, y = (rng.uniform(-4, 4) for _ in range(3))
        lhs = edge_energy(a, x, z) + edge_energy(b, z, y) - edge_energy(a + b, x, y)
        rhs = merge_remainder(a, b, x, z, y)
        max_merge_error = max(max_merge_error, abs(lhs - rhs))
        assert abs(lhs - rhs) < 2e-11 * (1 + abs(lhs) + abs(rhs))
        assert rhs >= -1e-12

        pieces = rng.randint(2, 16)
        raw = [rng.random() for _ in range(pieces)]
        total = rng.uniform(1e-3, math.pi)
        gaps = [total * value / sum(raw) for value in raw]
        values = [0.0] + [rng.uniform(-5, 5) for _ in range(pieces - 1)] + [0.0]
        energy = sum(
            edge_energy(gaps[i], values[i], values[i + 1]) for i in range(pieces)
        )
        q_value = path_quadratic(gaps, values)
        min_path_energy = min(min_path_energy, energy)
        max_q_energy_error = max(max_q_energy_error, abs(q_value + energy / 2))
        assert energy >= -2e-9
        assert abs(q_value + energy / 2) < 2e-11 * (1 + abs(q_value) + abs(energy))

        n = rng.randint(3, 24)
        angles = [2 * math.pi * i / n for i in range(n)]
        support = [rng.uniform(2, 3) for _ in range(n)]
        formula = support_area(angles, support)
        shoelace = signed_shoelace(support_vertices(angles, support))
        max_area_error = max(max_area_error, abs(formula - shoelace))
        assert abs(formula - shoelace) < 2e-9

    print(f"trials: {args.trials}")
    print(f"seed: {args.seed}")
    print(f"maximum merge-identity error: {max_merge_error:.3e}")
    print(f"minimum zero-endpoint path energy: {min_path_energy:.3e}")
    print(f"maximum Q + energy/2 error: {max_q_energy_error:.3e}")
    print(f"maximum support-area/shoelace error: {max_area_error:.3e}")
    print("all checks passed")


if __name__ == "__main__":
    main()
