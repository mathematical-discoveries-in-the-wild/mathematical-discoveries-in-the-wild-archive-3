# Essential numerical range characterization of unitary-similar L-asymptotic limits

Status: `candidate_full_separable_solution_likely_valid`

This packet answers the open problem stated after Theorem 4.2 of arXiv:1505.07205 in the standard separable infinite-dimensional Hilbert-space setting.

For every fixed Banach limit `L`, a bounded operator `A` occurs as the `L`-asymptotic limit of an operator similar to a unitary if and only if

1. `A` is positive and invertible; and
2. `1` belongs to the essential numerical range `W_e(A)`.

Equivalently, `1` belongs to `W_e(A^{-1})`. The constructive direction is stronger: for every such `A`, the packet constructs one operator

`T = A^{-1/2} U A^{1/2}`

for which `A_{T,L}=A` simultaneously for every Banach limit `L`.

The proof normalizes an arbitrary similarity by its unitary-conjugacy Banach mean, obtains the essential-numerical-range obstruction from a finite-rank trace argument, and proves sufficiency by combining Weyl--von Neumann diagonalization modulo compacts with a balanced bilateral-shift arrangement.

The result is scoped to separable Hilbert spaces. A nonseparable analogue is not claimed, and the bounded novelty search is not a publication-level priority search.

## Files

- `solution_packet.pdf`: source evidence, theorem, full proof, checks, literature boundary, and scope.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:1505.07205 source paper.
- `figures/open_problem_crop.png`: source-question evidence crop from PDF page 39.
- `verification.md`: adversarial proof audit and artifact-verification record.
- `code/check_shift_average.py`: numerical sanity check for the balanced diagonal construction.
