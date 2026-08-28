# Candidate partial result: a sharper bound for the minimal faithful V4 representation

Status: `candidate partial` (likely valid; human review recommended)

Source: Ben Blum-Smith, Harm Derksen, Dustin G. Mixon, Yousef Qaddura,
and Brantley Vose, *Estimating the Euclidean distortion of an orbit space*,
arXiv:2506.04425v1. The open question appears in Section 4.2, page 43.

## Contribution

Let

\[
G=\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}\leq O(3),
\]

the multiplicity-free sum of the three nontrivial real characters of
\(C_2\times C_2\). The source paper gives
\(\sqrt 2\leq c_2(\mathbb R^3/G)\leq2\). This packet proves the improved bound

\[
\sqrt2\leq c_2(\mathbb R^3/G)\leq\sqrt{2+\sqrt2}.
\]

The embedding sends an orbit to its ordered absolute coordinates together
with the parity of the signs times the distance to the boundary of the
positive orthant. The proof computes the quotient metric exactly and proves
sharp scalar inequalities for this embedding.

Among the one-parameter family obtained by scaling the signed boundary
coordinate, the displayed constant is optimal.

## Scope

This does **not** compute the contortion \(\Upsilon(C_2\times C_2)\): the
contortion is a supremum over all finite-dimensional representations, and the
exact distortion of this particular quotient is also not determined. It is a
strict improvement for the most natural minimal faithful representation.

The bounded novelty search used the exact phrases `Euclidean contortion`,
`Upsilon(C_4)`, and `C_2 times C_2`, plus the title and arXiv id. No later
resolution or occurrence of this constant for the target was found as of
2026-08-27. Novelty confidence is moderate, not definitive.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2506.04425v1.
- `figures/open_problem_crop.png`: source-page evidence.
- `code/verify_bound.py`: randomized and extremal numerical checks (not part
  of the proof).

Recommended verifier focus: check the normalized scalar inequality in Lemma 2
and the cross-sheet quotient-distance formula.
