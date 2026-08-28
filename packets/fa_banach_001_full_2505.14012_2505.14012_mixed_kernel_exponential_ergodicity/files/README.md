# Full mixed-kernel exponential ergodicity

Status: `full_solution_likely_valid`

Source: Anna-Mariya Otsetova and Jonas M. Tölle, *Ergodicity for stochastic
neural field equations*, arXiv:2505.14012v1 (2025), PDF page 5.

The source identifies its main contribution as existence of a unique invariant
measure and exponential ergodicity under a quantitative decay condition, then
asks for analogous results when the connectivity kernel is neither
non-negative nor non-positive definite.  The following metastability and
Kramers-law sentence is explicitly a separate problem.

## Full resolution

For the source equation on `H=L^2(U,rho)`, retain only its well-posedness
Assumptions 1 and 2.  Write `L_f=Lip(f)`, `L_B=Lip(B)`, and let `K` be the
bounded kernel operator.  If

```text
kappa = 2 alpha - 2 ||K|| L_f - L_B^2 > 0,
```

then no sign, symmetry, compactness, or invariant-nonlocal-subspace assumption
on `K` is needed: the Markov semigroup has a unique invariant law in
`P_2(H)` and contracts `W_2` at rate `exp(-kappa t/2)`.  Hence every
finite-second-moment initial law converges exponentially to equilibrium.

The proof uses synchronous coupling for contraction and a direct Itô moment
estimate to show that `P_t^* delta_0` is uniformly square-integrable and
`W_2`-Cauchy.  This bypasses the source's sign-dependent compact embedding and
Krylov--Bogoliubov step.

The dimensionally consistent form of source Assumption 5 is

```text
2 sqrt(2) ||K|| L_f + L_B^2 < 2 alpha.
```

It strictly implies `kappa > 0`.  Thus the packet recovers every conclusion of
source Theorem 1.2(iii) for arbitrary mixed-sign `K`, while deleting source
Assumptions 3 and 4.  The theorem also uses the sharper threshold and proves
the stronger `W_2` estimate.

## Scope

This is classified as a full solution to the source's stated mixed-kernel
exponential-ergodicity question in the same strict-dissipation regime as its
main theorem.  It does not assert ergodicity for every parameter value,
uniqueness outside `P_2(H)`, or solve the separately stated metastability and
Kramers-law problem.

## Review files

- `solution_packet.pdf`: full theorem and proof.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source PDF page 5, showing the question.
- `verification.md`: adversarial step check.

The incidental constant/rate issue found in the source proof is documented
separately under
`proof_gaps/2505.14012_noise_lipschitz_constant_and_rate_gap/`; it is not part
of the basis for the full-solution claim.

## Novelty check

The four run indexes, the local parsed arXiv corpus, and bounded web/arXiv
searches were checked using the source arXiv id/title, the exact mixed-kernel
phrase, stochastic-neural-field ergodicity, and Hilbert-space Wasserstein
contraction keywords.  The latest official arXiv source available on 26 August
2026 still states the problem, and no later paper explicitly resolving it was
found.  The contraction mechanism is standard in dissipative stochastic
evolution equations, so originality confidence is moderate; the packet's
contribution is the exact sign-free specialization and complete direct proof
for the source model.

Human review recommendation: **send to human**, with priority on the
well-posedness-to-Markov-flow handoff and the `L_B^2` constant.
