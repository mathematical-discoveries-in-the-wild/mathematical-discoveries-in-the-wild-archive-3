# Arbitrary Poisson boundary measures give coordinate multipliers

Status: `full_solution_likely_valid`  
Model: `GPT5.6`  
Source: Chavan--Gupta--Reza, arXiv:2001.09616v2 / JFA 279 (2020), 108733  
Target: published Question 1.2(a), Proposition 3.5, and the unresolved statement
on p. 12 for arbitrary finite positive boundary measures.

## Result

For every complex dimension `d >= 2`, every finite positive Borel measure
`mu` on the unit sphere, and every `f in D(mu)`, the packet proves

`integral_B |f|^2 P[mu] dV <= C_d (mu(S)||f||_H2^2 + integral_B |grad f|^2 P[mu] dV)`.

Thus `P[mu] dV` is a Carleson measure for `D(mu)`. By source Proposition 3.5,
every coordinate function is a multiplier, and source Theorem 3.4 makes the
coordinate multiplication tuple a joint 2-isometry. This is an affirmative
answer to the remaining scalar part of Question 1.2(a).

## Proof mechanism

The proof reduces by Tonelli to the atomic weights `P(z,eta)`. In real polar
coordinates centered at the boundary singularity `eta`, the Poisson power
cancels the polar Jacobian exactly:

`P(z,eta)dV = c(2<omega,eta>-rho) d rho d omega`.

Finite atomic gradient energy gives a single tip trace: radial energy gives
ray limits and the `rho^-2` angular energy forces those limits to agree. An
anchored one-dimensional Hardy inequality then controls the entire atomic
weighted `L2` norm by that trace and the atomic energy.

To bound the trace, average over the unitary stabilizer of `eta`, reducing to
`h(<z,eta>)` while contracting both relevant norms. Integrating the transverse
variables yields an explicit marginal weight `W_d`; on every dyadic Stolz box
at `1`, `W_d >= c_d/(1-r)`. Submean estimates and a bounded-overlap dyadic sum
bound the tip trace by the Hardy norm plus atomic energy.

## Verification and novelty

The included guard script checks 800 centered-polar identities, 10,001 Hardy
kernel samples (maximum exactly `3/16`), and 567 marginal samples in complex
dimensions 2 through 8. The proof does not use polynomial density or radial
dilation.

The bounded novelty search covered the four run indexes, exact source wording,
exact title/core terms, published labels, and later visible work/publication
lists of the source authors. It found no explicit later answer. Novelty
confidence is moderate because the search was not a full citation-database
review and the weighted trace mechanism may be known in another language.

Human review recommendation: `send_to_human`. Mathematical focus: the common
finite-energy tip trace and its identification after stabilizer averaging.
Literature focus: citing papers of the 2020 JFA article that discuss Question
1.2(a).

The final six-page PDF compiled without warnings, every page was visually
inspected, and its SHA-256 is
`c04b4aeab14d07509dc4833635940f27f5785f1704a3e95d1763cf2d9dc8d0a8`.
