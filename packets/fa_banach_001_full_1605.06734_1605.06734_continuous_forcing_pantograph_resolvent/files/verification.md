# Verification Report

Candidate: arXiv:1605.06734 Section 4, general smooth forcing for the
first-order inhomogeneous pantograph equation

## Claim checked

For a Banach space `X`, `0<alpha<1`, `B in L(X)`, continuous `q:R->X`, and
`a in X`, the unique global `C^1` solution of

`y'(x)=B y(alpha x)+q(x), y(0)=a`

is the compact-uniformly convergent series displayed as equation (4) in the
packet.

## Verdict

`likely valid`

Confidence: 96/100 for mathematical correctness.  Novelty confidence is only
moderate because the Volterra argument is elementary and an older equivalent
formula may exist.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Iterated scaled-Volterra kernel | valid | Direct induction yields the coefficient `alpha^(n(n-1)/2)/(n-1)!`. |
| Compact operator-series convergence | valid | The factorial bound proves norm convergence without a smallness condition. |
| Forcing kernel | valid | Substituting the primitive and applying Fubini gives the extra factor `alpha^n/n`. |
| Existence and regularity | valid | The series first solves the integral equation; the Banach-valued fundamental theorem then gives `C^1` regularity. |
| Uniqueness | valid | Iteration of the homogeneous integral equation forces the compact sup norm to zero. |
| Negative half-line | valid | Oriented integrals satisfy the same formula; equivalently transform `x` to `-x`. |
| Source consistency | valid | Expanding analytic `q` recovers source equation (44) coefficient by coefficient. |

## Counterexample and computation search

No counterexample was found.  The included checker passed 961 exact exponent
identities, 25 exact scalar coefficients, 38 exact rational-matrix coefficient
components, and 41 high-precision residual points on `[-2,2]`.  The maximum
truncated residual was `2.3336307e-61`.

## Gaps

No mathematical gap identified.  The open review item is bibliographic:
determine whether the explicit resolvent appeared earlier in pantograph or
general Volterra-equation literature.

## Human review recommendation

`send to human`

Focus first on the oriented-integral identity for negative `x`, then on prior
art for the explicit series.
