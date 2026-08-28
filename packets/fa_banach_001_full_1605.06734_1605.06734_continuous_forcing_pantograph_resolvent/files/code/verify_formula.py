#!/usr/bin/env python3
"""Exact and numerical checks for the continuous-forcing pantograph formula.

The exact checks are not a proof; they guard against exponent/index mistakes in
the displayed formula.  The proof is contained in the packet.
"""

from fractions import Fraction
from math import factorial

import mpmath as mp


def mat_vec(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a)))


def vec_add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def vec_scale(c, v):
    return tuple(c * x for x in v)


def exact_scalar_coefficient_check(max_degree=24):
    alpha = Fraction(2, 3)
    beta = Fraction(-5, 4)
    initial = Fraction(7, 5)
    q = [Fraction((-1) ** k * (k + 2), k + 3) for k in range(9)]

    recurrence = [initial]
    for m in range(max_degree):
        q_m = q[m] if m < len(q) else Fraction(0)
        recurrence.append((beta * alpha**m * recurrence[m] + q_m) / (m + 1))

    formula = []
    for m in range(max_degree + 1):
        value = initial * alpha ** (m * (m - 1) // 2) * beta**m / factorial(m)
        for k in range(min(m, len(q))):
            n = m - k - 1
            value += (
                beta**n
                * alpha ** (n * (n + 1) // 2 + n * k)
                * q[k]
                * factorial(k)
                / factorial(m)
            )
        formula.append(value)

    assert formula == recurrence
    return len(formula)


def exact_matrix_coefficient_check(max_degree=18):
    alpha = Fraction(3, 5)
    b = (
        (Fraction(1, 3), Fraction(-2, 5)),
        (Fraction(4, 7), Fraction(1, 6)),
    )
    initial = (Fraction(2, 3), Fraction(-5, 8))
    q = [
        (Fraction(k + 1, k + 2), Fraction((-1) ** k, k + 3))
        for k in range(7)
    ]

    recurrence = [initial]
    for m in range(max_degree):
        q_m = q[m] if m < len(q) else (Fraction(0), Fraction(0))
        next_value = vec_scale(
            Fraction(1, m + 1),
            vec_add(vec_scale(alpha**m, mat_vec(b, recurrence[m])), q_m),
        )
        recurrence.append(next_value)

    formula = []
    for m in range(max_degree + 1):
        b_power_initial = initial
        for _ in range(m):
            b_power_initial = mat_vec(b, b_power_initial)
        value = vec_scale(
            alpha ** (m * (m - 1) // 2) / factorial(m), b_power_initial
        )
        for k in range(min(m, len(q))):
            n = m - k - 1
            b_power_q = q[k]
            for _ in range(n):
                b_power_q = mat_vec(b, b_power_q)
            scale = (
                alpha ** (n * (n + 1) // 2 + n * k)
                * factorial(k)
                / factorial(m)
            )
            value = vec_add(value, vec_scale(scale, b_power_q))
        formula.append(value)

    assert formula == recurrence
    return 2 * len(formula)


def exponent_identity_check(max_index=30):
    checks = 0
    for n in range(max_index + 1):
        for k in range(max_index + 1):
            m = n + k + 1
            left = n * (n + 1) // 2 + n * k
            right = m * (m - 1) // 2 - k * (k + 1) // 2
            assert left == right
            checks += 1
    return checks


def numerical_residual_check(truncation=18):
    mp.mp.dps = 60
    alpha = mp.mpf("0.43")
    beta = mp.mpf("-1.1")
    initial = mp.mpf("0.7")

    def q(x):
        return mp.sin(mp.mpf("1.3") * x) + mp.mpf("0.25") * x**2

    def oriented_integral(fun, x):
        if x == 0:
            return mp.mpf("0")
        return mp.quad(fun, [0, x])

    def y(x):
        homogeneous = mp.fsum(
            initial
            * alpha ** (n * (n - 1) // 2)
            * beta**n
            * x**n
            / mp.factorial(n)
            for n in range(truncation + 1)
        )
        forced = mp.fsum(
            beta**n
            * alpha ** (n * (n + 1) // 2)
            / mp.factorial(n)
            * oriented_integral(lambda t: (x - t) ** n * q(alpha**n * t), x)
            for n in range(truncation + 1)
        )
        return homogeneous + forced

    def y_prime(x):
        homogeneous = mp.fsum(
            initial
            * alpha ** (n * (n - 1) // 2)
            * beta**n
            * x ** (n - 1)
            / mp.factorial(n - 1)
            for n in range(1, truncation + 1)
        )
        forced = q(x) + mp.fsum(
            beta**n
            * alpha ** (n * (n + 1) // 2)
            / mp.factorial(n - 1)
            * oriented_integral(
                lambda t: (x - t) ** (n - 1) * q(alpha**n * t), x
            )
            for n in range(1, truncation + 1)
        )
        return homogeneous + forced

    points = [mp.mpf(-2) + mp.mpf(4) * j / 40 for j in range(41)]
    residuals = [abs(y_prime(x) - beta * y(alpha * x) - q(x)) for x in points]
    initial_error = abs(y(mp.mpf("0")) - initial)
    max_residual = max(residuals)
    assert initial_error < mp.mpf("1e-50")
    assert max_residual < mp.mpf("1e-35")
    return len(points), max_residual, initial_error


def main():
    exponent_checks = exponent_identity_check()
    scalar_checks = exact_scalar_coefficient_check()
    matrix_checks = exact_matrix_coefficient_check()
    points, residual, initial_error = numerical_residual_check()
    print(f"exponent identities: {exponent_checks} passed")
    print(f"exact scalar coefficients: {scalar_checks} passed")
    print(f"exact 2x2 matrix coefficient components: {matrix_checks} passed")
    print(f"numerical residual points: {points} passed")
    print(f"maximum truncated residual: {mp.nstr(residual, 8)}")
    print(f"initial-value error: {mp.nstr(initial_error, 8)}")


if __name__ == "__main__":
    main()
