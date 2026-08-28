# Counterexample packet: a KMS_3 state from a symplectic hypersurface

Status: `candidate_counterexample_likely_valid`

Source: Ismail Abouamal, *Bost-Connes-Marcolli system for the Siegel modular
variety*, arXiv:2211.07778v2, Remark 1 on printed page 38.

## Result

The source conjectures that its `GSp_4` system has no KMS state at either
`beta=1` or `beta=3`. This packet refutes the conjecture at `beta=3`.

At each prime `p`, consider ordered pairs `(v,w)` in `Q_p^4` satisfying the
single equation `omega(v,w)=0`. The canonical p-adic hypersurface measure is
defined as the limit

```text
p^n integral Phi(v,w) 1_{omega(v,w) in p^n Z_p} dv dw.
```

It has finite nonzero mass `(1-p^-4)/(1-p^-3)` on the integral locus and
scales under `g in GSp_4(Q_p)` by `|lambda(g)|_p^3`. After local normalization,
the restricted product over all finite primes scales under rational `g` by
`lambda(g)^-3`. Embedding `(v,w)` as the first two columns of a multiplier-zero
matrix places the measure inside `MSp_4(A_f)`. Its product with normalized Haar
measure on `PGSp_4^+(R)` satisfies exactly the source paper's normalized
measure criterion for a KMS_3 state.

The construction evades the source's obstruction because the support is a
nonlinear hypersurface, not a stable linear subspace.

## Files

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: source conjecture from printed page 38.
- `VERIFICATION.md`: hypothesis, scaling, normalization, and novelty audit.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Scope

The result establishes existence for the paper's `GSp_4` system at `beta=3`.
It does not classify all KMS_3 states, decide `beta=1`, or automatically settle
the separate non-free Connes-Marcolli quotient.

## Novelty status

The four lightweight run indexes, exact conjecture phrase, paper title, and
arXiv keyword combinations were checked on 2026-08-26. No later arXiv answer
was found. Novelty is plausible, not certified.

