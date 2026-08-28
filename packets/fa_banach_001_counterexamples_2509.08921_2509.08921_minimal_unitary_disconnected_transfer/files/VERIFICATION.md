# Verification report

Status: candidate full counterexample, likely valid.

## Claim audited

Remark 2.4 of arXiv:2509.08921 asks for two minimal, analytically equivalent
univariate realizations whose invertibility domains are disconnected and whose
transfer functions differ on a component not containing 0.

## Line-by-line audit

1. **Partition.** A measurable partition `T=E disjoint union F` with both
   pieces of positive measure in every open arc exists. Enumerate a countable
   arc basis and recursively place two disjoint positive-measure nowhere-dense
   compact sets in each basis arc, avoiding all previously placed sets. Put all
   first sets into `E` and all second sets into its complement.

2. **Spectrum and domain.** On `L2(G,m)`, multiplication by `zeta` is unitary.
   Because every arc has positive `G`-measure, its essential range and spectrum
   are the full unit circle. Hence `I-zU_G` is invertible exactly when
   `|z| != 1`.

3. **Cyclicity.** If `h` is orthogonal in `L2(G)` to every analytic monomial,
   then `1_G conjugate(h)`, extended by zero to the circle, has only strictly
   positive Fourier modes. It is an `H2_0` boundary function and vanishes on
   `T\G`, a set of positive measure. Hardy boundary uniqueness forces it to be
   zero. Thus analytic polynomials are dense. Conjugation gives density of
   anti-analytic polynomials. Therefore `c_G=1` is `U_G`-cyclic, and
   `b_G=+/- conjugate(zeta)` is `U_G^*`-cyclic because its adjoint orbit is the
   shifted anti-analytic monomial family.

4. **Analytic equivalence.** With the standard convention
   `b^*x = integral conjugate(b)x dm`, the moments are

       b_F^* U_F^n c_F = integral_F zeta^(n+1) dm,
       b_E^* U_E^n c_E = -integral_E zeta^(n+1) dm.

   Their difference is `integral_T zeta^(n+1) dm=0` for every `n>=0`.
   Equality of all moments gives equality of the matrix-level power series
   `sum_{n>=0} Z^n (b^*U^n c)` for `||Z||<1`, which is precisely analytic
   equivalence at 0.

5. **Exterior disagreement.** On `|z|>1`, subtraction gives

       f_F(z)-f_E(z) = integral_T zeta/(1-z zeta) dm
                     = -1/z.

   The last equality follows by the uniformly convergent Laurent expansion
   `zeta/(1-z zeta)=-(1/z) sum_{k>=0} z^(-k) zeta^(-k)`.

All hypotheses in the source question are therefore met, and the requested
global disagreement is nonzero at every exterior point.

## Computational status

No numerical computation is used. The identities are exact Fourier and
resolvent calculations. The proof depends only on the standard uniqueness
theorem that a nonzero Hardy-space function cannot have boundary values zero
on a set of positive Lebesgue measure.

## Bounded novelty check

The four run indexes were searched for arXiv:2509.08921, the exact title,
“minimal and analytically equivalent realizations,” disconnected invertibility
domains, unitary realizations, and Markov parameters. Exact-phrase and close
arXiv/web searches through 27 August 2026 returned the source paper and general
realization literature, but no later paper or preprint giving this example or
answering Remark 2.4. Novelty is plausible, not certified.

## Human review recommendation

Check the Fourier-sign convention in the two moment formulas, the application
of Hardy boundary uniqueness to polynomial density on a measurable subset,
and the observation that scalar moment equality implies matrix-level analytic
equivalence in one variable. These are the only substantive checkpoints.
