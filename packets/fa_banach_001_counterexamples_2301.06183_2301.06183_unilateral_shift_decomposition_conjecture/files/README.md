# Counterexample Packet: The Unilateral Shift Blocks the Nontrivial Decomposition Conjecture

Run: `fa_banach_001`  
Agent: `agent_lane_09`  
Model: `GPT5.6`  
Result type: `candidate_counterexample_likely_valid_scoped`

## Source problem

- Jahangir Cheshmavar, Ayyaneh Dallaki, and Javad Baradaran,
  *On abstract results of operator representation of frames in Hilbert
  spaces*, arXiv:2301.06183v1; Journal of Pseudo-Differential Operators and
  Applications 14 (2023), article 30, DOI 10.1007/s11868-023-00524-8.
- Source location: page 11, final conjecture.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

The paper defines `E(H)` as the bounded operators `T` for which
`{T^k phi}_{k>=0}` is a frame for `H` for some `phi`.  It then conjectures
that `H` decomposes as a countable Hilbert direct sum of `T`-invariant
subspaces, each itself possessing a frame orbit under `T`.

## Resolution and scope

There are two readings, and both are completely decided.

1. If zero summands are permitted, the statement is immediate from the
   definition of `E(H)`: take `H_1=H` and `H_n={0}` thereafter.  Under the
   usual convention, the zero orbit is a frame for the zero space.
2. If the conjecture is meant nontrivially, with at least two—and in
   particular countably many—nonzero summands, it is false.  The
   multiplicity-one unilateral shift `S` on `ell_2(N_0)` belongs to `E(H)`
   because `{S^k e_0}` is the standard orthonormal basis, but `S` has no
   nontrivial reducing subspace.  An orthogonal direct sum of invariant
   summands would make every summand reducing.

The obstruction even rules out bounded nonorthogonal topological direct sums:
the commutant of the unilateral shift has no nontrivial idempotents.

## Verification status

- Membership `S in E(H)` is exact: its distinguished orbit is an orthonormal
  basis.
- The reducing-subspace obstruction has a three-line basis proof using
  `ker(S*)=span{e_0}`.
- The stronger topological-direct-sum statement is proved via the elementary
  Hardy-space multiplier description of operators commuting with `M_z`.
- `code/verify_shift_obstruction.py` checks the finite truncated-shift analogue
  in dimensions 2 through 40: every orbit Gram matrix is the identity and the
  joint commutant of the shift and its adjoint is one-dimensional.  This is
  corroborative and not used as proof.

## Novelty check

On 2026-08-27 the four run indexes were searched for arXiv:2301.06183, its
title, unilateral-shift frame orbits, invariant-summand decompositions, and
reducing-subspace variants.  Bounded exact-phrase, arXiv, title, and citation
searches found the source paper, the related arXiv:2212.01921 and
arXiv:2505.19303 papers, and one 2025 article citing the source (DOI
10.1007/s11785-025-01839-8).  No exact answer to the final conjecture surfaced;
the citing article's available metadata and abstract concern other
characterizations.  Novelty is plausible, not certified.

## Files

- `main.tex`: expert-facing convention audit and counterexample.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: page-11 evidence crop.
- `code/verify_shift_obstruction.py`: finite-matrix sanity checks.
- `code/crop_source_page.py`: reproducible crop.
- `tmp/`: build and rendering intermediates.

## Human-review recommendation

High-priority but quick review.  Confirm that the source intends all summands
to be nonzero.  Under that intended reading the unilateral-shift counterexample
is complete.  If zero summands are allowed, record instead that the printed
conjecture is tautological.
