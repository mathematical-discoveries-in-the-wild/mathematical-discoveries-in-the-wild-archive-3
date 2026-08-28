# Generic rank-three Cauchy-dual non-subnormality

Status: `candidate_partial_result_likely_valid`

Source: M. N. Khasnis and V. M. Sholapurkar, *Cyclic Analytic
2-isometry of Finite Rank and Cauchy Dual Subnormality Problem*,
arXiv:2309.03588v2, Section 1.2, Problem 1 (PDF p. 5).

## Claimed contribution

For measures supported at exactly three points, normalize rotation and cyclic
order as

`mu = c1 delta_1 + c2 delta_exp(i theta2) + c3 delta_exp(i theta3)`

with `0 < theta2 < theta3 < 2 pi` and all masses positive. The packet proves:

- the subnormal Cauchy-dual locus is contained in the union of two proper
  real-analytic zero sets;
- whenever the three outer roots are simple, subnormality is equivalent to
  pairwise orthogonality of their numerator-kernel evaluation vectors, with
  no pole-product distinctness assumption;
- consequently it is Lebesgue-null and nowhere dense in every rank-three
  angle-mass chart;
- an open dense set, and almost every rank-three measure, has a non-subnormal
  Cauchy dual;
- for every positive common mass, non-subnormality holds throughout a full
  neighborhood of the equal-mass equilateral measure, allowing arbitrary
  nearby support points and arbitrary nearby masses.

This is a full-dimensional partial answer, not a complete classification. The
proper real-analytic exceptional set remains unresolved.

## Proof mechanism

Theorem 2.1 of Chavan--Ghara--Reza supplies a positive matrix for every
complete-monotonicity order. Compressing it through the inverse outer-root
Vandermonde matrix gives entries
`c_rt (1-u_r conjugate(u_t))^ell`. A two-by-two principal minor cannot remain
positive for all `ell` when `r != t` and `c_rt != 0`, because
`|1-u_r conjugate(u_t)|^2` strictly exceeds
`(1-|u_r|^2)(1-|u_t|^2)`. Thus simple outer roots force all cross-Gram values
to vanish under subnormality; the converse is the source's Corollary 2.3.

Consequently the two analytic obstructions can be taken to be the ordinary
outer-root discriminant and an iterated resultant equal to the product of all
nine numerator Gram values.

Both functions depend real-analytically on support angles and masses. At the
equal-mass equilateral model the outer roots are simple and the resultant is
nonzero.
Proper real-analytic zero sets are null and nowhere dense.

The neighborhood theorem separately uses the grouped forbidden-atom measure:
within either equilateral off-diagonal cluster, all three base residues are
the same nonzero number, so no collision group can cancel after a sufficiently
small perturbation.

## Packet contents

- `solution_packet.pdf`: expert-facing proof and review packet.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2309.03588v2.
- `supporting_paper_2103.10059.pdf`: rational-symbol and forbidden-atom
  criteria used in the proof.
- `figures/open_problem_crop.png`: real source-PDF crop of Problem 1.
- `code/verify_rank_three.py`: independent numerical reconstruction.
- `VERIFIER_REPORT.md`: adversarial step-by-step verification.
- `tmp/`: LaTeX and rendering intermediates.

## Reproduce the numerical sanity check

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2309.03588_generic_rank_three_nonsubnormality/code/verify_rank_three.py
```

## Human-review focus

Check the real-analytic outer-factor dependence, the Vandermonde compression,
the large-order two-by-two minor argument, and the resultant reduction. The
bounded arXiv novelty audit through 2026-08-26 found no generic, almost-every,
or perturbative rank-three theorem.
