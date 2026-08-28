"""Finite-coordinate sanity checks for the Theorem 6.3 counterexample.

This script is not part of the proof.  It verifies the defining identities on
finite lists and prints the growth of the first coordinate.
"""

from __future__ import annotations


def project(vector: list[float], n: int) -> list[float]:
    """Apply P_n to a list containing at least n+1 coordinates."""
    output = [0.0] * len(vector)
    for k in range(n):
        output[k] = vector[k]
    output[0] += (n**3) * vector[n]
    return output


def main() -> None:
    last_value = 0.0
    for n in range(1, 251):
        length = n + 8
        vector = [0.0] + [1.0 / ((k + 1) ** 2) for k in range(1, length)]
        projected = project(vector, n)
        projected_twice = project(projected, n)
        assert projected_twice == projected

        in_range = [float(k + 1) if k < n else 0.0 for k in range(length)]
        assert project(in_range, n) == in_range
        assert all(value == 0.0 for value in projected[n:])

        expected = (n**3) / ((n + 1) ** 2)
        assert abs(projected[0] - expected) < 1e-10
        if n >= 4:
            assert projected[0] > last_value
        last_value = projected[0]

    print("passed: n=1..250")
    print(f"first coordinate at n=250: {last_value:.6f}")


if __name__ == "__main__":
    main()

