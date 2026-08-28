# Verification Report

## Claim Checked

Under source Assumptions 1 and 2 and
`kappa = 2 alpha - 2 ||K|| Lip(f) - Lip(B)^2 > 0`, the stochastic neural
field semigroup has a unique invariant probability measure in `P_2(H)` and is
an `exp(-kappa t/2)` contraction in `W_2`, without any sign-definiteness
assumption on the kernel.

## Verdict

Full solution likely valid, under the source-faithful interpretation recorded
below.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Global solution and Markov flow | valid/external | Supplied by source Theorem 3.3 under Assumptions 1 and 2; coefficients are globally Lipschitz. |
| Synchronous difference estimate | valid | Itô gives the drift term `2 ||K|| Lip(f)` and the quadratic-variation term `Lip(B)^2`; Grönwall yields the stated mean-square contraction. |
| Uniform second moment | valid | The affine parts `f(0)` and `B(0)` are absorbed by Young inequalities after choosing epsilon so the remaining coercivity is positive. |
| `P_t^* delta_0` is `W_2`-Cauchy | valid | For `r=t+s`, semigroup plus contraction gives a bound uniform in `s`, using the uniform moment estimate. |
| Existence/invariance of the limit | valid | `P_2(H)` is complete; applying a fixed `P_h^*` is Wasserstein-Lipschitz, so the limit is invariant. |
| Uniqueness and convergence | valid | Contract two invariant `P_2` laws and let time tend to infinity. The same estimate gives convergence from any `P_2` initial law. |
| Mixed-sign scope | valid | The proof uses only the operator norm of `K`; no quadratic-form sign or symmetry occurs. |
| Exact source corollary | valid | The corrected source condition `2 sqrt(2)||K||Lip(f)+Lip(B)^2<2 alpha` strictly implies `kappa>0`; source Assumptions 3 and 4 can therefore be deleted. |
| Exponential ergodicity/mixing | valid | `W_2` convergence implies weak convergence, the source's Lipschitz-observable estimate, and its Fortet--Mourier mixing estimate. |

## Counterexample Search

The two-dimensional linear model with
`K=diag(a,-b)`, `a>=b>0`, `f(x)=x`, and `B(u)q=sigma*q*u` has genuinely mixed
spectrum.  Along the positive eigendirection its exact mean-square difference
exponent is `-2 alpha + 2a + sigma^2`, matching the packet's `kappa` and
confirming both the squared-noise constant and the halved `W_2` rate.  No
contradiction was found.

## Important Source-Comparison Note

The source defines `C_B` by an unsquared Lipschitz inequality but later places
`C_B`, rather than `C_B^2`, in quadratic-variation estimates.  It also derives
a mean-square bound and then states a Lipschitz-observable rate without taking
the square root.  The packet does not inherit those constants: it uses
`L_B^2` and the Wasserstein/Lipschitz rate `exp(-kappa t/2)`.

## Full-Solution Scope Audit

- The source calls unique invariant measure plus exponential ergodicity under
  its quantitative Assumption 5 its main contribution, and immediately asks
  for the mixed case.
- The packet proves those conclusions under a sharper corrected condition and
  without the sign-dependent Assumptions 3 and 4.
- The following source sentence separately asks about metastability and
  Kramers' law; those topics are not part of this resolution.
- No result is claimed for `kappa <= 0`, and uniqueness is proved within
  `P_2(H)`, the same moment class targeted by the source theorem.
- The latest official arXiv source available on 26 August 2026 still contains
  the open sentence.  Bounded searches found no later exact resolution.

Confidence: theorem 95/100; full-scope classification 88/100.

Human review recommendation: send to human.
