# The conjectured grid-gradient monotonicity can fail

Status: `candidate_counterexample_likely_valid`.

Source: E. Bottazzi, *Describing limits of integrable functions as grid
functions of nonstandard analysis*, arXiv:2101.08108; Partial Differential
Equations and Applications 2 (2021), article 51. The target is the fourth
conjectural bullet in Remark 4.2 on source PDF page 18.

## Claimed counterexample

The source conjectures that the `L2` norm of
`D^+- *phi(u(t,.))` is nonincreasing along the grid flow

```text
u_t = Delta_X *phi(u).
```

This is false under the hypotheses in force around the remark. Define the
globally Lipschitz, continuously differentiable function

```text
phi(s) = 4s               for s <= 0,
         s(2-s)^2         for 0 <= s <= 2,
         0                for s >= 2.
```

It satisfies `phi(0)=0` and `phi(s)>=0` for `s>=0`, but
`phi'(s)<0` on `(2/3,2)`. Restrict a nonzero smooth compactly supported bump
`rho` to the grid and take `u_0=2-rho/2`. Then `u_0` is nonnegative and bounded, while
`v_0=*phi(u_0)` vanishes in a boundary layer. Exact grid summation by parts
gives

```text
d/dt [ (1/2)||D^+- v(t)||_2^2 ] at t=0
  = - <phi'(u_0) Delta_X v_0, Delta_X v_0> > 0.
```

Thus both the forward- and backward-difference norms increase initially.
The strict sign follows because `phi'(u_0)<0` wherever `v_0>0`, while
`phi'(u_0)=0` wherever `v_0=0`.

## Scope

This disproves only the fourth bullet of source Remark 4.2. It does not affect
the first three conjectural statements about Dirac Young measures, nor the
paper's main representation theorems. The calculation also explains the
missing hypothesis: the proposed monotonicity is valid when `phi'(u)>=0`, but
the sign reverses on decreasing branches.

## Files

- `solution_packet.pdf`: expert-facing counterexample packet.
- `main.tex`: LaTeX source.
- `verification.md`: adversarial proof and scope audit.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: source Remark 4.2 and its four bullets.
- `code/check_energy_derivative.py`: exact rational five-node check.

## Novelty check

A bounded check was performed on 2026-08-27. The run indexes, the official
arXiv page, the published Springer version, exact-phrase searches for the
gradient claim, and searches for an erratum or correction were checked. The
published version still states the conjecture, and no later correction or
explicit counterexample was found. This is not an exhaustive citation search,
so novelty remains provisional.

## Human review recommendation

Send to an expert in finite-difference gradient flows or nonstandard PDEs.
The principal review point is that the source's Neumann Laplacian and its
forward/backward norms obey the displayed summation-by-parts identity when the
test profile vanishes in a boundary layer. The packet makes this localization
explicit and also supplies a direct five-node rational check.
