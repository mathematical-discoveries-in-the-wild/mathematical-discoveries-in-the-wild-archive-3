# Verification report

## Claim checked

The exact localization claim

`supp(x_alpha^delta) subset {1,...,n(delta)}`

fails under the deterministic noise model, even in the polynomial diagonal
oversmoothing example and under the parameter scaling of Gerth--Hofmann's
2019 follow-up.

## Verdict

`candidate counterexample - likely valid`

## Step checks

1. **Model assumptions:** valid. For `sigma_k=k^(-beta)`, `beta>0`, the
   diagonal map on ell2 is compact and injective. For
   `x_k^dagger=k^(-eta)`, `1/2<eta<=1`, the exact solution lies in
   `ell2` but not `ell1`.
2. **Minimizer formula:** valid. The squared Hilbert residual and ell1 penalty
   decouple by coordinate, giving
   `x_k=S_(alpha/sigma_k^2)(y_k^delta/sigma_k)`.
3. **Truncation index:** valid. For
   `phi(delta)=min_m(delta/sigma_m+||(I-P_m)x^dagger||_2)`, every minimizing
   index tends to infinity as `delta` tends to zero.
4. **Parameter comparison:** valid. Since
   `phi(delta)>=delta/sigma_n`,
   `alpha/(delta sigma_(n+1)) <= c_alpha (sigma_n/sigma_(n+1))/sqrt(n)`.
   The polynomial ratio is at most `2^beta`, so the right side tends to zero.
5. **Admissible noise:** valid. `y^delta=y+delta e_(n+1)` has noise norm
   exactly `delta`.
6. **Violation:** valid. For small `delta`, `alpha<delta sigma_(n+1)`, and
   therefore soft thresholding leaves coordinate `n+1` strictly positive.

## Computational check

Command:

`conda run --no-capture-output -n sandbox python code/verify_counterexample.py`

For `beta=1`, `eta=3/4`, and `c_alpha=10`, five noise levels from `1e-4` to
`1e-6` were tested. In every case the computed `n(delta)+1` coefficient was
strictly positive; the threshold ratio decreased from about `0.0762` to
`0.0121`. This is a sanity check, not part of the proof.

## Scope

- The result refutes exact initial-segment support containment, which is the
  reading that would make the source's truncation tail vanish.
- It does not refute a cardinality-only bound on the support.
- It does not refute the later paper's quantitative tail estimate or its
  convergence-rate theorems.
- The 2019 follow-up itself treats noisy tails quantitatively rather than
  asserting their exact vanishing.

## Novelty check

A bounded search through 2026-08-27 used arXiv, the exact titles, author names,
the exact source phrase, `n_inf`, `support`, `noise`, `counterexample`,
`correction`, and `erratum`. It located the announced 2019 follow-up and later
oversmoothing work, but no explicit statement of this counterexample or an
erratum addressing the exact support cutoff. Novelty confidence is therefore
moderate, not definitive.

## Human review recommendation

Verify that the source's phrase "support ... not larger than n(delta)" was
indeed intended as containment in the first `n(delta)` coordinates. The
surrounding `P_n` argument and the later paper's replacement by a tail bound
strongly support that interpretation.

