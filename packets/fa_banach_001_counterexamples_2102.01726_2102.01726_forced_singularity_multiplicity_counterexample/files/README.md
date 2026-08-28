# The forced multiplicity is ceil((d mod n)/2), not binomial(d mod n,2)

Status: `candidate_full_negative_solution_likely_valid`

## Source conjecture

Faye Pasley Simon and Cynthia Vinzant, *Invariant hyperbolic curves:
determinantal representations and applications to the numerical range*,
arXiv:2102.01726 (2021), Section 8.1 on PDF/printed page 20.

For `r = d mod n >= 3`, the authors conjecture that the forced complex
singularities `[0:1:+/-i]` of an invariant degree-`d` curve each have
multiplicity `binomial(r,2)`.

## Result

The conjecture is false, including under a generic reading and inside the
strictly hyperbolic locus. Put `u=x+iy`, `v=x-iy`, and write `d=qn+r`,
`0<=r<n`. The invariant monomial support shows that every invariant form has
multiplicity at least `ceil(r/2)` at each forced point, and the unique
extremal monomial shows that this is the generic exact multiplicity.

More strongly, for every `q>=1` and `r>=3` there are normalized, strictly
hyperbolic, real `C_n`-invariant (indeed dihedral-invariant) forms having exact
multiplicity `ceil(r/2)` at both points. Since
`ceil(r/2) < binomial(r,2)` for every `r>=3`, this gives a family of full
counterexamples.

The smallest displayed instance uses `n=4`, `d=7`:

```text
H = t(t^2-uv)(t^2-4uv)(t^2-9uv),
G = t(uv^5+u^5v),
F_epsilon = H + epsilon G.
```

For all sufficiently small nonzero real `epsilon`, `F_epsilon` is strictly
hyperbolic and has multiplicity exactly `2` at each point, rather than the
conjectured `3`.

## Files

- `solution_packet.pdf`: complete counterexample, sharp support theorem, and review notes.
- `main.tex`: self-contained packet source.
- `source_paper.pdf`: the source paper PDF.
- `figures/open_problem_crop.png`: the conjecture and invariant monomial basis from source page 20.
- `code/verify_local_orders.py`: exact symbolic and finite support checks.
- `verification.md`: proof audit, novelty search bounds, and build verification.

## Human review recommendation

Check the one-line local-order formula `ord_[0:1:i] = d-k`, the maximization of
`k` under `j congruent k (mod n)`, and the compactness/IVT proof that a small
perturbation of the radial form remains strictly hyperbolic. These are the
three substantive steps; no external theorem is needed.
