# Verification report

## Claim checked

For `d >= 3` and `0 < s < 1`, the weighted polygonal closure furnished by
Corollary 5.3 of arXiv:2403.03901 contains a closed current of finite
`s`-fractional mass which is not the boundary of any 2-current of locally
finite mass.

## Adversarial checks

1. **Threshold.** The proof uses `d-s-2 > 0`.  This holds exactly throughout
   the claimed range `d >= 3`, `0 < s < 1`; it fails in the planar case, which
   the source already identifies as positive.
2. **Fourier estimate.** For a potential
   `u=A eta(x) sin(N x_1)`, the boundary multiplier contributes
   `xi_1^2+xi_2^2`, while the source norm contributes
   `|xi|^{-(d-s)}`.  Translating the Schwartz Fourier transform of `eta` to
   `+/- N e_1` gives squared norm `O(A^2 N^{2-d+s})`, hence norm
   `O(A N^{-(d-s-2)/2})`.  The singular region near frequency zero is harmless
   because the translated Schwartz tail decays faster than any power and
   `|xi|^{2-d+s}` is locally integrable.
3. **Flat-dual lower bound.** The test 1-forms have uniformly bounded exterior
   derivative and common compact support.  Pairing the boundary with them
   gives a diagonal term comparable to the potential amplitude.  Therefore a
   locally finite-mass filling would give a single uniform bound from its mass
   on that compact set, contradicting the unbounded pairings.
4. **Infinite sum.** Frequencies can be chosen inductively so that the
   `C_s` norms are summable and all off-diagonal test pairings are summable.
   Schwartz decay gives both requirements simultaneously.  Weighted Fourier
   convergence defines a compactly supported current in `C_s`; boundary zero
   passes to the limit.
5. **Membership in the proposed closure.** Corollary 5.3 applies to every
   closed current in `C_s`, so it supplies weighted closed polygonal
   approximants with weak-star convergence and convergence of `M_s`.
6. **Coefficient caveat.** The proof does not show membership in a closure
   restricted to integer-coefficient polyhedral currents.  The packet states
   this limitation prominently and makes no claim about that stricter class.

## Verdict

Likely valid as a scoped counterexample to the weighted closure explicitly
available from Theorem 5.1 and Corollary 5.3.  The proof is analytic and does
not depend on numerical evidence.

## Human review focus

Check the weighted-shift estimate in Lemma 1, the simultaneous lacunary
frequency selection, and whether the intended word "integer" in the source
was meant to impose classical integer coefficients despite the noninteger
weights in the approximation theorem.
