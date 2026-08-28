#!/usr/bin/env python3
"""Numerically check the soft-threshold counterexample in the packet.

This is only a sanity check.  The proof in main.tex is analytic.
"""

from __future__ import annotations

import numpy as np
from scipy.special import zeta


BETA = 1.0
ETA = 0.75
C_ALPHA = 10.0
MAX_N = 250_000


def tail(m: np.ndarray) -> np.ndarray:
    """Exact l2 tail of x_k = k^{-ETA}, via the Hurwitz zeta function."""
    return np.sqrt(zeta(2.0 * ETA, m + 1.0))


def check(delta: float) -> tuple[int, float, float, float]:
    m = np.arange(1, MAX_N + 1, dtype=float)
    sigma = m ** (-BETA)
    objective = delta / sigma + tail(m)
    index = int(np.argmin(objective))
    if index in (0, MAX_N - 1):
        raise RuntimeError("search interval did not bracket the minimizing index")

    n = index + 1
    phi = float(objective[index])
    alpha = C_ALPHA * delta**2 / (np.sqrt(n) * phi)

    k = n + 1
    sigma_k = k ** (-BETA)
    exact_k = k ** (-ETA)
    threshold_ratio = alpha / (delta * sigma_k)
    recovered_k = max(exact_k + delta / sigma_k - alpha / sigma_k**2, 0.0)

    assert threshold_ratio < 1.0
    assert recovered_k > 0.0
    return n, phi, threshold_ratio, recovered_k


def main() -> None:
    print("beta=1, eta=3/4, c_alpha=10")
    print("delta        n(delta)    alpha/(delta*sigma[n+1])    recovered[n+1]")
    for delta in (1e-4, 3e-5, 1e-5, 3e-6, 1e-6):
        n, _, ratio, recovered = check(delta)
        print(f"{delta:8.1e}  {n:9d}    {ratio:24.8f}    {recovered:.8e}")


if __name__ == "__main__":
    main()
