# Automorphism invariance for arbitrary increasing radial weights

Status: `candidate counterexample/disproof - likely valid, awaiting human review`

Source: David Norrbo, *Compactness and related properties of weighted composition operators on weighted BMOA spaces*, arXiv:2502.05533, Conjecture 2 on published page 39.

## Result

Conjecture 2 predicts an increasing radial weight `v`, a disk automorphism `phi`, and an `f in BMOA_v` for which `f composed with phi` is not in `BMOA_v`.

The packet proves the opposite universal statement. For every positive nondecreasing radial weight, every disk automorphism induces a bounded invertible composition operator on `BMOA_{v,p}` for every `1 <= p < infinity`. It also preserves `VMOA_{v,p}`. In particular, the conjectured example cannot exist.

The mechanism is short. A fixed automorphism changes boundary depth only by a constant factor. If `b=phi(a)` lies radially inside `a`, move `b` outward on its ray to a point `c` with `|c|=|a|`. The points `b,c` remain at uniformly bounded pseudohyperbolic distance, so their `H^p` oscillations are uniformly comparable. Radial monotonicity then supplies exactly the needed weight comparison.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: rendered crop of Conjecture 2.
- `verification.md`: proof audit and novelty-search bounds.

Ledger: `runs/fa_banach_001/ledger/results/2502.05533_automorphism_invariance_disproof.json`.

## Human review recommendation

Review as a full disproof of Conjecture 2. The two points most worth checking are the exact automorphism covariance of `gamma_p` and the uniform pseudohyperbolic bound for the radial comparison point. Both are proved explicitly in the packet.
