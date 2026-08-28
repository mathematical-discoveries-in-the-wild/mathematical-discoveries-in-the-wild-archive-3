#!/usr/bin/env python3
"""Sanity checks for the constant-spectrum projection counterexample in R^3."""

from __future__ import annotations

import math

from scipy.integrate import quad


A = 1.0 - math.tanh(1.0)
C = 1.0 / math.cosh(1.0)


def h(r: float) -> float:
    if r == 0.0:
        return C
    if r <= 1.0:
        return C * math.sinh(r) / r
    return 1.0 - A / r


def h_prime(r: float) -> float:
    if r <= 1.0:
        if r == 0.0:
            return 0.0
        return C * (r * math.cosh(r) - math.sinh(r)) / (r * r)
    return A / (r * r)


def smooth_cutoff_derivatives(r: float, radius: float) -> tuple[float, float]:
    """Return eta_R'(r), eta_R''(r) for a C^2 quintic cutoff."""
    if r <= radius or r >= 2.0 * radius:
        return 0.0, 0.0
    s = (r - radius) / radius
    first_s = -30.0 * s * s * (1.0 - s) * (1.0 - s)
    second_s = -60.0 * s + 180.0 * s * s - 120.0 * s * s * s
    return first_s / radius, second_s / (radius * radius)


def residual(r: float, radius: float) -> float:
    eta_prime, eta_second = smooth_cutoff_derivatives(r, radius)
    return -h(r) * (eta_second + 2.0 * eta_prime / r) - 2.0 * eta_prime * h_prime(r)


def radial_l2_squared(function, start: float, stop: float) -> float:
    integral, _ = quad(
        lambda r: 4.0 * math.pi * function(r) ** 2 * r * r,
        start,
        stop,
        epsabs=1e-12,
        epsrel=1e-12,
        limit=400,
    )
    return integral


def main() -> None:
    print("projection-valued potential checks")
    for value in (0.0, 1.0):
        diagonal = (1.0 - value, value)
        idempotence_error = max(abs(entry * entry - entry) for entry in diagonal)
        eigenvalues = tuple(sorted(diagonal))
        print(
            f"v={value:.0f}: spectrum={eigenvalues}, trace={sum(diagonal):.1f}, "
            f"op_norm={max(diagonal):.1f}, ||W^2-W||={idempotence_error:.1e}"
        )

    matching_value_error = abs(C * math.sinh(1.0) - (1.0 - A))
    matching_derivative_error = abs(C * (math.cosh(1.0) - math.sinh(1.0)) - A)
    potential_norm = math.sqrt(radial_l2_squared(h, 0.0, 1.0))

    print(f"value matching error      {matching_value_error:.3e}")
    print(f"derivative matching error {matching_derivative_error:.3e}")
    print(f"||1_B h||_2              {potential_norm:.10f}")
    print("R       ||H(eta_R h)||_2       sqrt(R)*residual       obstruction ratio")
    for radius in (8.0, 32.0, 128.0, 512.0, 2048.0, 8192.0):
        residual_norm = math.sqrt(
            radial_l2_squared(lambda r: residual(r, radius), radius, 2.0 * radius)
        )
        print(
            f"{radius:5.0f}   {residual_norm:18.10e}   "
            f"{math.sqrt(radius) * residual_norm:18.10e}   "
            f"{potential_norm / residual_norm:18.10e}"
        )


if __name__ == "__main__":
    main()
