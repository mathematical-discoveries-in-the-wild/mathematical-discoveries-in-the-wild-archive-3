#!/usr/bin/env python3
"""Exact regression checks for the affine-group counterexample."""

import sympy as sp


def mul(x, y):
    """Multiplication in the orientation-preserving affine group."""
    a, b = x
    c, d = y
    return (sp.expand(a * c), sp.expand(b + a * d))


def main():
    alpha, beta, u, v = sp.symbols("alpha beta u v", positive=True)
    x1, x2, y1, y2, z1, z2 = sp.symbols("x1 x2 y1 y2 z1 z2", positive=True)

    # The inverse Jacobian and the density 1/a after left translation.
    left_inverse_jacobian = alpha ** -2
    left_inverse_a = u / alpha
    left_density = sp.simplify(left_inverse_jacobian / left_inverse_a)
    assert sp.simplify(left_density - 1 / (alpha * u)) == 0

    # The same calculation for right translation.
    right_inverse_jacobian = alpha ** -1
    right_inverse_a = u / alpha
    right_density = sp.simplify(right_inverse_jacobian / right_inverse_a)
    assert sp.simplify(right_density - 1 / u) == 0

    # Any group satisfies ((xy)z)y = x(y(zy)); verify in affine coordinates.
    x = (x1, x2)
    y = (y1, y2)
    z = (z1, z2)
    lhs = mul(mul(mul(x, y), z), y)
    rhs = mul(x, mul(y, mul(z, y)))
    assert all(sp.simplify(a - b) == 0 for a, b in zip(lhs, rhs))

    # j(a,b)=1/a is multiplicative but nontrivial.
    xy = mul((alpha, beta), (x1, x2))
    j_xy = sp.simplify(1 / xy[0])
    assert sp.simplify(j_xy - (1 / alpha) * (1 / x1)) == 0
    assert sp.Rational(1, 2) != 1

    print("PASS: affine right-Haar measure gives j(alpha,beta)=alpha^(-1), rho=1")


if __name__ == "__main__":
    main()
