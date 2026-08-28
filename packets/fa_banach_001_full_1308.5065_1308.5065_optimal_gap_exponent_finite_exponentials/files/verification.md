# Verifier report

Verdict: `likely valid candidate full asymptotic answer`

## Claim audit

1. The synthesis Gram matrix is `G_{jk}=2 sin(pi(lambda_j-lambda_k))/(lambda_j-lambda_k)`, with diagonal `2 pi`, and its least eigenvalue is the lower frame/Riesz bound used in the packet.
2. If `W` is the coefficient matrix of the Newton divided differences, then `H=W* G W` and `G^{-1}=W H^{-1} W*`. The final column of `W` is exactly the full barycentric vector.
3. Hermite-Genocchi gives uniform convergence of the `k`th divided difference to `(ix)^k/k!` as the full cluster diameter tends to zero. This convergence depends on the diameter, not on ratios between gaps.
4. Every earlier column of `W` is bounded by `h^(n-k)` times the final column termwise. Hence the inverse Gram matrix, divided by the squared barycentric norm, has a uniform rank-one limit.
5. The bottom-right entry of the inverse limiting monomial Gram matrix is the reciprocal squared distance of `x^n/n!` from lower polynomials. The monic Legendre norm gives

   ```text
   D_n = 2 pi^(2n+1) 4^n / ((2n+1) binom(2n,n)^2).
   ```

6. For `delta`-separated ordered nodes, each barycentric weight is at most `delta^-n/(j!(n-j)!)`. Vandermonde's identity therefore gives the sharp norm bound, with equality at arithmetic spacing.
7. The cluster-exclusion lemma uses blockwise divided differences. If the largest coalescing block has `q<N` nodes, its coefficient matrix has norm `O(delta^-(q-1))`, while the confluent Gram matrix stays uniformly invertible. Therefore the lower frame bound is at least `c delta^(2q-2)`, too large to contribute at scale `delta^(2N-2)`.
8. Saturation of the barycentric norm forces the endpoint product to saturate. Since `(lambda_k-lambda_0)/delta >= k`, every factor tends to `k`, proving asymptotic arithmetic rigidity.
9. The original Montgomery-Vaughan/Turan-Nazarov argument still supplies the explicit all-gap lower estimate. Its `2 pi` normalization and level-set constants were rechecked.

## Computational check

`code/verify_numeric.py` uses 90-digit arithmetic to diagonalize the exact sinc Gram matrix. It checks:

- convergence to the closed-form constant for arithmetic clusters with `N=2,3,4`;
- agreement with the general Legendre-barycentric shape constant for nonarithmetic clusters;
- strict separation between those nonarithmetic constants and the arithmetic extremal constant;
- divergence of the `delta^(-4)` normalization for the hierarchical configuration `(0,delta,sqrt(delta))` when `N=3`.

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_numeric.py
```

The check passed on 27 August 2026. Computation is not used in the proof.

## Novelty check

The bounded search covered the run indexes and web/arXiv queries using the source question plus `finite exponential lower frame bound`, `sinc Gram matrix`, `prolate matrix small bandwidth`, `divided differences`, `clustered nodes`, `Legendre`, and `smallest singular value`.

The search established an important boundary: the exact arithmetic-cluster constant is classical. Batenkov--Demanet--Goldman--Yomdin (arXiv:1809.00658, equation (2.5)) quote Slepian's exact small-bandwidth prolate asymptotic, and its normalization agrees with the constant in this packet. The later clustered-node papers arXiv:1809.00658, arXiv:1907.07119, and arXiv:2107.09326 give sharp cluster-size exponents and geometry-sensitive bounds. No source located in the bounded search states the exact infimum over all real `delta`-separated configurations, proves arithmetic spacing is globally asymptotically worst, or gives the rigidity theorem.

Novelty confidence is therefore moderate: the arithmetic constant and individual tools are known; the unrestricted extremal synthesis appears new within the search bounds.

## Scope

The result fully solves the natural fixed-`N`, `delta -> 0` extremal formulation and retains an explicit bound for every `delta<=1`. It does not determine `m_N(delta)` exactly for fixed nonzero `delta`, optimize the Turan-Nazarov constant, or treat a simultaneous `N -> infinity` regime.

## Recommendation

Promote as a candidate full quantitative answer and send for expert review. The closest scrutiny should go to the uniform error in the one-cluster lemma, the subsequence/positive-definiteness step for multiple clusters, and the literature boundary with classical prolate asymptotics.
