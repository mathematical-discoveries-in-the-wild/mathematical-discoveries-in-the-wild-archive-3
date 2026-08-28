# Verification report

Status: candidate full solution, likely valid, pending human review.

## Exact target audit

- The source’s Section 6, Question 1 literally asks for an operator in `NCFB_n(Omega)` when `Omega` is connected.
- The source’s standing convention makes `Omega` a bounded open connected subset of the complex plane.
- The packet proves nonemptiness for every such `Omega` and retains strong irreducibility.
- It does not claim `spectrum(T)=closure(Omega)` or the other Fredholm-domain properties of source Theorem 3.10, because Question 1 does not state them.

## Proof audit

1. If `A` is in `B_m(U)` and `V` is a nonempty connected open subset of `U`, surjectivity and constant kernel dimension restrict pointwise.
2. If a vector is orthogonal to the fibers over `V`, pairing it with a local holomorphic frame gives scalar holomorphic functions vanishing on an open set.
3. A finite chain of overlapping frame neighborhoods along a path propagates this vanishing to every point of connected `U`.
4. Totality over `U` then forces the vector to be zero, proving totality over `V`.
5. For `T=bI+RA`, Cowen–Douglas membership transfers under `w=b+Rz`, while `[T*,T]=R^2[A*,A]`.
6. The same block decomposition works. An off-diagonal product coefficient rescales by `R^(1-(j-k))`, the adjacent Rosenblum map rescales by the nonzero scalar `R`, and the idempotents are unchanged.
7. The commutants of `A` and `bI+RA` coincide, so strong irreducibility is preserved.
8. Restricting from a containing disk to `Omega` changes only the Cowen–Douglas base; all remaining `CFB/NCFB` data are unchanged.

No numerical computation is needed or used.

## Source and visual verification

- Original arXiv PDF stored as `source_paper.pdf`.
- The question is on PDF page 27.
- `figures/open_problem_crop.png` is a real, full-readable-width crop showing both numbered questions.
- The four-page final PDF was rendered page by page. All text, formulas, the evidence crop, page numbers, and references are legible; no clipping, overlap, missing glyphs, or LaTeX warnings remain.

## Bounded novelty check

Checked through 27 August 2026:

- run-wide registry, solutions, attempts, and proof-gap indexes for arXiv:1910.10538, the exact title, `NCFB_n`, and connected-domain Cowen–Douglas terms;
- exact-question and exact-title web searches;
- close web/arXiv queries for `NCFB Cowen Douglas connected` and `Cowen-Douglas NCFB connected domain`.

The search found the 2022 journal publication and later work on Cowen–Douglas flag classes, but no explicit answer to Question 1 and no matching restriction argument. Novelty remains plausible rather than certified.

## Human-review focus

Review the analytic-continuation chain in the restriction lemma, the scaling of the `CFB_n` product relation and Property (H), and the intended scope of the literal Question 1. If the source authors intended the unstated stronger spectral analogue of Theorem 3.10, the packet should be reclassified as a full answer to the literal question but only a partial result toward that stronger interpretation.
