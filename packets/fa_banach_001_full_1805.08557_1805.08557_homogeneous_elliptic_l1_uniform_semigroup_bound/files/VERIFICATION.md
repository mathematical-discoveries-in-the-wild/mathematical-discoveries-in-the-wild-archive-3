# Verification record

## Mathematical audit

1. In the source's Section 4, the operator is explicitly the
   constant-coefficient Fourier multiplier `H=P(D)`.
2. In the homogeneous elliptic subsection, `P` is a real homogeneous
   polynomial of even order `m` satisfying Assumption A3, hence
   `P(xi) >= c |xi|^m`.
3. Every derivative of `exp(-P)` is a polynomial times `exp(-P)`; ellipticity
   therefore implies `exp(-P)` is Schwartz. Its inverse Fourier transform `k`
   is Schwartz and belongs to L1.
4. Homogeneity gives the exact identity
   `k_t(x)=t^(-d/m) k(t^(-1/m)x)`, so `||k_t||_1=||k||_1` for every `t>0`.
5. Fourier diagonalization and Young's inequality give
   `||e^(-tP(D))u||_1 <= ||k||_1 ||u||_1` first on Schwartz functions and then
   on all of L1.
6. The multiplier identity gives the semigroup law, while `integral k=1` and
   the exact dilations make `(k_t)` a bounded approximate identity. Thus the
   L1 extension is strongly continuous at zero.
7. Choosing `beta=0` and
   `C_2(u)=max(||k||_1^2-1,0)||u||_1^2` matches every quantifier in Question
   4.5. The endpoint `t=0` is checked directly.
8. Rearranging the paper's homogeneous Nash inequality and integrating
   `d/dt ||T_tu||_2^2=-2 E(T_tu)` yields `O(t^(-d/m))`, as predicted by the
   source for `beta<=0`.

Verdict: the candidate is a full affirmative answer in the exact
constant-coefficient context of the source. Mathematical confidence is high.

## Scope and possible semantic failure mode

The proof does not cover arbitrary variable-coefficient elliptic operators.
The source question occurs inside a section that begins by fixing
`H=P(D)` with constant coefficients, and its homogeneous subsection writes
the symbol as a homogeneous polynomial with real constant coefficients. A
reviewer should verify that this surrounding context is the intended scope;
the literal proof is complete under it.

## Novelty check

A bounded search through 2026-08-26 covered:

- the run's registry, solution, attempt, and proof-gap indexes;
- arXiv:1805.08557 and the exact wording of Question 4.5;
- primary-source searches combining homogeneous elliptic operators, heat
  kernels, L1 bounds, and semigroups.

No later paper explicitly presenting itself as an answer to Question 4.5 was
found. Uniform L1 boundedness here follows from classical kernel scaling, so
this is not proof of historical priority. Novelty confidence is moderate; the
identification appears new to this run.

## Source and artifact checks

- `source_paper.pdf` is arXiv:1805.08557v5, 15 A4 pages.
- The complete question and the source's decay consequence occur on PDF page
  14.
- Page 14 was rendered at 180 dpi; the crop retains the full page width and
  was visually checked for completeness and readability.
- The final packet was compiled into `tmp/`, copied to
  `solution_packet.pdf`, rendered page by page, and visually checked.
- The LaTeX log was checked for undefined references, missing citations,
  overfull boxes, and fatal errors.

No numerical or symbolic computation is part of the proof.
