# Polynomially bounded solutions are dense in the Jacobi spectrum

Status: `candidate_full_solution_likely_valid`

This packet answers the conjecture stated after Theorem 3.2 of Dale T. Smith's arXiv:1204.3322, *Spectral Analysis of a Class of Self-Adjoint Difference Equations*.

Under the coefficient-growth and limit-point hypotheses used in Smith's Theorem 2.3, let

`E = {lambda in R : the difference equation has a polynomially bounded solution}`.

Then

`closure(E) = sigma(B)`.

The missing inclusion is a spectral-measure argument. The first Jacobi basis vector is cyclic because every off-diagonal coefficient is nonzero, so its scalar spectral measure has support exactly `sigma(B)`. Meanwhile, orthonormality of the recurrence polynomials and Tonelli's theorem imply that, for every `epsilon > 0`, the canonical polynomial solution is `O((n+1)^(1/2+epsilon))` for spectral-measure almost every `lambda`. Thus `E` has full spectral measure and must be dense in its support. Smith's Theorem 2.3 supplies the reverse inclusion.

The density half is stronger than the conjecture: it holds for every self-adjoint half-line Jacobi operator with nonzero off-diagonal coefficients, without Smith's coefficient-growth assumptions. Those assumptions are needed only for the Shnol-type reverse inclusion.

The mathematical ingredients are classical and the arXiv source archive contains a commented-out sketch pointing toward the same contradiction, although the rendered paper leaves the statement as a conjecture and the sketch does not state the cyclic-support bridge. The packet is therefore a candidate full answer with high validity confidence but deliberately low novelty confidence.

## Files

- `solution_packet.pdf`: source evidence, theorem, full proof, edge cases, and literature boundary.
- `main.tex`: packet source.
- `source_paper.pdf`: local copy of arXiv:1204.3322.
- `figures/source_theorem_2_3.png`: source crop showing the proved inclusion.
- `figures/source_theorem_3_2_conjecture.png`: source crop showing the a.e. bound and conjecture.
- `verification.md`: adversarial proof and artifact audit.
