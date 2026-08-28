# A one-column counterexample to the reverse Toeplitz-algebra implication

Status: `candidate counterexample (likely valid; human review requested)`

Source: David Békollè, Hugues Olivier Défo, and Edgar L. Tchoundja,
*Analysis of Toeplitz Operators with BMO^1_alpha operator-valued symbols on
ell^2-valued Bergman spaces*, arXiv:2510.19589 (2025), Section 13, page 41.

## Result

The answer to the paper's final question is **no**, for every complex dimension
`n >= 1` and every `alpha > -1`.

There is a bounded, strongly measurable symbol

\[
b:\mathbb B_n\longrightarrow
\mathcal L(\ell^2,\ell^1\cap\ell^2)
\]

such that the same is true of its Hilbert-space adjoint, so both symbols belong
to the required `BMO^1_alpha` spaces, and
`tilde b` is bounded. Moreover,

\[
T_bQ_d=0\quad(d\ge1),
\]

where `Q_d` is the projection onto coordinates after `d`. Nevertheless,

\[
\|Q_dT_b\|=1\quad(d\ge1),
\]

and consequently
\(T_b\notin\mathcal T_{L^\infty_{\mathrm{fin}}}\).

## Proof intuition

The source assumes decay only on the input-coordinate side. Use a symbol with
exactly one nonzero input column, making that decay automatic. Split the ball
into countably many disjoint angular sectors and send the first input
coordinate into a different output coordinate on each sector. Normalized
Bergman kernels concentrate at boundary points, so every sector supports a
scalar Toeplitz operator of norm one. Thus arbitrarily far output coordinates
remain visible with full norm. The finite-symbol Toeplitz algebra cannot have
this behavior: its elements are norm limits of operators with finite row and
column support, hence have two-sided coordinate-tail decay.

## Files

- `main.tex`: self-contained statement and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: page-41 crop of the exact open question.
- `VERIFICATION.md`: proof audit and novelty-search bounds.

No computational experiment is used; the argument is exact.

## Novelty status

A bounded search on 2026-08-26 used the exact arXiv id, exact title, the
finite-symbol Toeplitz-algebra notation, and close phrases from the final
question. It found the source, mirrors, and summaries, but no later paper
claiming an answer. This supports, but cannot guarantee, novelty.

## Human review recommendation

Review as a high-priority candidate counterexample. The key checks are the
vector-valued `BMO^1_alpha` membership of the bounded rank-one symbol and the
necessary two-sided tail property of
\(\mathcal T_{L^\infty_{\mathrm{fin}}}\).
