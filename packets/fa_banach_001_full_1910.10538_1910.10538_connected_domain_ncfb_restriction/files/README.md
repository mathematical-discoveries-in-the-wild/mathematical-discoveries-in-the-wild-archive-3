# Connected-domain construction in `NCFB_n(Omega)`

Status: **candidate full solution, likely valid, pending human review**.

Source: Chunlan Jiang, Kui Ji, and Jinsong Wu, *Similarity Invariants of Essentially normal Cowen-Douglas Operators and Chern Polynomials*, arXiv:1910.10538v1; Israel Journal of Mathematics 248 (2022), 229–270.

Source question: Section 6, PDF page 27, Question 1 asks whether one can construct an operator in `NCFB_n(Omega)` when `Omega` is connected.

## Result

Yes, for the bounded connected planar domains used throughout the source paper. Choose a disk `U` containing `Omega`, affinely transfer the paper’s strongly irreducible disk example to `NCFB_n(U)`, and restrict its Cowen–Douglas base from `U` to `Omega`. The totality axiom survives restriction by the identity theorem applied to local holomorphic frames. Every extra `CFB/NCFB` condition is operator- and block-intrinsic, so it is unchanged. Strong irreducibility is retained.

The construction does **not** force `spectrum(T)=closure(Omega)` or the other Fredholm-domain conclusions of source Theorem 3.10. It answers the literal construction/nonemptiness question, not that stronger extension, and does not answer Question 2.

## Packet contents

- `solution_packet.pdf`: review packet with the exact result and proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: real crop of the source question on PDF page 27.
- `tmp/`: LaTeX and rendering intermediates.

## Verification

The proof was checked axiom by axiom:

1. surjectivity and constant kernel dimension are inherited under domain restriction;
2. totality follows by analytic continuation of the frame coefficients;
3. affine scaling preserves essential normality, commutants, the triangular product relations, Property (H), and the Calkin-idempotent condition;
4. restricting the base changes none of the structural data;
5. the commutant is unchanged by a nonconstant affine transformation, preserving strong irreducibility.

Bounded novelty search (2026-08-27): run-wide indexes plus exact-question/title and close-keyword web/arXiv searches. The search found the 2022 journal version and later flag-class papers, but no explicit later answer or matching restriction argument. This is not a certification of novelty.

Human review should focus on the restriction lemma and on whether the intended reading of Question 1 includes the stronger spectral conclusions of Theorem 3.10 despite their absence from the question’s wording.
