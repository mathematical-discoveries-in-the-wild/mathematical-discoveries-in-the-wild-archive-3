# Verification notes

## Claim audited

For every pair of gauges `rho, sigma` satisfying `sigma >= rho^*`, the
map `lambda` in Lemma 7(iii) of arXiv:2006.16141 is not injective.

## Quantifier audit

The source defines uniform negligibility by

`for every q, eventually in epsilon, for every n in N`.

The spike index may therefore depend on epsilon. For `q=1`, the estimate
fails at `n=K_epsilon` because the array value is 1 and `rho_epsilon -> 0`.
Thus the domain class is nonzero.

Every `sigma`-hypernatural has a representative bounded eventually by
`sigma_epsilon^(-R)` for one fixed `R`. Since

`exp(1/sigma_epsilon) / sigma_epsilon^(-R) -> infinity`,

any fixed pair of hypernatural endpoints eventually lies below the spike.
The target interval sum is then exactly zero, not merely negligible.

## Edge cases

- No monotonicity of either gauge is used.
- The proof works when the two endpoints have different moderateness
  exponents by taking their maximum.
- If the source sum convention allows reversed endpoints, all indices
  between the endpoints still lie below the spike; if it declares such a
  sum empty, it is zero a fortiori.
- The condition `sigma >= rho^*` is required by the source to define
  `lambda`; the kernel construction itself only needs sigma to be a gauge.
- The counterexample is uniformly bounded by 1 and so satisfies domain
  moderateness with exponent zero.

## Verdict

Likely valid, with no conditional lemma or computational dependency. The
counterexample completely settles injectivity negatively on the full stated
domain of `lambda`.

## Human-review focus

Confirm the transcription of the two quotient relations and the convention
that representatives of elements of the hypernatural set are sigma-moderate.
No other delicate step remains.
