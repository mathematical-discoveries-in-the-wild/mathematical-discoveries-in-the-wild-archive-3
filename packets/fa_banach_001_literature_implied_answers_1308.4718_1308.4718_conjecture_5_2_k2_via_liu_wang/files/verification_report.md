# Verification Report

## Claim checked

The `k=2` case of arXiv:1308.4718v1, Conjecture 5.2, is implied by
Liu--Wang (2016), Lemma 2.4.

## Verdict

`verified_direct_transpose_identification`

## Checks

| Check | Status | Notes |
| --- | --- | --- |
| Source statement | verified | arXiv:1308.4718v1, PDF page 16, defines `tau` for `n x (n+k)` matrices and states Conjecture 5.2. |
| Later theorem | verified | Liu--Wang (2016), Lemma 2.4, article page 4, gives `C/n^(3/2)` for `(n+2) x n` matrices with row norms at most one. |
| Identification | verified | Set `A=F^T`; row/column norm hypotheses and selected submatrices correspond, and singular values are transpose-invariant. |
| Scope | verified | Only `k=2` is claimed; arbitrary fixed `k` and Conjecture 5.1 remain outside the packet. |
| Provenance | verified | Later theorem proves the identical inequality but does not use the source conjecture label; literature-implied classification is conservative. |
| Supporting context | verified | Liu (2024), Theorem 2.7, proves the sharp planar two-column bound and cites both Balan--Wang and Liu--Wang. |
| PDF build | passed | `latexmk` completed in two passes with resolved references, no overfull boxes, and a two-page final PDF. |
| Visual QA | passed | Both pages were rendered at 160 DPI and inspected at original resolution; headings, formulas, references, margins, and page breaks are legible with no clipping or overlap. |

## Search bounds

Searched the run's four cheap indexes for `1308.4718`, the paper title,
`phaseless reconstruction`, `phase retrieval`, `robustness`, and
`invertibility`; no exact existing run record was found.  External
primary-source searches covered the exact paper title and conjecture
label, the matrix formula, works citing Balan--Wang, and later papers on
minimal smallest singular values.  The decisive items were Liu--Wang
(2016) and Liu (2024).  No source located in this bounded search claims
the full arbitrary-`k` conjecture.
