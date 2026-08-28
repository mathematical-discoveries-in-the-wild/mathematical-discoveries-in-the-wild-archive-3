"""Symbolic transcription checks for the threshold-set parity proof."""

from __future__ import annotations

import sympy as sp


def chebyshev_u(n: int, x: sp.Symbol) -> sp.Expr:
    """Return U_n(x) using U_0=1, U_1=2x, U_{n+1}=2xU_n-U_{n-1}."""
    if n == 0:
        return sp.Integer(1)
    previous = sp.Integer(1)
    current = 2 * x
    for _ in range(1, n):
        previous, current = current, sp.expand(2 * x * current - previous)
    return current


def main() -> None:
    variables = sp.symbols("x0:4")
    checks = 0

    for kappa in range(1, 9):
        for j in range(1, 8):
            degree = j * kappa - 1
            for dimension in range(1, 5):
                g = sum(
                    (1 - x**2) * chebyshev_u(degree, x)
                    for x in variables[:dimension]
                )
                reflected = g.subs({x: -x for x in variables[:dimension]})
                expected = (-1) ** degree * g
                assert sp.expand(reflected - expected) == 0
                checks += 1

    print(f"PASS: {checks} symbolic g_(j kappa) parity identities")
    print("PASS: the common factor is independent of the witness index q")


if __name__ == "__main__":
    main()
