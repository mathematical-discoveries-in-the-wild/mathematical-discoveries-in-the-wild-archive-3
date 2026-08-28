# Solel's TRO-range conjecture in arXiv:0301298

Status: `literature_already_answered_negative`

Original source:

- Aristides Katavolos and Vern I. Paulsen, *On the ranges of bimodule
  projections*, arXiv:math/0301298; *Canadian Mathematical Bulletin* 48
  (2005), 97--111.
- Exact location: arXiv PDF page 2. The paper records Solel's conjecture that
  the range of every contractive idempotent MASA-bimodule map on `B(H)` is a
  sub-TRO even without weak-star continuity. It repeats the conjecture on
  PDF page 9.

Answering source:

- Vern I. Paulsen, *Equivariant Maps and Bimodule Projections*,
  arXiv:math/0510641; *Journal of Functional Analysis* 240 (2006), 495--507.
- Exact locations: the abstract and introduction explicitly announce the
  counterexample; Theorem 2.15 on PDF page 10 constructs the equivariant
  projection; Theorem 3.1 and Corollary 3.2 on PDF pages 12--13 lift it to the
  required MASA-bimodule projection.

Paulsen first constructs a unital completely positive, idempotent,
`Z`-equivariant map on `ell_infinity(Z)` whose range is not a C-star
subalgebra. Theorem 3.1 transfers such maps to unital completely positive
`L_infinity(T)`-bimodule maps on `B(L_2(T))`, preserving idempotence.
Corollary 3.2 concludes that the lifted range is not a C-star subalgebra.

This is exactly a counterexample to the source conjecture. A unital
completely positive map is contractive. Its idempotent range contains the
identity; if that range were a TRO, then for range elements `A,B`, the ternary
products `A I* B = AB` and `I A* I = A*` would make it a C-star subalgebra,
contradicting Corollary 3.2. The example is non-weak-star-continuous, so it
does not conflict with Solel's positive theorem in the normal case.

Scope: this packet answers only the TRO-range conjecture. It does not claim
to settle the separate questions in arXiv:0301298 about the norm gap for all
bounded bimodule projections, extending the symbol calculus, or identifying
the kernels of the restriction maps with the closed commutator ideal.

Search evidence: the four run indexes were checked for both arXiv ids, the
exact titles, and the MASA/TRO language. No existing run packet was found.
A current exact-phrase search located arXiv:math/0510641, whose abstract
explicitly identifies itself as a counterexample to the source conjecture.
This is an exact later-literature answer, not a new result of this run.

- Compact status note: `solution_packet.pdf`
- Original source PDF: `source_paper.pdf`
- Answering source PDF: `supporting_paper_0510641.pdf`
- Ledger:
  `runs/fa_banach_001/ledger/results/0301298_solel_tro_conjecture_answered_by_0510641.json`
