# Verification report

Verdict: **candidate counterexample, likely valid**.

The two examples were checked directly against the displayed hypotheses of
Theorems 6.2 and 6.3 in arXiv:1610.04776v2.

- For Theorem 6.2, `P(a,b)=(a,-a)` is continuous, has range
  `span{(1,-1)}`, fixes that range, and is therefore idempotent.  It sends the
  positive vector `(1,0)` outside the coordinate cone.
- For Theorem 6.3, the formula
  `P_n x = sum_{k<=n} x_k e_k + n^3 x_{n+1}e_1` fixes `V_n`, has range in
  `V_n`, and is bounded for each fixed `n`.  For `x_k=k^-2` (`k>=2`) its
  first coordinate equals `n^3/(n+1)^2`, which diverges.  The self-duality of
  `ell^2` gives the weak-star counterexample as well.
- The included finite-coordinate checker passed all programmed idempotence,
  range-fixing, and divergence checks for `1 <= n <= 250`.
- No computational test is used in the proof.

Scope: the packet refutes the auxiliary theorems as stated and demonstrates
that the Section 7 Galerkin proofs are incomplete.  It does not disprove the
Walrasian equilibrium conclusions and does not settle saturation necessity.

