#!/usr/bin/env python3
"""Exact checks for the forced-singularity multiplicity counterexample.

This script verifies local expansions and symmetry for the n=4, d=7 example,
then brute-forces the invariant monomial support over a finite parameter grid.
It is a consistency check; the packet contains the general proof.
"""

from math import ceil

import sympy as sp


t, x, y, z = sp.symbols("t x y z")
I = sp.I
u = x + I * y
v = x - I * y

H = sp.expand(t * (t**2 - u * v) * (t**2 - 4 * u * v) * (t**2 - 9 * u * v))
G = sp.expand(t * (u * v**5 + u**5 * v))


def lowest_homogeneous_part(expr):
    poly = sp.Poly(sp.expand(expr), t, z)
    terms = poly.terms()
    order = min(sum(exponents) for exponents, _ in terms)
    low = sum(
        coefficient * t ** exponents[0] * z ** exponents[1]
        for exponents, coefficient in terms
        if sum(exponents) == order
    )
    return order, sp.expand(low)


for label, point_y in (("P_plus", I), ("P_minus", -I)):
    local_H = sp.expand(H.subs({x: 1, y: point_y + z}, simultaneous=True))
    local_G = sp.expand(G.subs({x: 1, y: point_y + z}, simultaneous=True))
    order_H, low_H = lowest_homogeneous_part(local_H)
    order_G, low_G = lowest_homogeneous_part(local_G)
    assert order_H == 4
    assert order_G == 2
    print(f"{label}: ord(H)={order_H}, initial(H)={low_H}")
    print(f"{label}: ord(G)={order_G}, initial(G)={low_G}")

# Expanded coefficients are real.
assert all(sp.im(coefficient).simplify() == 0 for coefficient in sp.Poly(G, t, x, y).coeffs())

# A quarter turn and reflection preserve both forms. Substitutions are simultaneous.
quarter_turn = {x: -y, y: x}
reflection = {x: x, y: -y}
for form in (H, G):
    assert sp.expand(form.subs(quarter_turn, simultaneous=True) - form) == 0
    assert sp.expand(form.subs(reflection, simultaneous=True) - form) == 0

checked = 0
for n in range(4, 19):
    for d in range(n, 4 * n):
        r = d % n
        support = [
            (j, k)
            for j in range(d + 1)
            for k in range(d + 1 - j)
            if (j - k) % n == 0
        ]
        order_plus = min(d - k for j, k in support)
        order_minus = min(d - j for j, k in support)
        expected = ceil(r / 2)
        assert order_plus == expected
        assert order_minus == expected
        checked += 1

print(f"support formula verified for {checked} (n,d) pairs")
print("all exact checks passed")
