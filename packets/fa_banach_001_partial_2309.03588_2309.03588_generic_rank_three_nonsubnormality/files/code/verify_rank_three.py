#!/usr/bin/env python3
"""Numerically reconstruct the rank-three rational model and forbidden atoms.

This is a sanity checker for the perturbative/generic proof.  It implements
the Costara--Chavan--Ghara--Reza formulas directly from the support points and
weights.  Floating-point checks are not used as proof.
"""

from __future__ import annotations

import itertools
import numpy as np
from numpy.polynomial import polynomial as poly


def polyval(coeff: np.ndarray, z: complex) -> complex:
    return poly.polyval(z, coeff)


def derivative(coeff: np.ndarray) -> np.ndarray:
    return poly.polyder(coeff)


def divide_linear(coeff: np.ndarray, root: complex) -> np.ndarray:
    quotient, remainder = poly.polydiv(coeff, np.array([-root, 1.0]))
    assert np.max(np.abs(remainder)) < 2e-7
    return np.trim_zeros(quotient, trim="b")


def star(coeff: np.ndarray) -> np.ndarray:
    return np.conjugate(coeff[::-1])


def spectral_factor(
    zetas: np.ndarray, weights: np.ndarray
) -> tuple[np.ndarray, float, np.ndarray]:
    n = len(zetas)
    support_poly = poly.polyfromroots(zetas)
    self_inversive = poly.polymul(support_poly, star(support_poly))
    for j in range(n):
        reduced = divide_linear(support_poly, zetas[j])
        term = poly.polymul(reduced, star(reduced))
        term = np.pad(term, (1, 0))  # multiply by z
        self_inversive[: len(term)] += weights[j] * term

    roots = poly.polyroots(self_inversive)
    outer = roots[np.abs(roots) > 1.0 + 1e-8]
    assert len(outer) == n, (roots, outer)
    q = poly.polyfromroots(outer)

    probe = np.exp(0.371j)
    lhs = abs(polyval(support_poly, probe)) ** 2
    for j in range(n):
        reduced = divide_linear(support_poly, zetas[j])
        lhs += weights[j] * abs(polyval(reduced, probe)) ** 2
    gamma = float(np.real_if_close(lhs / abs(polyval(q, probe)) ** 2))
    assert gamma > 0
    return q, gamma, support_poly


def gram_polynomial(
    zetas: np.ndarray, weights: np.ndarray
) -> tuple[np.ndarray, np.ndarray, float]:
    n = len(zetas)
    q, gamma, support_poly = spectral_factor(zetas, weights)
    ratio = support_poly[0] / q[0]
    phase = np.conjugate(ratio) / abs(ratio)
    p = phase * support_poly / np.sqrt(gamma)

    reduced = [divide_linear(support_poly, zeta) for zeta in zetas]
    support_deriv = derivative(support_poly)
    fnum = [
        polyval(q, zetas[j]) / polyval(support_deriv, zetas[j]) * reduced[j]
        for j in range(n)
    ]
    op_deriv = np.array(
        [phase / np.sqrt(gamma) * polyval(support_deriv, zetas[j]) / polyval(q, zetas[j])
         for j in range(n)]
    )

    gram = np.empty((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            if i == j:
                num = fnum[i]
                value = (
                    polyval(derivative(num), zetas[i]) * polyval(q, zetas[i])
                    - polyval(num, zetas[i]) * polyval(derivative(q), zetas[i])
                ) / polyval(q, zetas[i]) ** 2
                gram[i, i] = weights[i] * zetas[i] * value
            else:
                gram[i, j] = 1.0 / (
                    op_deriv[i]
                    * np.conjugate(op_deriv[j])
                    * (1.0 - zetas[i] * np.conjugate(zetas[j]))
                )
    assert np.max(abs(gram - np.conjugate(gram.T))) < 2e-6
    gram = (gram + np.conjugate(gram.T)) / 2
    assert np.min(np.linalg.eigvalsh(gram)) > 1e-9
    inverse = np.linalg.inv(gram)

    finite = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            finite += np.conjugate(inverse[j, i]) * np.outer(fnum[j], np.conjugate(fnum[i]))

    result = np.outer(q, np.conjugate(q)) - np.outer(p, np.conjugate(p))
    result[:n, :n] -= finite
    result[1 : n + 1, 1 : n + 1] += finite
    assert np.max(abs(result[0, :])) < 3e-6
    assert np.max(abs(result[:, 0])) < 3e-6
    return result, q, gamma


def evaluate_bivariate(coeff: np.ndarray, z: complex, y: complex) -> complex:
    powers_z = z ** np.arange(coeff.shape[0])
    powers_y = y ** np.arange(coeff.shape[1])
    return powers_z @ coeff @ powers_y


def inspect(angles: tuple[float, float, float], weights: tuple[float, float, float]) -> None:
    zetas = np.exp(1j * np.array(angles))
    coeff, q, gamma = gram_polynomial(zetas, np.array(weights))
    roots = poly.polyroots(q)
    qprime = derivative(q)
    products = []
    residues = []
    cross_values = []
    for r, t in itertools.product(range(3), repeat=2):
        x = roots[r] * np.conjugate(roots[t])
        g = evaluate_bivariate(coeff, roots[r], np.conjugate(roots[t]))
        residue = g / (
            roots[r] ** 2
            * np.conjugate(roots[t]) ** 2
            * polyval(qprime, roots[r])
            * np.conjugate(polyval(qprime, roots[t]))
        )
        products.append(x)
        residues.append(residue)
        if r != t:
            cross_values.append(g)
    separation = min(
        abs(products[i] - products[j])
        for i in range(9)
        for j in range(i)
    )
    print("angles", angles, "weights", weights)
    print("gamma", gamma)
    print("outer roots", roots)
    print("minimum pole-product separation", separation)
    print("minimum |cross G|", min(abs(v) for v in cross_values))
    print("minimum |off-diagonal residue|", min(
        abs(residues[3*r+t]) for r in range(3) for t in range(3) if r != t
    ))


if __name__ == "__main__":
    inspect((0.0, 2 * np.pi / 3, 4 * np.pi / 3), (1.0, 1.0, 1.0))
    inspect((0.0, 2.03, 4.31), (0.91, 1.08, 1.17))
    inspect((0.0, 1.0, 2.7), (0.0001, 0.0004, 0.0009))
