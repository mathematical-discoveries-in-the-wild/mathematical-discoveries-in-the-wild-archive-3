# arXiv:1904.08923 — compact positive-definite spaces can have infinite magnitude

Status: `literature_already_answered (negative answer)`

Original source:

- Mark W. Meckes, *On the magnitude and intrinsic volumes of a convex body
  in Euclidean space*, arXiv:1904.08923.
- Exact location: arXiv PDF page 2, immediately after display (1).

Answering source:

- Tom Leinster and Mark W. Meckes, *Spaces of extremal magnitude*,
  arXiv:2112.12889.
- Exact locations: arXiv PDF page 2 (explicit identification of the old
  question) and Theorem 2.1 on page 3.

The source asks whether every compact positive-definite metric space has
finite magnitude.  The answering paper explicitly lists the source among the
places where this question was raised and constructs a compact metric space
of negative type whose magnitude is infinite after every positive rescaling.
Negative type is stronger than positive definiteness, so this is an exact
negative answer.

The compact status note also records a shorter self-contained witness:
`{0} union {(1/n)e_n}` in `ell_1`.  Its first `N` nonzero points have exact
magnitude

`1 + sum_{n=1}^N tanh(1/(2n))`,

which diverges.  This alternate derivation is not claimed as new; the target
was already settled by arXiv:2112.12889.

- Compact status note: `solution_packet.pdf`
- Original source PDF: `source_paper.pdf`
- Answering source PDF: `supporting_paper_2112.12889.pdf`
- Ledger: `runs/fa_banach_001/ledger/results/1904.08923_compact_pd_infinite_magnitude_answered_2112.12889.json`

