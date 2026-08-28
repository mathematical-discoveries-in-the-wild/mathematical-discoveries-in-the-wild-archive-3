# Verification Report

## Claim checked

For the height function `K` in Proposition 6.3 of arXiv:2506.15149v2,

```text
K(x1,x2,p) = 1/2 * [
    sqrt((1+p)^2 - (x1+x2)^2)
  + sqrt((1-p)^2 - (x1-x2)^2)
],
```

so `K` is concave on the open real tetrablock and the real hexablock is
convex.

## Verdict

Full solution likely valid.

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Real tetrablock coordinates | valid/source | Source Corollary 2.2 gives the real `beta` representation; solving its two linear equations gives `x1=beta1+p beta2` and `x2=beta2+p beta1`. |
| Domain of `artanh` | valid | `max(|beta1+beta2|,|beta1-beta2|)=|beta1|+|beta2|<1`. |
| Discriminant factorization | valid | Both source radicals reduce exactly to `(1-u^2)(1-v^2)`. |
| Half-angle formulas | valid | Direct substitution into `tanh((U+V)/2)` and `tanh((U-V)/2)` gives the source's `z1,z2`, including the zero-numerator cases by continuity. |
| Height simplification | valid | The four product-to-sum identities and `x1+x2=(1+p)u`, `x1-x2=(1-p)v` give `K=((1+p)sech U+(1-p)sech V)/2`. |
| Radical formula | valid | `sech(artanh t)=sqrt(1-t^2)` for `|t|<1`; the positive root is forced. |
| Facet identification | valid | The four `Li` are four times the barycentric coordinates of the tetrahedron in a permuted order, hence are positive exactly in its interior. |
| Concavity | valid | The displayed square identity proves concavity of the scalar geometric mean without an external Hessian theorem. Affine precomposition and addition preserve concavity. |
| Final implication | valid/source | Source Proposition 6.3 states exactly that concavity of `K` is equivalent to convexity of `H intersect R^4`. |

## Computational check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2506.15149_real_hexablock_convexity/code/verify_closed_form.py \
  --cases 100000
```

With seed `250615149`, the maximum absolute difference between the source
formula and the closed form was `4.163336342344337e-14`.  A separate 100,000
random Jensen-triple check found minimum concavity gap
`K(tx+(1-t)y)-tK(x)-(1-t)K(y)` equal to
`2.1841944823156243e-07`.
The script also verifies the half-angle formulas numerically.

The computation is a regression check only.  The proof is the exact
factorization in `main.tex`.

## Scope audit

- The source's conjecture is stated on PDF page 38 and its Proposition 6.3
  reduces the exact conjecture to concavity of this `K`.
- The proof covers every point of the open real tetrablock, not merely a
  symmetric slice or compact subset.
- Positivity of all radicals follows from the open tetrahedron inequalities.
- No assertion is made about convexity in complex coordinates.
- Bounded local and arXiv/web searches found no earlier proof.  The latest
  later hexablock papers returned by the searches concern operator theory,
  automorphisms, and function theory rather than this real convexity claim.

Confidence: theorem 97/100; novelty 85/100.

Human review recommendation: send to human.
