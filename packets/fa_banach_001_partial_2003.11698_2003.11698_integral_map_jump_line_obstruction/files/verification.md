# Verification report

## Claim checked

The fixed-point integral map associated with a bounded uniformly
positive-definite `BV` matrix coefficient need not carry variable input paths
to variable output paths, even when the source paper's determinant,
curl-free-inverse, and angle hypotheses hold and the smooth driver has two
active coordinates.

## Verdict

**Likely valid.** The argument is exact and reduces to two matrix
multiplications and two one-dimensional singular integrals. No numerical step
is used as proof.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Matrix inverses and positivity | valid | `det(A_+)=1`, `det(A_-)=1/2`; the smallest eigenvalue over both matrices is `1-1/sqrt(2)>0`. |
| `BV` and jump measure | valid | Every nonconstant entry is a two-valued half-space indicator; its distributional derivative is a nonzero constant multiple of Hausdorff measure on the horizontal line. |
| Curl-free inverse | valid | The inverse matrices differ only in their `(2,2)` entry. The first inverse row is constant, while the first component of the second row is constant, so both distributional row curls vanish. |
| Angle condition | valid | Symmetric uniform positive definiteness gives the condition with a positive constant, e.g. the ratio of the uniform lower and upper eigenvalue bounds. |
| Input variability | valid | At `X_t=(0,t^alpha)`, the line-measure Riesz potential is bounded by `C t^{-alpha s}`; its `p`th power is time-integrable exactly when `alpha*s*p<1`. |
| Integral computation | valid | For almost every positive time the coefficient is `A_+`, and `A_+(1,1)=(1,0)`, hence the ordinary Stieltjes integral against `Y_t=(t,t)` is `(t,0)`. |
| Output nonvariability | valid | Every open neighborhood of the output segment contains a line interval around each output point. The integral of `|r-t|^{-1-rho}` over that interval is infinite for every `rho>0`. |
| Match to source target | valid with scope caveat | This disproves a natural invariance principle under strong baseline hypotheses. The source asks only for some unspecified “reasonable assumptions,” so the result is an obstruction/partial result, not a negative full answer. |

## Counterexample stress tests

- Both driver coordinates vary: `Y_t=(t,t)`.
- The input and output start at the same prescribed point `0`.
- The input may be Lipschitz in the basic `p=1` case.
- For every prescribed finite `p`, one can choose `alpha>0` with
  `alpha*s*p<1`; thus the obstruction is not confined to the weakest
  variability class.
- The coefficient is symmetric and uniformly positive definite on both sides
  of the jump, not merely invertible.
- Changing the representative of the coefficient on the jump line does not
  affect the input integral, because the input meets the line only at time
  zero. It also does not affect output nonvariability, which depends on the
  distributional derivative measure.

## External dependencies

- The definition of `(s,p)`-variability and the source fixed-point problem are
  taken from arXiv:2003.11698.
- The half-space `BV` derivative formula and elementary Riesz-potential
  integrals are standard; both are recalculated in the packet.

## Remaining scope

The construction does not rule out fixed-point invariance under explicit
output-transversality assumptions, high-dimensional stochastic occupation
bounds, or regular coefficients whose gradient potentials are locally
bounded. It also does not provide an `(s,infinity)`-variable input, because all
inputs start on the jump line.

## Human-review recommendation

Send for review as a concise partial obstruction. The main reviewer focus
should be whether the source authors intended “integral process” to refer to
the raw Picard map on arbitrary admissible inputs (the interpretation used
here) or only to iterates inside a more restricted, already transversal
candidate set.

