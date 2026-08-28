# Verification report

Verdict: `literature_implied_answer (full Problem 49)`.

## Hypothesis audit

- Mori's Section 3 equips the connected noncompact Lie group with a
  left-invariant Riemannian metric and defines `rho` as its positive heat
  kernel for `partial_t u = Delta u`.
- Every left-invariant Riemannian metric on a Lie group is complete.
- Left translations are isometries, so the eigenvalues of the Ricci tensor
  are constant under translation. Hence `Ric >= -k g` for some finite
  `k >= 0`.
- Li--Xu Theorem 1.4 applies to every positive solution on a complete
  noncompact Riemannian manifold with this Ricci lower bound. Its heat-equation
  normalization matches Mori's Definition 12.

## Deduction audit

Set `u(g,s)=rho(s,g)` and use the same point for `x_1` and `x_2` in Li--Xu
Theorem 1.4. The distance term vanishes and yields

```text
rho(t,g) <= C(t,t+epsilon,k,dim G) rho(t+epsilon,g)
```

uniformly in `g`. Thus

```text
||f||_{L2(rho_t dg)} <= sqrt(C) ||f||_{L2(rho_{t+epsilon} dg)}.
```

The inclusion claimed by Problem 49 is therefore well-defined and continuous.
Since both weights are positive and continuous, `C_c(G)` lies in the
later-time space. Standard Radon-measure approximation makes `C_c(G)` dense
in `L2(rho_t dg)`, proving density.

## Scope and novelty audit

- Full coverage: source Problem 49 for all `t, epsilon > 0`.
- Strengthening: the same proof covers every connected noncompact Lie group
  with a left-invariant Riemannian metric.
- Not covered: Problems 46--48.
- Provenance: direct implication of Li--Xu Theorem 1.4; supporting authors
  could not have cited the 2019 source question.
- Searches: run indexes; exact Problem 49 wording and close variants;
  arXiv id, title, and author queries. No explicit later answer found.
- No computational check is needed: the proof is theorem-theoretic and the
  norm comparison is one line.
