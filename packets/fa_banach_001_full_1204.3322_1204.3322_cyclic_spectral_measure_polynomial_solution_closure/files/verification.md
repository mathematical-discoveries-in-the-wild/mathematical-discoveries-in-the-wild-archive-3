# Verification report

Candidate: full proof of Smith's conjecture in arXiv:1204.3322 that the closure of the parameters admitting a polynomially bounded solution equals the spectrum of the associated self-adjoint difference operator.

## Claim checked

Under the coefficient-growth and limit-point assumptions of Smith's Theorem 2.3,

`closure(E) = sigma(B)`.

For every fixed `epsilon > 0`, the canonical orthogonal-polynomial solution is `O((n+1)^(1/2+epsilon))` on a full spectral-measure subset dense in `sigma(B)`.

## Verdict

`likely valid` as a candidate full result. Mathematical-validity confidence is 97/100. Novelty confidence is low because all ingredients are classical and the downloadable source TeX contains a commented-out sketch toward the same conclusion, although the rendered paper leaves the equality as a conjecture.

## Adversarial proof audit

| Step | Status | Notes |
| --- | --- | --- |
| Sign change from `B` to the positive-off-diagonal Jacobi operator `J` | valid | The diagonal unitary `e_n -> (-1)^n e_n` changes the off-diagonal signs, preserves the spectrum, and fixes `e_0`. |
| Finitely supported vectors lie in the operator domain | valid | The Jacobi expression maps finite support to finite support; in the limit-point case its closure is the self-adjoint operator used by Smith. |
| Cyclicity of `e_0` | valid | The recurrence isolates `e_{n+1}` because every `a_n` is strictly positive. Induction gives `e_n=q_n(J)e_0`. |
| Scalar measure equals the orthogonality measure | valid | In the cyclic spectral representation, the recurrence polynomials send `1` to the coordinate basis; this is the standard Favard/Jacobi realization used in the source. |
| `supp(mu)=sigma(J)` | valid | Cyclicity makes `J` unitarily equivalent to multiplication by the independent variable on all of `L^2(mu)`, not merely a reducing subspace. Its spectrum is the closed support. |
| Tonelli interchange | valid | Every summand is nonnegative. The integral of the weighted series is `sum (n+1)^(-1-2epsilon)`, which is finite for every `epsilon>0`. |
| Pointwise polynomial bound | valid | If the weighted square sum is `S<infinity`, each term is at most `S`; taking square roots gives the exponent `1/2+epsilon`. |
| Full measure implies density | valid | Every open neighborhood of a support point has positive `mu` measure, while the complement of `E` has zero measure. |
| Reverse inclusion | source theorem | Smith's Theorem 2.3 gives `closure(E) subset sigma(B)` under exactly the stated growth and limit-point hypotheses. |
| Quantifier in `epsilon` | valid | The proof claims a full-measure set for each fixed `epsilon`; it does not require one common set for uncountably many `epsilon`. A single fixed `epsilon` already proves density of `E`. |

## Counterexample and edge-case checks

- Pure point spectrum: atoms are support points and the full-measure argument still works.
- Singular continuous spectrum: no absolute-continuity assumption is used.
- Unbounded coefficients/spectrum: the argument uses only the finite scalar measure of `e_0`, orthonormality, and local support.
- A parameter outside the spectrum could in principle admit other formal solutions, but Smith's Shnol theorem excludes polynomially bounded ones under the growth hypotheses.
- The canonical solution meets the source boundary condition `y_{-1}=0`; normalization `p_0=1` ensures it is nonzero.
- The exponent need not be uniform in `lambda`, and no such uniformity is claimed.
- If an off-diagonal coefficient vanished, `e_0` would no longer see every Jacobi block. The source assumes all `a_n>0`, so this obstruction is absent.
- Limit-circle extensions are outside the full theorem because the source's reverse inclusion is not supplied there.

## Literature and provenance boundary

- Exact source question: arXiv:1204.3322, PDF page 11, immediately after Theorem 3.2.
- Exact source inclusion: Theorem 2.3 on PDF page 5.
- Searches: run registry/solution/attempt/proof-gap indexes; exact arXiv id and title; author plus conjecture phrases; combinations of Jacobi, Shnol, polynomially bounded solution, closure `E`, spectral measure, and generalized eigenfunction.
- Search outcome: no later paper explicitly resolving the exact conjecture was found. General converse-Shnol results contain closely related ingredients. The search was bounded, not definitive.
- Source-archive caveat: the TeX source contains a commented-out proof sketch toward the equality. The rendered paper does not present it as a result, and the sketch does not explicitly justify the full-support step. The packet makes that step explicit and replaces the cited a.e. estimate with a direct Tonelli proof.

## Confidence and recommendation

Mathematical-validity confidence: 97/100.

Human-review recommendation: retain as a candidate full answer, with low novelty expectations. First verify that Smith's `mu` is the scalar measure of the cyclic vector `e_0`; then assess priority against the commented source sketch and standard converse-Shnol literature.

## Artifact verification

- `solution_packet.pdf`: five pages; all five final rendered pages were visually inspected at 135 dpi. No clipping, overlap, missing glyphs, or unreadable evidence text was found.
- Extracted-text smoke check: 7,729 characters. The cyclic-support lemma, Tonelli lemma, growth-free corollary, validity-confidence line, and references are present.
- LaTeX build: `latexmk` completed with resolved references and no warnings, overfull boxes, or underfull boxes in the final log.
- SHA-256 `solution_packet.pdf`: `7da80c533c95c160477617b730e2e39ad10d9f65abe6ed97eb945fe8bf6abd7a`.
- SHA-256 `source_paper.pdf`: `4be6ee234912b011024b18dbfc561c22cd57cf24576a18b9eb5f71896960c81e`.
- SHA-256 `figures/source_theorem_2_3.png`: `7a7f6401f2bda5f1b61d1e2ca3fdff82124c3a4a2c4729347a35aaafe11cbf33`.
- SHA-256 `figures/source_theorem_3_2_conjecture.png`: `9c6360937162e3c319a749ca1ac3bb689bc1df6e5589c5720fc24abd988a79ba`.
