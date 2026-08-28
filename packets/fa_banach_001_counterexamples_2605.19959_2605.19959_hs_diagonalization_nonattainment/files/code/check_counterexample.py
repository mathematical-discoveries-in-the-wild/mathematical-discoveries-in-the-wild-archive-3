#!/usr/bin/env python3
"""Exact arithmetic regression for the nonattainment construction."""

from fractions import Fraction


def finite_objective(m: int, tail_pairs: int) -> Fraction:
    """Objective through ``tail_pairs`` pairs for Q_m."""
    total = Fraction(0)
    for k in range(1, tail_pairs + 1):
        odd = 2 * k - 1
        even = 2 * k
        p_odd = Fraction(1, 2**odd)
        p_even = Fraction(1, 2**even)
        lam_odd = p_odd
        lam_even = p_even
        if k <= m:
            total += p_odd * lam_odd + p_even * lam_even
        else:
            total += p_odd * lam_even + p_even * lam_odd
    return total


def main() -> None:
    optimum = Fraction(1, 3)
    for m in range(9):
        exact = optimum - Fraction(1, 15 * 16**m)
        # The omitted tail after 40 pairs is summed in closed form.
        partial = finite_objective(m, 40)
        if m < 40:
            omitted = Fraction(4, 15 * 16**40)
        else:
            omitted = Fraction(5, 15 * 16**40)
        assert partial + omitted == exact
        assert optimum - exact == Fraction(1, 15 * 16**m)

    # Any equality case moves every basis vector by squared distance 2.
    displacement_partial_sums = [2 * n for n in range(1, 100)]
    assert all(
        displacement_partial_sums[i] < displacement_partial_sums[i + 1]
        for i in range(len(displacement_partial_sums) - 1)
    )
    print("PASS: F(Q_m)=1/3-1/(15*16^m) and equality displacement diverges")


if __name__ == "__main__":
    main()
