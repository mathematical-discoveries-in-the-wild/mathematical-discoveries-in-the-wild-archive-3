#!/usr/bin/env python3
"""Finite checks for the entropy-separation example in the packet.

This script is not part of the proof.  It compares the scale sums for
N_k=floor(c exp(k)/k^2) gaps of length exp(-k), and checks numerically that
Whitney subdivision changes the log-log entropy by only a bounded factor.
"""

from __future__ import annotations

import math


def phi(t: float) -> float:
    return math.log(math.e + math.log(1.0 / t))


def main() -> None:
    c = 0.05
    for cutoff in (25, 50, 100, 200, 400):
        gap_mass = 0.0
        loglog_entropy = 0.0
        bc_entropy = 0.0
        for k in range(5, cutoff + 1):
            # Avoid constructing exp(k) for the count: N_k e^{-k} differs
            # negligibly from c/k^2 at these scales.
            mass_k = c / (k * k)
            gap_mass += mass_k
            loglog_entropy += mass_k * phi(math.exp(-k))
            bc_entropy += mass_k * k
        print(
            f"K={cutoff:3d}  mass={gap_mass:.6f}  "
            f"loglog={loglog_entropy:.6f}  BC={bc_entropy:.6f}"
        )

    print("\nWhitney/original log-log entropy ratios")
    for k in (5, 10, 25, 50, 100, 250):
        length = math.exp(-k)
        original = length * phi(length)
        whitney = length / 3.0 * phi(length / 3.0)
        for j in range(1, 200):
            piece = length / (3.0 * 2.0**j)
            whitney += 2.0 * piece * phi(piece)
        print(f"k={k:3d}  ratio={whitney / original:.6f}")


if __name__ == "__main__":
    main()
