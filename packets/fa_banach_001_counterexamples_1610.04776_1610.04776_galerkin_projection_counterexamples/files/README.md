# Counterexamples to the Galerkin projection lemmas in arXiv:1610.04776

**Status:** candidate counterexample, likely valid; human review recommended.

**Source:** M. Ali Khan and Nobusumi Sagara, *Fatou's Lemma, Galerkin
Approximations and the Existence of Walrasian Equilibria in Infinite
Dimensions*, arXiv:1610.04776v2 (2017), especially Theorems 6.2 and 6.3 and
the proofs of Theorems 7.1 and 7.2.

This packet gives elementary counterexamples to two exact auxiliary claims in
the source paper.

1. Theorem 6.2 says that every continuous projection from an ordered locally
   convex Hausdorff space onto a closed subspace is positive.  In
   \(\mathbb R^2\) with the coordinate cone, the projection
   \(P(a,b)=(a,-a)\) onto \(\operatorname{span}(1,-1)\) maps the positive
   vector \((1,0)\) to a nonpositive vector.
2. Theorem 6.3 says that arbitrary continuous projections onto a nested dense
   Galerkin scheme have a subsequence converging weakly to the identity.  On
   \(\ell^2\), take \(V_n=\operatorname{span}\{e_1,\ldots,e_n\}\) and
   \[
   P_nx=\sum_{k=1}^n x_ke_k+n^3x_{n+1}e_1.
   \]
   Each \(P_n\) is a bounded projection onto \(V_n\), but for
   \(x_1=0\), \(x_k=k^{-2}\) (\(k\ge2\)), the first coordinate of \(P_nx\)
   is \(n^3/(n+1)^2\to\infty\).  Thus no subsequence converges weakly to
   \(x\).  The same self-dual example refutes the intended statement of
   Theorem 6.3(ii).

The source uses Theorem 6.2 to assert positivity of the finite-dimensional
projections in Step 1 of its equilibrium proofs and Theorem 6.3 to identify
weak or weak-star limits of projected endowments.  Therefore those proofs are
not established as written.  This packet does **not** claim that the principal
equilibrium theorems are false, and it does **not** answer the concluding
question whether saturation is necessary.

The PDF contains the exact statements, proofs, repair conditions, bounded
novelty search, and verification notes.  The checker in `code/` confirms the
finite-coordinate identities numerically; the mathematical proof is exact and
does not rely on the checker.

Ledger record:
`runs/fa_banach_001/ledger/results/1610.04776_galerkin_projection_counterexamples.json`.

