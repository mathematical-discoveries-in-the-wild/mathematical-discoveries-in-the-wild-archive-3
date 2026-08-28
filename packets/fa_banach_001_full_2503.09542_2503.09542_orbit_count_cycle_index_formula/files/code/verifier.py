#!/usr/bin/env python3
"""Verify the Burnside--Möbius formula for orbit counts f_{n,k}.

The left-right action is (mu, nu).sigma = mu sigma nu on S_n.  This
program groups Burnside's sum by the cycle types of mu and nu and computes
the fixed-subset polynomial for each pair of types.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import permutations
from math import comb, factorial, gcd, lcm


def partitions(n: int, maximum: int | None = None):
    """Yield partitions of n as nonincreasing tuples."""
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def centralizer_size(cycle_type: tuple[int, ...]) -> int:
    multiplicities = Counter(cycle_type)
    answer = 1
    for length, multiplicity in multiplicities.items():
        answer *= length**multiplicity * factorial(multiplicity)
    return answer


def permutation_order(cycle_type: tuple[int, ...]) -> int:
    return reduce(lcm, cycle_type, 1)


def power_type(cycle_type: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    result: list[int] = []
    for length in cycle_type:
        splitting = gcd(length, exponent)
        result.extend([length // splitting] * splitting)
    return tuple(sorted(result, reverse=True))


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    answer = 1
    prime = 2
    while prime * prime <= n:
        if n % prime == 0:
            n //= prime
            answer = -answer
            if n % prime == 0:
                return 0
            while n % prime == 0:
                n //= prime
        prime += 1
    if n > 1:
        answer = -answer
    return answer


def action_cycle_counts(
    left_type: tuple[int, ...], right_type: tuple[int, ...]
) -> dict[int, int]:
    """Return {cycle length: number of cycles} for sigma -> mu sigma nu."""
    action_order = lcm(permutation_order(left_type), permutation_order(right_type))
    fixed_by_power: dict[int, int] = {}
    for exponent in divisors(action_order):
        left_power = power_type(left_type, exponent)
        right_power = power_type(right_type, exponent)
        fixed_by_power[exponent] = (
            centralizer_size(left_power) if left_power == right_power else 0
        )

    counts: dict[int, int] = {}
    for length in divisors(action_order):
        numerator = sum(
            mobius(length // exponent) * fixed_by_power[exponent]
            for exponent in divisors(length)
        )
        assert numerator % length == 0
        count = numerator // length
        assert count >= 0
        if count:
            counts[length] = count
    assert sum(length * count for length, count in counts.items()) == factorial(sum(left_type))
    return counts


def fixed_subset_polynomial(
    cycle_counts: dict[int, int], maximum_degree: int
) -> list[int]:
    """Coefficients through maximum_degree of prod_l (1+x^l)^c_l."""
    coefficients = [0] * (maximum_degree + 1)
    coefficients[0] = 1
    for length, count in cycle_counts.items():
        updated = [0] * (maximum_degree + 1)
        for old_degree, old_value in enumerate(coefficients):
            if not old_value:
                continue
            for chosen_cycles in range((maximum_degree - old_degree) // length + 1):
                updated[old_degree + chosen_cycles * length] += (
                    old_value * comb(count, chosen_cycles)
                )
        coefficients = updated
    return coefficients


def representative(cycle_type: tuple[int, ...]) -> tuple[int, ...]:
    """Construct a permutation with the prescribed cycle type."""
    result = list(range(sum(cycle_type)))
    start = 0
    for length in cycle_type:
        cycle = list(range(start, start + length))
        for index, point in enumerate(cycle):
            result[point] = cycle[(index + 1) % length]
        start += length
    return tuple(result)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def direct_action_cycle_counts(
    left: tuple[int, ...], right: tuple[int, ...]
) -> dict[int, int]:
    """Enumerate the cycles of sigma -> left o sigma o right directly."""
    elements = list(permutations(range(len(left))))
    unseen = set(elements)
    counts: Counter[int] = Counter()
    while unseen:
        start = unseen.pop()
        current = compose(compose(left, start), right)
        length = 1
        while current != start:
            unseen.remove(current)
            current = compose(compose(left, current), right)
            length += 1
        counts[length] += 1
    return dict(counts)


def orbit_counts(n: int, maximum_k: int) -> list[int]:
    answer = [Fraction(0) for _ in range(maximum_k + 1)]
    types = list(partitions(n))
    for left_type in types:
        z_left = centralizer_size(left_type)
        for right_type in types:
            z_right = centralizer_size(right_type)
            fixed_polynomial = fixed_subset_polynomial(
                action_cycle_counts(left_type, right_type), maximum_k
            )
            weight = Fraction(1, z_left * z_right)
            for degree, coefficient in enumerate(fixed_polynomial):
                answer[degree] += weight * coefficient
    assert all(value.denominator == 1 for value in answer)
    return [value.numerator for value in answer]


def main() -> None:
    expected = {
        2: [1, 1, 1],
        3: [1, 1, 2, 2, 2, 1, 1],
        4: [1, 1, 4, 10, 41, 103, 309, 691, 1458, 2448, 3703, 4587, 5050],
        5: [1, 1, 6, 37, 715, 13710, 256751, 4140666, 58402198,
            726296995, 8060937770, 80604620206, 732149722382],
    }
    for n, target in expected.items():
        computed = orbit_counts(n, len(target) - 1)
        assert computed == target, (n, computed, target)
        print(f"n={n}: {computed}")
    for n in range(1, 5):
        types = list(partitions(n))
        for left_type in types:
            for right_type in types:
                direct = direct_action_cycle_counts(
                    representative(left_type), representative(right_type)
                )
                inferred = action_cycle_counts(left_type, right_type)
                assert direct == inferred, (n, left_type, right_type, direct, inferred)
        print(f"n={n}: direct action-cycle enumeration agrees for all type pairs")
    print("All published table values through n=5, k=12 agree exactly.")


if __name__ == "__main__":
    main()
