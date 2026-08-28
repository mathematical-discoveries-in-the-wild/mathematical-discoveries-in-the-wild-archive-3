# arXiv:2007.02324 — duality closes the intermediate-trace gap

Status: `candidate_full_result_likely_valid` (human review pending).

Pierre de Jager and Jurie Conradie ask in Remark 5.6 of *Extreme point
methods in the study of isometries on certain non-commutative spaces* whether
positive surjective isometries of `L1 cap Linfinity` can be described when one
trace of the identity lies strictly between 1 and 2.

This packet proves that the answer is unchanged: every such isometry is a
trace-preserving Jordan star-isomorphism. The key is to avoid the unavailable
pair of orthogonal trace-one projections. The finite-side identity is an order
unit, so its image forces the other trace to be finite. Normal duality then
turns the intersection-space isometry into a positive sum-space isometry, to
which the source paper's earlier classification applies.

Files:

- `solution_packet.pdf`: complete proof and review notes.
- `source_paper.pdf`: arXiv:2007.02324.
- `supporting_paper_1907.06452.pdf`: the order-isomorphism/normality lemma used
  by the proof.
- `figures/open_problem_crop.png`: direct crop of Remark 5.6 from source PDF
  page 21.
- `VERIFICATION.md`: mathematical, provenance, and rendering checks.

No computational code is used. The proof is purely functional-analytic.

