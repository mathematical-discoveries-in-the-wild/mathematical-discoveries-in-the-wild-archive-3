#!/usr/bin/env python3
"""Numerical regression checks for the V4 minimal-representation packet.

This script is not part of the proof. It enumerates the group metric and tests
the proved inequalities on reproducible random samples.
"""

from __future__ import annotations

import math
import random


GROUP = (
    (1.0, 1.0, 1.0),
    (1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (-1.0, -1.0, 1.0),
)


def sqnorm(v):
    return sum(t * t for t in v)


def quotient_sq(u, v):
    return min(sqnorm(tuple(u[i] - g[i] * v[i] for i in range(3))) for g in GROUP)


def canonical(u):
    a = tuple(abs(t) for t in u)
    product = u[0] * u[1] * u[2]
    eps = 1.0 if product >= 0.0 else -1.0
    return a, eps


def formula_sq(u, v):
    a, eps = canonical(u)
    b, delta = canonical(v)
    A = sqnorm(tuple(a[i] - b[i] for i in range(3)))
    if eps == delta:
        return A
    return A + 4.0 * min(a[i] * b[i] for i in range(3))


def image_sq(u, v, t=1.0):
    a, eps = canonical(u)
    b, delta = canonical(v)
    base = sqnorm(tuple(a[i] - b[i] for i in range(3)))
    return base + t * t * (eps * min(a) - delta * min(b)) ** 2


def main():
    rng = random.Random(250604425)
    lower = 2.0 - math.sqrt(2.0)
    upper = 2.0
    seen_min = float("inf")
    seen_max = 0.0

    for _ in range(200_000):
        u = tuple(rng.uniform(-5.0, 5.0) for _ in range(3))
        v = tuple(rng.uniform(-5.0, 5.0) for _ in range(3))
        d2 = quotient_sq(u, v)
        f2 = formula_sq(u, v)
        assert abs(d2 - f2) <= 1e-10 * max(1.0, d2, f2)
        if d2 > 1e-14:
            ratio = image_sq(u, v) / d2
            assert lower - 1e-12 <= ratio <= upper + 1e-12
            seen_min = min(seen_min, ratio)
            seen_max = max(seen_max, ratio)

    L = 1.0 + math.sqrt(2.0)
    a = (1.0, L, L)
    b = (-L, 1.0, L)  # opposite sign parity
    for t in (0.2, 0.5, 1.0, 2.0, 5.0):
        ratio = image_sq(a, b, t=t) / quotient_sq(a, b)
        expected = (1.0 + t * t) / (2.0 + math.sqrt(2.0))
        assert abs(ratio - expected) < 1e-12

    print(f"random samples: 200000")
    print(f"observed squared-ratio range: [{seen_min:.12f}, {seen_max:.12f}]")
    print(f"proved squared-ratio range:   [{lower:.12f}, {upper:.12f}]")
    print("exact metric formula and extremal-family identities: PASS")


if __name__ == "__main__":
    main()
