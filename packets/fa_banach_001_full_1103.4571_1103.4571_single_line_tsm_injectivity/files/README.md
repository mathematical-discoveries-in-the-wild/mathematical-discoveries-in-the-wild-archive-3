# Full solution packet: a single line determines twisted spherical means

Status: `candidate_full_likely_valid`

## Source problem

R. K. Srivastava, *Coxeter system of lines are sets of injectivity for the
twisted spherical means on C*, arXiv:1103.4571. On page 14 the paper conjectures
injectivity for Coxeter systems with an odd number of lines, after proving the
even case for `L^p(C)`, `1 <= p <= 2`.

The reserved queue source arXiv:1204.3076 supplies the adjacent real-analytic
spectral-projection framework and is retained as a supporting paper.

## Result

The packet proves the stronger theorem that **one line through the origin** is
already a set of injectivity for twisted spherical means on `L^p(C)` for every
`1 <= p <= 2`. Every odd Coxeter system contains such a line, so the source
conjecture follows immediately.

The new step is an injectivity theorem for restriction of a fixed special
Hermite/Landau eigenspace to the real axis. The creation-operator representation
turns axis vanishing into a normal-ordered ODE. After Gaussian conjugation, its
characteristic polynomial is `2^{-k} i^k H_k(i s)`. Its roots are distinct and
imaginary, so the only formal solutions are finite exponential sums; Fock
integrability excludes every nonzero such sum.

## Verification

`code/check_hermite_axis_ode.py` checks the normal-order and Hermite-polynomial
identities exactly for levels 0 through 12. The proof itself is symbolic for all
levels and does not rely on finite computation.

The bounded novelty check searched the four cheap run indexes, the local parsed
arXiv corpus, and arXiv web results for the exact paper/title, odd-Coxeter and
single-line terminology, and Landau/polyanalytic-Fock reformulations. No later
paper claiming this result was found as of 2026-08-26. This is not an exhaustive
publication search.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: arXiv:1103.4571 source PDF.
- `supporting_paper_1204.3076.pdf`: adjacent spectral-projection paper.
- `figures/open_problem_crop.png`: source page 14 evidence.
- `code/check_hermite_axis_ode.py`: exact finite identity checker.
- `tmp/`: compilation and rendering intermediates.

## Human review focus

Check the twist convention in the factorization of the special Hermite operator,
the normal-order generating function, and strong `L^1` reconstruction by the
special-Hermite heat kernel. The result does not address arbitrary real-analytic
curves or `p > 2`.
