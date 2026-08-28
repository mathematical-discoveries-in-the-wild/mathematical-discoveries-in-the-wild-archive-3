"""Exact rational sanity checks for the arXiv:1904.00351 counterexample."""

from fractions import Fraction


def check_radius(r0: Fraction) -> None:
    assert r0 > 0
    r = min(r0 / 2, Fraction(1, 2))
    threshold = (1 - r) / (r * r * (1 + r))
    m = threshold + 1

    # B_1=I_2 and the norms of B_2,B_3 are both M.
    coefficient_sum = r + m * r * r + m * r * r * r
    assert 0 < r <= r0
    assert coefficient_sum > 1

    # The second diagonal polynomial q(z)=z+Mz^2-Mz^3 satisfies q(1)=1.
    q_at_one = 1 + m - m
    assert q_at_one == 1


def main() -> None:
    for r0 in (
        Fraction(1, 10_000),
        Fraction(1, 3),
        Fraction(1, 1),
        Fraction(10, 1),
    ):
        check_radius(r0)
    print("all exact rational counterexample checks passed")


if __name__ == "__main__":
    main()
