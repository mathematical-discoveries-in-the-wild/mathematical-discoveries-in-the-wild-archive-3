#!/usr/bin/env python3
"""Guard checks for the atomic Poisson-trace proof.

The script does not replace the proof.  It checks the centered-polar
Jacobian, the sharp scalar kernel used in the anchored Hardy estimate, and
the scale-uniform marginal lower bound on representative dyadic boxes.
"""

from __future__ import annotations

import math
import random

import mpmath as mp


mp.mp.dps = 60


def poisson(z: list[float], eta: list[float], dimension_real: int) -> mp.mpf:
    norm_z2 = mp.fsum(x * x for x in z)
    distance2 = mp.fsum((x - y) ** 2 for x, y in zip(z, eta))
    return (1 - norm_z2) / distance2 ** (mp.mpf(dimension_real) / 2)


def check_centered_polar_identity() -> int:
    rng = random.Random(200109616)
    checked = 0
    for dimension_real in (4, 6, 8, 12):
        eta = [mp.mpf(1)] + [mp.mpf(0)] * (dimension_real - 1)
        for _ in range(200):
            raw = [mp.mpf(rng.gauss(0, 1)) for _ in range(dimension_real)]
            length = mp.sqrt(mp.fsum(x * x for x in raw))
            omega = [x / length for x in raw]
            if omega[0] < 0:
                omega = [-x for x in omega]
            a = omega[0]
            rho = 2 * a * mp.mpf(rng.uniform(0.001, 0.999))
            z = [eta[j] - rho * omega[j] for j in range(dimension_real)]
            lhs = poisson(z, eta, dimension_real) * rho ** (dimension_real - 1)
            rhs = 2 * a - rho
            if not mp.almosteq(lhs, rhs, rel_eps=mp.mpf("1e-48")):
                raise AssertionError((dimension_real, lhs, rhs))
            checked += 1
    return checked


def hardy_ratio(t: mp.mpf) -> mp.mpf:
    """A(s)/(L^2(L-s)) after scaling t=s/L."""
    if t == 1:
        return mp.mpf(0)
    numerator = mp.mpf(1) / 6 - t * t / 2 + t**3 / 3
    return numerator / (1 - t)


def check_hardy_kernel() -> tuple[int, mp.mpf]:
    values = []
    for k in range(10001):
        t = mp.mpf(k) / 10000
        values.append(hardy_ratio(t))
    maximum = max(values)
    exact_maximum = mp.mpf(3) / 16
    if abs(maximum - exact_maximum) > mp.mpf("1e-8"):
        raise AssertionError((maximum, exact_maximum))
    if not mp.almosteq(hardy_ratio(mp.mpf(1) / 4), exact_maximum):
        raise AssertionError("maximum is not attained at t=1/4")
    return len(values), maximum


def marginal_weight(d: int, lam: complex) -> mp.mpf:
    x = mp.mpc(lam)
    area = 1 - abs(x) ** 2
    distance = abs(1 - x) ** 2
    if area <= 0:
        return mp.mpf(0)

    def integrand(u: mp.mpf) -> mp.mpf:
        return (area - u) * u ** (d - 2) / (distance + u) ** d

    return mp.quad(integrand, [0, area])


def check_marginal_boxes() -> tuple[int, dict[int, float]]:
    checked = 0
    minima: dict[int, float] = {}
    for d in range(2, 9):
        minimum = mp.inf
        for n in range(3, 12):
            delta = mp.mpf(2) ** (-n)
            for radial_factor in (mp.mpf("0.55"), mp.mpf("0.75"), mp.mpf("0.95")):
                for angular_factor in (mp.mpf("-0.16"), mp.mpf(0), mp.mpf("0.16")):
                    lam = complex(
                        float(1 - radial_factor * delta),
                        float(angular_factor * delta),
                    )
                    scaled = delta * marginal_weight(d, lam)
                    minimum = min(minimum, scaled)
                    checked += 1
        if not (minimum > 0):
            raise AssertionError((d, minimum))
        minima[d] = float(minimum)
    return checked, minima


def main() -> None:
    polar_checks = check_centered_polar_identity()
    hardy_checks, hardy_maximum = check_hardy_kernel()
    marginal_checks, minima = check_marginal_boxes()
    print("PASS")
    print(f"centered-polar identities: {polar_checks}")
    print(f"Hardy-kernel samples: {hardy_checks}")
    print(f"Hardy-kernel maximum: {mp.nstr(hardy_maximum, 20)} (exact 3/16)")
    print(f"dyadic marginal samples: {marginal_checks}")
    for d, value in minima.items():
        print(f"  d={d}: min(delta * W_d)={value:.12g}")


if __name__ == "__main__":
    main()
