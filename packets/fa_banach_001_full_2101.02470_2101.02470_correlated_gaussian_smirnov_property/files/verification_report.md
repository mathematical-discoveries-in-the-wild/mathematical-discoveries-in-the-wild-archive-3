# Verification Report

Candidate: arXiv:2101.02470, Remark 2.10

## Claim Checked

Every nondegenerate bivariate Gaussian density has the Smirnov property for every `1 < q < infinity`.

## Verdict

`likely valid`

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Reduction to standard marginals | valid | Separate invertible affine transformations preserve the marginal and joint `L^1`/`L^q` statements. Nondegeneracy becomes `abs(rho)<1`. |
| Conditional-expectation identities | valid | For a standardized Gaussian pair, the conditional kernel is exactly `P_rho`; hence `A=F+P_rho G` and `B=P_rho F+G`. Conditional Jensen puts `A,B` in `L^q`. |
| Cancellation | valid | The Mehler composition law holds also for negative `rho`: `P_rho P_rho=P_{rho^2}`. Thus `B-P_rho A=(I-P_{rho^2})G` is in `L^q`. |
| `L^2` spectral estimate | valid | For `T=P_t-Pi`, `T^m=P_{t^m}-Pi`. On the Hermite basis, constants are removed and the remaining eigenvalues are `t^{mk}`, so the norm is `t^m`. |
| Interpolation and inverse | valid | The full-space endpoint norms of `T^m` are at most 2 on `L^1` and `L^infinity`. Riesz-Thorin makes some power a strict contraction on every finite `L^q`; the factorization of `I-T^m` gives a bounded inverse for `I-T`. |
| Constant component | valid | The right side `(I-P_t)g` has mean zero. The inverse solution also has mean zero, so it solves the desired equation for `I-P_t`, not merely `I-T`. |
| Residual `L^1` fixed point | valid | The residual `d` is mean-zero and satisfies `P_t d=d`, hence `d=P_{t^m}d`. Strong convergence `P_s d -> Pi d` in `L^1` as `s->0` follows by approximation with bounded continuous functions. Therefore `d=0`. |
| Recovery of both summands | valid | Rigidity yields `G in L^q`; then `F=A-P_rho G in L^q` by contraction of `P_rho`. |
| Match to source question | valid | The paper's factor `1/2` is immaterial, and univariate `L^p` with the joint weight equals `L^p` under the corresponding Gaussian marginal. |
| Source condition (2.3) | valid | Direct Gaussian integration reduces finiteness to positivity of a two-by-two quadratic-form matrix. Its smaller eigenvalue is `(1-p*abs(rho))/(1-abs(rho))`, so the exact range is `p*abs(rho)<1`. |

## Adversarial Failure Search

- **Initial functions only in `L^1`:** the proof never expands them in Hermite series. Hermite analysis is used only for the bounded operator norm on `L^2`.
- **Non-invertibility on constants:** constants are split off by `Pi`, and the datum automatically has mean zero.
- **Interpolation-subspace gap:** interpolation is performed on the full operator `T^m=P_{t^m}-Pi`, not on an informally interpolated mean-zero subspace.
- **Negative correlation:** only the squared parameter enters the rigidity step, and the signed Mehler composition is exact.
- **Endpoint leakage:** the theorem is claimed only for finite `1<q<infinity`; no `q=1` or `q=infinity` conclusion is used.
- **Uniqueness overclaim:** the packet computes condition (2.3) exactly and still states uniqueness only under the source theorem's remaining marginal hypotheses.

No counterexample or unresolved logical gap was found.

## Novelty Check

Local indexes contained no result or attempt for the exact arXiv id or Gaussian Smirnov question. Bounded web searches found the source preprint and its 2024 published version, both presenting the question as open, and no later resolution or Ornstein-Uhlenbeck argument. Subscription databases were not searched.

## External Dependencies

No nontrivial external theorem is required beyond standard Riesz-Thorin interpolation and the elementary Hermite diagonalization of the Gaussian noise operator; the latter is derived from the Hermite generating function in the packet.

## Confidence

Score: 96/100.

Reason: the main reduction is an exact two-line conditional-expectation cancellation, and the only delicate upgrade is isolated in a self-contained resolvent lemma with both the `L^q` inverse and the `L^1` kernel handled explicitly.

## Human Review Recommendation

`send to human`
