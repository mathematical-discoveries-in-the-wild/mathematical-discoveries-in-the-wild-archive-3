#!/usr/bin/env python3
"""Illustrate the character obstruction for a Gaussian L1 approximate identity."""

from decimal import Decimal, getcontext

getcontext().prec = 80


def multiplier(j: int, n: int) -> Decimal:
    """Fourier multiplier of j/sqrt(pi) * exp(-j^2 t^2) at frequency n."""
    exponent = -Decimal(n * n) / Decimal(4 * j * j)
    return exponent.exp()


for j in (1, 2, 4, 8, 16):
    n = 20 * j
    defect = abs(Decimal(1) - multiplier(j, n))
    print(f"j={j:2d}, n={n:3d}, |1-m_j(n)|={defect}")
    assert defect > Decimal(1) - Decimal("1e-40")

print("PASS: every sampled approximate-identity scale has an almost-unit defect.")
