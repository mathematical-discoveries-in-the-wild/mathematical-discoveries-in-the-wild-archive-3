# Minimal unitary realizations can agree locally and disagree globally

Status: candidate full counterexample, likely valid, human review required.

Source: Ali Karoobi, Robert T. W. Martin, and Maximilian Tornes,
“Operator realizations about a matrix-centre,” arXiv:2509.08921,
Remark 2.4 on PDF page 8.

This packet fully answers the existence question in Remark 2.4. Choose a
measurable partition of the unit circle

    T = E disjoint union F

such that both pieces have positive Lebesgue measure in every nonempty open
arc. Let U_G be multiplication by zeta on L2(G) and consider

    (U_F, b_F = conjugate(zeta), c_F = 1),
    (U_E, b_E = -conjugate(zeta), c_E = 1).

Both operators are unitary with spectrum T. Hardy boundary uniqueness makes
analytic and anti-analytic polynomials dense on each proper measurable piece,
so both realizations are minimal. Their nonnegative moments agree because

    integral_F zeta^(n+1) dm = - integral_E zeta^(n+1) dm,   n >= 0.

Consequently the realizations are analytically equivalent near 0 at every
matrix level. Their common scalar invertibility domain is
`{|z|<1} union {|z|>1}`. On the exterior component their transfer functions
differ by

    integral_T zeta/(1-z zeta) dm = -1/z.

Files:

- `solution_packet.pdf` — review-ready full proof packet
- `main.tex` — packet source
- `source_paper.pdf` — original arXiv paper
- `figures/open_problem_crop.png` — source Example 2.3 and Remark 2.4
- `VERIFICATION.md` — independent proof audit and bounded novelty record

The result answers exactly the construction requested in Remark 2.4. It does
not answer the separate compact matrix-centre realization question later in
the paper.
