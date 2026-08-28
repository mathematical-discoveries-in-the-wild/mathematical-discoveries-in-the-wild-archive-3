# Verification report

Candidate: generic rank-three Cauchy-dual non-subnormality for
arXiv:2309.03588, Problem 1.

## Claim checked

In each ordered angle-mass chart for three distinct support points, the
subnormal locus is contained in a union of two proper real-analytic zero sets,
hence is Lebesgue-null and nowhere dense. In addition, every equal-mass
equilateral measure has a full neighborhood consisting entirely of
non-subnormal models.

## Verdict

`likely valid`; candidate substantial partial result. Specialist review is
recommended before treating it as verified.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Rational finite-support model | valid/external | Theorem 6.1 of arXiv:2103.10059 supplies the monic outer factor and intrinsic Gram numerator. |
| Forbidden complex measure | valid/external | Corollary 4.1 and Remark 4.2 of arXiv:2103.10059 explicitly require grouped coefficients outside `[0,1]` to vanish. |
| Complete-monotonicity matrices | valid/external | Theorem 2.1 of arXiv:2103.10059 gives the formally positive matrices for every order `ell`; Corollary 2.3 gives sufficiency of cross-Gram vanishing. |
| New simple-root iff criterion | likely valid | Leading-block Vandermonde congruence isolates `c_rt(1-u_r conjugate(u_t))^ell`. The strict identity `|1-u_r conjugate(u_t)|^2-(1-|u_r|^2)(1-|u_t|^2)=|u_r-u_t|^2` makes a nonzero cross term violate a 2x2 principal minor for large `ell`. No product-distinctness hypothesis is used. |
| Real-analytic dependence of `q` | likely valid | The coefficient map has square, injective linearization. The maximum-principle argument forces its kernel to vanish, so the real-analytic implicit-function theorem applies. |
| Real-analytic dependence of `G` | likely valid | Costara's finite Gram formula uses only analytic rational operations and inversion of a positive Gram matrix. The intrinsic Gram polynomial avoids Cholesky branch issues. |
| Outer-root discriminant | valid | The ordinary polynomial discriminant is real-analytic and is nonzero at the equilateral factor `q(z)=z^3-rho`. |
| Iterated resultant identity | valid | Both outer factors are monic; applying the root formula for resultants twice gives the product of all nine `G(alpha_r,alpha_t)`. Hermitian symmetry makes it real and nonnegative. |
| Equilateral nonzero witness | valid | The explicit positive coefficients reduce a hypothetical cross zero to `A2/A1=rho^(-2/3)`, contradicted by the strict elementary inequality in the packet. |
| Real-analytic zero-set conclusion | valid/external | A nonzero real-analytic function on a connected open set has a null, empty-interior zero set. |
| Equilateral neighborhood with collisions | valid | In each of two disjoint nonreal clusters, every base residue is the same nonzero number. A sum of values within half its modulus cannot cancel. |

## Counterexample search

The independent numerical reconstruction checked:

- the equal-mass equilateral point, where pole products collide but all
  individual off-diagonal residues are nonzero;
- a nonsymmetric nearby support/weight perturbation, where all nine products
  are separated and all six cross values are nonzero;
- a generic small-mass example with distinct first-order radial splittings.

No computational contradiction was found. The calculation uses floating
point arithmetic and is not part of the proof.

## Main residual risks

- A reviewer should reconstruct the real-linear Jacobian count in the spectral
  factorization lemma, although injectivity and the number of variables match.
- The new Vandermonde step should be checked directly against the index shifts
  in Theorem 2.1. The shifts only rescale rows and columns by nonzero outer-root
  factors, so the exponential comparison is unaffected.
- The theorem is generic only. It gives no classification on either analytic
  zero set, and neither zero condition is claimed sufficient for subnormality.

## Confidence

Score: 93/100.

The key reduction is finite, invariant under pole relabeling, and directly
matches the source complete-monotonicity matrices. It also removes the earlier
pole-product discriminant and its perturbative witness. The remaining review
burden is concentrated in the spectral-factor analytic-dependence lemma and
the Vandermonde congruence.

## Human review recommendation

Send to an operator theorist familiar with rational de Branges--Rovnyak
spaces. First check Lemma 1 (analytic dependence) and the simple-root
orthogonality criterion; then verify the source labels and the local
grouped-residue argument.
