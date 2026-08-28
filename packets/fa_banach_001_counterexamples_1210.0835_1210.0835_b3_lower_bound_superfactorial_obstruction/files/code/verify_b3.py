#!/usr/bin/env python3
"""Exact finite checks for the B_3(2m+1) counterexample packet.

This script is a reproducibility check, not part of the proof.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def enumerate_b3(m: int) -> tuple[Fraction, Fraction, int]:
    """Return signed sum, absolute sum, and admissible-path count."""
    n = 2 * m + 1
    step_count = m + 5
    signed = Fraction(0)
    absolute = Fraction(0)
    admissible_count = 0

    for negative_locations in combinations(range(step_count), 3):
        negative = set(negative_locations)
        r = 0
        denominator = 1
        admissible = True

        for t in range(step_count):
            r += -1 if t in negative else 2
            if t < step_count - 1:
                if r in (0, n):
                    admissible = False
                    break
                denominator *= 4 * r * (n - r)

        if admissible:
            admissible_count += 1
            term = Fraction(1, denominator)
            signed += term
            absolute += abs(term)

    return signed, absolute, admissible_count


def proof_bound(m: int) -> Fraction:
    return Fraction(comb(m + 5, 3), 4 ** (m + 4) * factorial(m) ** 2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=12)
    args = parser.parse_args()
    if args.max_m < 1:
        raise SystemExit("--max-m must be positive")

    print("m\tpaths\tB3(2m+1)\tabs_sum<=proof_bound")
    for m in range(1, args.max_m + 1):
        signed, absolute, count = enumerate_b3(m)
        bound = proof_bound(m)
        assert abs(signed) <= absolute <= bound
        print(f"{m}\t{count}\t{signed}\t{absolute <= bound}")


if __name__ == "__main__":
    main()

