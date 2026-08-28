# Verification report

Status: `candidate_full_result_likely_valid`; expert review is recommended.

## Source and provenance

- Open question verified in Remark 5.6, PDF page 21, of arXiv:2007.02324.
- The crop in `figures/open_problem_crop.png` is rendered directly from the
  locally stored `source_paper.pdf` and contains the complete question.
- The order-isomorphism and normality input was checked against Lemma 3.1 of
  arXiv:1907.06452, also stored locally.
- The sum-space classification is Theorem 4.2 and its positive corollary in
  arXiv:2007.02324.

## Mathematical checks

1. If one total trace is in `(1,2)`, inversion is legitimate because the cited
   lemma makes the inverse positive and normal.
2. The no-order-unit argument in infinite trace uses spectral projections of
   `U(1)` and a summable orthogonal family of finite projections. Compression
   gives the explicit contradiction `q_k <= (c/k) q_k` for `k>c`.
3. The other finite total cannot be at most one: two distinct trace-one
   projections on the first side would both map to the identity by the source
   paper's extreme-point characterization.
4. For finite trace, the intersection norm and operator norm are equivalent,
   so the normal order isomorphism has an invertible normal preadjoint.
5. The norm induced on normal functionals by the intersection norm is exactly
   the `L1 + Linfinity` sum norm. Taking suprema over the two unit balls proves
   that the preadjoint is a positive surjective sum-space isometry.
6. The source sum-space theorem therefore gives a trace-preserving Jordan
   star-isomorphism. The trace/Jordan-product identity identifies its inverse
   with the original map.

No numerical or symbolic experiments are needed or claimed as evidence.

## Novelty bounds

Bounded searches through 2026-08-27 used the exact arXiv id, exact title,
authors, the quoted open-problem phrase, combinations of “positive surjective
isometry”, “L1 intersection Linfinity”, and “trace between 1 and 2”, plus a
forward-citation check. They found the source, its Glasgow Mathematical
Journal version, and an unrelated paper citing the source, but no later paper
claiming to solve this intermediate-trace problem. This is not an exhaustive
novelty guarantee.

## Human-review focus

The highest-value review point is the normal-duality step: confirm the stated
polar identity between the intersection norm on the finite algebra and the
sum norm on its normal predual. The remaining steps are short consequences of
the two cited source results and elementary trace arguments.

## Rendering

The final PDF is compiled with `latexmk`; build warnings and every rendered
page are checked before handoff.

