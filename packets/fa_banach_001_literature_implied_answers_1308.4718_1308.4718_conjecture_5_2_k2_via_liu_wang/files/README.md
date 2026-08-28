# Conjecture 5.2: the `k=2` subcase is in later literature

Status: `literature_implied_answer_partial_subcase`

Source: Radu Balan and Yang Wang, *Invertibility and Robustness of
Phaseless Reconstruction*, arXiv:1308.4718v1, Conjecture 5.2 on PDF page
16.

Supporting result: Yang Liu and Yang Wang, *On the Decay of the Smallest
Singular Value of Submatrices of Rectangular Matrices*, Asian-European
Journal of Mathematics 9 (2016), article 1650075,
DOI `10.1142/S1793557116500753`, Lemma 2.4 on article page 4.

## Identification

The source considers an `n x (n+k)` matrix `F` with column norms at most
one and

```text
tau = min_{|S|=n} sigma_n(F_S).
```

Conjecture 5.2 predicts `tau <= C(k) n^{-(k-1/2)}`.  For `k=2`, transpose
`F` to an `(n+2) x n` matrix `A=F^T`.  Selecting `n` columns of `F` is
the same as selecting the corresponding `n` rows of `A`, and
`sigma_n(F_S)=sigma_n(A_S)` because singular values are invariant under
transpose.

Liu--Wang's Lemma 2.4 proves for every such `(n+2) x n` matrix that

```text
min_{|S|=n} sigma_n(A_S) <= C n^(-3/2).
```

This is exactly Conjecture 5.2 for `k=2`.  The relation is recorded as
literature-implied because the later paper does not label the theorem as
an answer to “Conjecture 5.2,” although Yang Wang coauthored both papers
and the matrix formulations agree after transposition.

## Scope

This packet does not claim the general fixed-`k` conjecture.  The 2016
paper proves the base cases and develops a kernel-duality reduction; its
`n+3 by n` analysis leads to a planar Heilbronn-type point-line incidence
problem and does not settle all `k`.  Conjecture 5.1 is also outside this
packet.

The later open-access 2024 paper by Yang Liu restates the connection to
the source, cites Balan--Wang and Liu--Wang, and proves the sharp planar
two-column extremal bound used on the dual side.  It is included as a
corroborating local PDF.  The 2016 PDF was publicly readable through the
ResearchGate full-text view during verification, but its direct PDF URL
returned HTTP 403, so no local copy is included.

## Files

- `main.tex`: compact theorem-to-theorem identification.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1308.4718v1 source PDF.
- `supporting_paper_2024_liu.pdf`: open-access corroborating paper.
- `verification_report.md`: scope, source, build, and visual checks.

