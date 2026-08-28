#!/usr/bin/env python3
"""Numerical sanity checks for the finite-edge negative-type proof.

These checks are corroborative only.  The packet's proof is analytic.
"""

from __future__ import annotations

import math
import random

import mpmath as mp
import numpy as np


def safe_exponent(edge_count: int) -> float:
    return 1.0 + (2.0 / math.pi) * math.asin(
        1.0 / (2.0 * max(1, edge_count - 1))
    )


def kernel_multiplier_ratio(alpha: float, xi: float) -> float:
    """The exact Mellin multiplier ratio bhat/ahat."""
    return math.cos(math.pi * alpha / 2.0) / math.cosh(math.pi * xi)


def gamma_formula_ratio(alpha: float, xi: float) -> float:
    """Compute bhat/ahat from the two beta/gamma formulas in the proof."""
    z = mp.mpf(alpha) / 2 + 1j * mp.mpf(xi)
    b_hat = abs(mp.gamma(z)) ** 2 / mp.gamma(alpha)
    a_hat = mp.gamma(1 - alpha) * (
        mp.gamma(z) / mp.gamma(1 - mp.conj(z))
        + mp.gamma(mp.conj(z)) / mp.gamma(1 - z)
    )
    return float(mp.re(b_hat / a_hat))


def random_weighted_tree(rng: random.Random, vertices: int):
    parent = [-1]
    length = [0.0]
    for child in range(1, vertices):
        parent.append(rng.randrange(child))
        length.append(rng.uniform(0.2, 2.0))
    return parent, length


def distance_matrix(parent, length):
    n = len(parent)
    adjacency = [[] for _ in range(n)]
    for child in range(1, n):
        par = parent[child]
        weight = length[child]
        adjacency[child].append((par, weight))
        adjacency[par].append((child, weight))

    distances = np.zeros((n, n), dtype=float)
    for source in range(n):
        stack = [(source, -1, 0.0)]
        while stack:
            vertex, previous, distance = stack.pop()
            distances[source, vertex] = distance
            for neighbor, weight in adjacency[vertex]:
                if neighbor != previous:
                    stack.append((neighbor, vertex, distance + weight))
    return distances


def maximum_zero_sum_eigenvalue(distances: np.ndarray, exponent: float) -> float:
    n = distances.shape[0]
    projection = np.eye(n) - np.ones((n, n)) / n
    compressed = projection @ np.power(distances, exponent) @ projection
    return float(np.linalg.eigvalsh(compressed).max())


def main() -> None:
    # The closed formula is even and has its maximum at xi=0.  Check a grid.
    for alpha in (0.1, 0.25, 0.5, 0.8, 0.95):
        values = [kernel_multiplier_ratio(alpha, xi) for xi in np.linspace(-8, 8, 4001)]
        expected = math.cos(math.pi * alpha / 2.0)
        assert max(values) <= expected + 1e-14
        assert abs(kernel_multiplier_ratio(alpha, 0.0) - expected) < 1e-14
        for xi in (-3.0, -0.7, 0.0, 0.4, 2.5):
            assert abs(gamma_formula_ratio(alpha, xi) - kernel_multiplier_ratio(alpha, xi)) < 2e-13

    rng = random.Random(20260827)
    cases = 0
    worst = -math.inf
    # A finite weighted tree with E edges is itself a finite-topological tree
    # with E open edges, so the packet's explicit safe exponent applies.
    for vertices in range(3, 15):
        edge_count = vertices - 1
        exponent = safe_exponent(edge_count)
        for _ in range(200):
            parent, length = random_weighted_tree(rng, vertices)
            distances = distance_matrix(parent, length)
            maximum = maximum_zero_sum_eigenvalue(distances, exponent)
            scale = max(1.0, float(np.power(distances, exponent).max()))
            assert maximum <= 2e-10 * scale, (vertices, exponent, maximum)
            worst = max(worst, maximum / scale)
            cases += 1

    print("kernel multiplier grids: 5 x 4001 points passed")
    print("beta/gamma formula comparisons: 25 points passed")
    print(f"random weighted trees: {cases} cases passed")
    print(f"largest normalized zero-sum eigenvalue: {worst:.3e}")


if __name__ == "__main__":
    main()
