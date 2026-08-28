#!/usr/bin/env python3
"""Bounded sanity checks for the base-4 digit-cost counterexample.

The finite computation is not part of the proof. It checks the two exact
identities on which the packet's closed-form argument is based.
"""


def digit_cost(r: int) -> int:
    """Read the base-4 digits of r as coefficients of powers of 2."""
    if r < 0:
        raise ValueError("r must be nonnegative")
    total = 0
    place = 1
    while r:
        r, digit = divmod(r, 4)
        total += digit * place
        place *= 2
    return total


def phi(r: int) -> int:
    return r + digit_cost(r)


def main() -> None:
    limit = 1000
    costs = [digit_cost(r) for r in range(2 * limit + 1)]
    checked = 0
    for r in range(limit + 1):
        for s in range(limit + 1):
            assert costs[r + s] <= costs[r] + costs[s], (r, s)
            checked += 1

    for j in range(1, 13):
        assert digit_cost(4**j - 1) == 3 * (2**j - 1)
        assert digit_cost(4**j) == 2**j
        assert phi(4**j - 1) - phi(4**j) == 2 ** (j + 1) - 4

    print(f"verified subadditivity on {checked:,} pairs")
    print("verified exact jump formulas for 1 <= j <= 12")


if __name__ == "__main__":
    main()
