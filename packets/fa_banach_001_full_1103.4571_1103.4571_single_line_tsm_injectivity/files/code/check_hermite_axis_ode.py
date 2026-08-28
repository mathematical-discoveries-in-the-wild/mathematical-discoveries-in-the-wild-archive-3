#!/usr/bin/env python3
"""Exact checks for the normal-ordered axis ODE in the proof packet.

The proof itself is symbolic and does not depend on this finite check.  This
script verifies the two polynomial identities used in the argument for a
user-selected finite range of Landau levels.
"""

from __future__ import annotations

import argparse

import sympy as sp


def normal_order_polynomial(k: int, s: sp.Symbol) -> sp.Expr:
    """Return P_k(s) from exp(t^2/4-ts) = sum P_k(s)t^k/k!."""
    return sp.expand(
        sp.factorial(k)
        * sum(
            (-s) ** (k - 2 * r)
            / (4**r * sp.factorial(r) * sp.factorial(k - 2 * r))
            for r in range(k // 2 + 1)
        )
    )


def run(max_k: int) -> None:
    s, x, t = sp.symbols("s x t")
    for k in range(max_k + 1):
        pk = normal_order_polynomial(k, s)

        # Coefficient extraction from the generating function.
        generated = sp.expand(
            sp.diff(sp.exp(t**2 / 4 - t * s), t, k).subs(t, 0)
        )
        assert sp.simplify(pk - generated) == 0

        # P_k(s) = 2^{-k} i^k H_k(i s), with physicists' Hermite H_k.
        hermite_form = sp.expand(sp.I**k * sp.hermite(k, sp.I * s) / 2**k)
        assert sp.simplify(pk - hermite_form) == 0

        # Direct normal-order check on a generic polynomial test function.
        test = sum(sp.Symbol(f"a{j}") * x**j for j in range(max_k + 3))
        tk = sum(
            sp.binomial(k, j)
            * (x / 2) ** (k - j)
            * (-1) ** j
            * sp.diff(sp.exp(x**2 / 4) * test, x, j)
            for j in range(k + 1)
        )
        conjugated = sp.exp(x**2 / 4) * pk.subs(s, sp.Derivative(test, x))

        # Substitution of a differential operator is not native in SymPy;
        # evaluate P_k(D) term by term instead.
        pk_poly = sp.Poly(pk, s)
        conjugated = sp.exp(x**2 / 4) * sum(
            coeff * sp.diff(test, x, degree)
            for (degree,), coeff in pk_poly.terms()
        )
        assert sp.simplify(sp.expand(tk - conjugated)) == 0

        roots = sp.nroots(sp.hermite(k, x)) if k else []
        assert all(abs(complex(root).imag) < 1e-12 for root in roots)
        assert len({round(float(sp.re(root)), 10) for root in roots}) == k

        print(f"k={k:2d}  P_k(s)={pk}")

    print(f"verified levels 0 through {max_k}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=10)
    args = parser.parse_args()
    run(args.max_k)
