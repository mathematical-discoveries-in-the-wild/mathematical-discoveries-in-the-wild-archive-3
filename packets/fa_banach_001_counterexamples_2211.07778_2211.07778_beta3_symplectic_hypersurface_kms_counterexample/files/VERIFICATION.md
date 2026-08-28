# Verification report

## Exact target

Remark 1 on printed page 38 of arXiv:2211.07778v2 conjectures that the
`GSp_4` system has no KMS state at `beta=1` or `beta=3`. Proposition 2.12 of
the same paper reduces existence to a normalized Gamma-invariant Radon measure
with scaling exponent `-beta`.

## Mathematical audit

1. **Support in the monoid.** For `M=[v w 0 0]`, the equation
   `omega(v,w)=0` implies `M^T J M=0`; hence `M` belongs to the multiplier-zero
   locus of `MSp_4`.
2. **Left stability.** `gM=[gv gw 0 0]`, and
   `omega(gv,gw)=lambda(g) omega(v,w)`, so the hypersurface is stable under
   every symplectic similitude.
3. **Existence and Radon property.** The p-adic delta approximation is locally
   integrable at `(0,0)`. Shells where `min_i v_p(v_i)=k` contribute on the
   order of `p^-3k`, a convergent series.
4. **Integral mass.** Direct shell summation gives exactly
   `c_p=(1-p^-4)/(1-p^-3)`, finite and positive.
5. **Scaling exponent.** The two-vector ambient Jacobian is
   `|det g|_p^2=|lambda(g)|_p^4`; the one hypersurface equation contributes
   `|lambda(g)|_p^-1`. The product is `|lambda(g)|_p^3`.
6. **Adelic sign.** For positive rational `lambda(g)`, the product formula
   gives `prod_p |lambda(g)|_p^3=lambda(g)^-3`, matching the source convention.
7. **Normalization.** Dividing each local measure by `c_p` makes its integral
   compact factor have mass one. The restricted product therefore gives mass
   one to the integral finite-adelic locus. Normalized Haar measure gives mass
   one on `Gamma\PGSp_4^+(R)`.
8. **Gamma invariance.** The real factor is left Haar and
   `lambda(gamma)=1` for `gamma in Sp_4(Z)`, so the product measure is invariant.
9. **Conclusion.** Every clause of Proposition 2.12 is met with `beta=3`.

The dependent-pair locus is null: for each nonzero `v`, the line `Q_p v` has
zero Haar measure in the three-dimensional hyperplane `v^perp`. Thus the
construction is genuinely supported on the rank-two singular stratum almost
everywhere, although this fact is not needed for existence.

## Independent sanity checks

- The local mass can also be recovered modulo `p^n`: if `v` has coordinate
  valuation `k<n`, the number of `w mod p^n` satisfying
  `omega(v,w)=0 mod p^n` is `p^(3n+k)`. The zero vector supplies the final
  negligible tail. Dividing the total by `p^(7n)` tends to `c_p`.
- Central scalar `aI` has multiplier `a^2`. The pair `(v,w)` is scaled in
  eight ambient coordinates by `a`, while the one quadratic equation has
  degree two; the resulting measure scales by `|a|_p^6=|a^2|_p^3`, consistent
  with the general calculation.

## Source and novelty checks

- Checked `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  and `proof_gaps/index.tsv` for the arXiv id, title, KMS_3, and GSp_4 terms.
- Checked the exact conjecture phrase and arXiv searches combining the title,
  `GSp_4`, `KMS_3`, and the exceptional temperature.
- No later arXiv answer was found as of 2026-08-26. This is a bounded search,
  not a certification of novelty.

## Human review recommendation

Review the construction of the local hypersurface measure and the passage from
cylinder-set scaling to the restricted-product Radon measure. Also confirm that
the source's Proposition 2.12 is intended with the literal normalization and
scaling conventions printed in arXiv:2211.07778v2.

