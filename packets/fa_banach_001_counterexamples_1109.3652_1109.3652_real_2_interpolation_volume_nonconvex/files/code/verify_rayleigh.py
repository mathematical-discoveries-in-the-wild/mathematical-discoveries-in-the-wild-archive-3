"""Exact symbolic audit of the two-dimensional Rayleigh deficit."""

import sympy as sp


theta, eps = sp.symbols("theta eps", real=True)
h = 1 + eps * sp.cos(4 * theta)
curvature_radius = h + sp.diff(h, theta, 2)
a = sp.cos(2 * theta)

period = (theta, 0, 2 * sp.pi)
cone_mass = sp.integrate(h * curvature_radius, period)
mean_numerator = sp.integrate(a * h * curvature_radius, period)
tangential_energy = sp.integrate(h**2 * sp.diff(a, theta) ** 2, period)
angular_second_moment = sp.integrate(a**2 * h * curvature_radius, period)
deficit = sp.factor(tangential_energy - 4 * angular_second_moment)

expected = {
    "cone_mass": sp.pi * (2 - 15 * eps**2),
    "mean_numerator": 0,
    "tangential_energy": sp.pi * (4 - 4 * eps + 2 * eps**2),
    "angular_second_moment": sp.pi * (1 - 7 * eps - sp.Rational(15, 2) * eps**2),
    "deficit": 8 * sp.pi * eps * (3 + 4 * eps),
}

actual = {
    "cone_mass": sp.factor(cone_mass),
    "mean_numerator": sp.factor(mean_numerator),
    "tangential_energy": sp.factor(tangential_energy),
    "angular_second_moment": sp.factor(angular_second_moment),
    "deficit": deficit,
}

for key in expected:
    assert sp.simplify(actual[key] - expected[key]) == 0, key
    print(f"{key}: {actual[key]}")

sample = sp.Rational(-1, 100)
assert sp.simplify(curvature_radius.subs(eps, sample) - (1 + sp.Rational(3, 20) * sp.cos(4 * theta))) == 0
assert expected["deficit"].subs(eps, sample) < 0
print(f"epsilon: {sample}")
print(f"exact_deficit: {sp.factor(expected['deficit'].subs(eps, sample))}")
