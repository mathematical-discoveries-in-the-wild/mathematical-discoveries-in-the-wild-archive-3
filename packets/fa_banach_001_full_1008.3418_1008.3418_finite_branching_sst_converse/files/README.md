# Full Solution Packet: The Converse for Spherically Symmetric Trees

Run: `fa_banach_001`  
Agent: `agent_lane_09`  
Model: `GPT5.6`  
Result type: `full_solution_likely_valid`

## Source problem

- Elena Caffarelli, Ian Doust, and Anthony Weston, *Metric trees of
  generalized roundness one*, arXiv:1008.3418v2, Aequationes Mathematicae 83
  (2012), DOI 10.1007/s00010-011-0108-8.
- Source location: page 5, immediately before Section 3, after Theorem 2.2.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

Theorem 2.2 proves that a countable spherically symmetric tree whose downward
degree sequence has infinitely many entries greater than one has generalized
roundness one.  The authors ask whether the converse is true.

## Claimed answer

Yes.  More generally, the geometric realization of any tree made from only
finitely many finite intervals and half-lines has generalized roundness
strictly greater than one.  A countable SST with only finitely many branching
levels is a subset of such a finite-topological tree, so its generalized
roundness is greater than one.  Together with Theorem 2.2, this gives the exact
equivalence

```text
gamma(T)=1  iff  infinitely many downward degrees d_j exceed 1.
```

## Proof mechanism

For a zero-mass finite configuration, introduce the cumulative flow on every
open edge and integrate the distance-power form twice.  The within-edge terms
are positive Riesz energies with kernel `|s-t|^{-alpha}`.  Every between-edge
term is, up to sign and reversal of coordinates, a shifted Hankel form with
kernel `(s+t+c)^{-alpha}`.

A logarithmic change of variables diagonalizes both forms.  The exact ratio of
their Fourier multipliers is

```text
cos(pi*alpha/2) / cosh(pi*xi).
```

Thus a cross-edge form is at most `cos(pi*alpha/2)` times the geometric mean
of the two diagonal energies.  There are only finitely many open edges, and
this constant tends to zero as `p=2-alpha` decreases to one.  Elementary
diagonal dominance then proves `p`-negative type for some `p>1`.

## Verification status

- The flow integration identity includes atoms at branch vertices through the
  Kirchhoff balance relation.
- The singular second derivative is locally integrable because `0<alpha<1`.
- The Mellin/Fourier multiplier calculation is written out from beta and gamma
  identities; no sharp-transform theorem is assumed.
- The proof treats finite intervals and half-lines uniformly, including
  shifted cross-edge kernels and arbitrary edge orientations.
- `code/verify_finite_edge_bound.py` checks the exact multiplier ratio on
  20,005 frequency/exponent points, independently compares the beta/gamma
  formulas at 25 points, and checks the resulting negative-type inequality on
  2,400 random weighted finite trees.  This is a sanity check, not proof.

## Novelty check

On 2026-08-27 the four run indexes were searched for arXiv:1008.3418, the
paper title, the exact converse, finite-ended/finitely-branching tree phrases,
and generalized-roundness/negative-type variants.  Bounded arXiv/web searches
used the same terms and inspected the later related papers arXiv:1608.03699,
arXiv:0901.0695, and arXiv:1108.0451.  They found the original question and
adjacent results, but no exact resolution of this converse or the finite-edge
theorem used here.  Novelty is plausible, not certified.

## Files

- `main.tex`: expert-facing proof.
- `solution_packet.pdf`: rendered solution packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: page-5 evidence crop.
- `code/verify_finite_edge_bound.py`: numerical sanity checks.
- `code/crop_source_page.py`: reproducible full-width crop.
- `tmp/`: LaTeX and rendering intermediates.

## Human-review recommendation

High-priority expert review.  Check especially the graph-wide integration by
parts identity and the bookkeeping of ordered cross-edge pairs.  The analytic
Hankel/Riesz estimate and the finite-edge diagonal-dominance step are explicit,
and no conditional lemma remains.
