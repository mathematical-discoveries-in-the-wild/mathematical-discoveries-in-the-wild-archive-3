# Sharp small-gap lower frame bound for finite exponentials

Status: `candidate full asymptotic answer - likely valid, awaiting human review`

Source: Ole Christensen, *Six problems in frame theory*, arXiv:1308.5065, Section 7.2, page 22.

## Exact result

For increasing real frequencies `lambda_1 < ... < lambda_N` with adjacent gaps at least `delta`, let `A(lambda)` be the optimal lower frame bound of the exponentials `exp(i lambda_j x)` in `L2(-pi,pi)`, and let `m_N(delta)` be the infimum of `A(lambda)` over every such configuration. Put `n=N-1`. The packet proves the exact unrestricted asymptotic

```text
lim_(delta -> 0) m_N(delta) / delta^(2N-2)
  = 2 pi^(2n+1) 4^n / ((2n+1) binom(2n,n)^3).
```

Arithmetic clusters `a,a+delta,...,a+n delta` attain this constant. Conversely, every asymptotically extremizing sequence is arithmetic up to translation and an `o(delta)` perturbation. This gives the exact leading coefficient, not only the sharp exponent.

For every `0 < delta <= 1`, the packet retains the explicit global estimate

```text
m_N(delta) >= (pi/2) (delta/(4 C_TN))^(2N-2),
```

where `C_TN` is the universal constant in Turan-Nazarov.

## Proof mechanism

Newton divided differences reduce a collapsing exponential cluster to the monomials `1, ix, ..., (ix)^n/n!`. The exact analytic constant is the squared norm of the monic Legendre polynomial on `(-pi,pi)`, while the geometric constant is the squared norm of the barycentric weight vector. Minimum separation maximizes these weights exactly at arithmetic spacing. A separate confluence argument shows that multi-cluster and hierarchical degenerations lose powers and therefore cannot be extremal.

## Scope and literature boundary

This completely determines the fixed-`N` small-gap extremal problem, including its sharp constant and asymptotic geometry. The arithmetic prolate-matrix constant was already known through Slepian's asymptotic; the candidate new content is that it is the unrestricted worst constant over all separated real configurations, together with rigidity. The bounded search found no exact match. The packet does not claim the exact value of `m_N(delta)` away from zero or simultaneous asymptotics as `N` grows.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original open-problem paper.
- `supporting_paper_1206.1657.pdf`: source for the two classical inequalities used in the proof.
- `figures/open_problem_crop.png`: source-page evidence.
- `code/make_crop.py`: reproducible crop helper.
- `code/verify_numeric.py`: deterministic Gram-matrix sanity checks.
- `verification.md`: proof and novelty audit.

Ledger: `runs/fa_banach_001/ledger/results/1308.5065_optimal_gap_exponent_finite_exponentials.json`.

## Human review recommendation

Review as a candidate full quantitative answer. The critical checks are uniformity of the one-cluster divided-difference asymptotic, positivity of the multi-cluster confluent limit, the barycentric rigidity argument, and the novelty boundary with known prolate asymptotics.
