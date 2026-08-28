# Principal polynomial submodule projections need not almost commute

Status: `candidate_counterexample_likely_valid_needs_human_review`

## Source question

Ronald G. Douglas and Kai Wang, *Some Remarks On Essentially Normal
Submodules*, arXiv:1204.0620. At the bottom of printed page 7, continuing onto
page 8, the authors suggest that for polynomials `p,q` the orthogonal
projections onto the principal submodules `[p]` and `[q]` of the Hardy,
Bergman, or Drury-Arveson module on the unit ball might always almost commute.
Here “almost commute” means that their commutator is compact.

## Counterexample

In every complex dimension `n >= 3`, take

```text
p = z_1,        q = z_1 + z_2.
```

Let `P` and `Q` be the orthogonal projections onto `[p]` and `[q]`,
respectively, in any of the three modules named above. Then

```text
||[P,Q]|_{V_m}|| = 1/2     for every m >= 1,
```

where

```text
V_m = span{z_1 z_3^(m-1), z_2 z_3^(m-1)}.
```

The spaces `V_m` are mutually orthogonal, so `[P,Q]` is not compact.

## Mechanism

Write `E=I-P` and `F=I-Q` for the quotient projections. On the normalized
basis formed by the two displayed monomials, `E` projects onto the second
basis vector, while `F` projects onto their normalized difference. Hence

```text
E = [[0,0],[0,1]],
F = (1/2)[[1,-1],[-1,1]],
[E,F] = [[0,1/2],[-1/2,0]].
```

Since `[P,Q]=[E,F]`, the fixed norm `1/2` disproves compactness.

## Files

- `solution_packet.pdf`: exact source passage, theorem, and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: local copy of arXiv:1204.0620.
- `figures/open_problem_crop.png`: first part of the page-spanning passage.
- `figures/open_problem_continuation.png`: continuation on printed page 8.
- `verification.md`: proof and scope audit.

## Human review recommendation

Check the two elementary reducing-subspace assertions: within homogeneous
degree `m`, `[z_1]^perp` meets `V_m` in the second monomial, and
`[z_1+z_2]^perp` meets `V_m` in their difference. All three modules have
orthogonal monomials with equal norms after exchanging `z_1` and `z_2`, so the
same `2 x 2` block applies verbatim.

