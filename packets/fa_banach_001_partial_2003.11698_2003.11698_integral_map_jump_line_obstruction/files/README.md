# Jump-line obstruction to preservation of variability

- **Source:** Michael Hinz, Jonas M. Tölle, and Lauri Viitasaari,
  *Variability of paths and differential equations with BV-coefficients*,
  arXiv:2003.11698; Ann. Inst. H. Poincaré Probab. Statist. 59 (2023),
  2036–2082.
- **Source target:** the open problem on replacing the Doss transform by a
  fixed-point argument, specifically proving under suitable assumptions that
  the integral process is variable (journal/arXiv PDF p. 6, Section 1.2).
- **Status:** candidate substantial partial result / sharp obstruction, likely
  valid; not a full resolution of the deliberately open-ended source problem.
- **Model:** GPT5.6.

## Result

The raw fixed-point map need not preserve variability, even when all of the
following hold simultaneously:

- the coefficient is bounded, symmetric, uniformly positive definite, and
  piecewise constant with one flat jump line;
- its inverse has distributionally curl-free rows and the coefficient obeys
  the source paper's angle condition;
- the driver is smooth and both of its coordinates are active;
- the input path is Hölder and `(s,p)`-variable for any prescribed finite
  `p` after choosing its Hölder exponent appropriately.

Explicitly, two positive-definite matrices `A_+` and `A_-` are chosen so that
both send `(1,1)` to `(1,0)`. The coefficient equals `A_+` above the horizontal
axis and `A_-` below it. An input path leaves the jump line transversally, so
its Riesz potential behaves like `t^{-alpha s}` and is integrable. The
integral process, however, is exactly `(t,0)` and lies on the jump line for all
time. Its relevant Riesz potential is therefore infinite at every time.

This isolates a necessary feature of any successful fixed-point theorem:
nondegeneracy and the Doss structural hypotheses alone do not control the
occupation of the *output* relative to the jump measure. Some output-side
transversality, occupation-energy, or comparable geometric condition is
needed.

The packet also records a scalar positive subcase: for the time driver
`Y_t=t`, a coefficient bounded below by a positive constant makes the integral
process bi-Lipschitz and hence variable for every exponent below one.

## Files

- `solution_packet.pdf`: rendered review packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: local source paper.
- `figures/open_problem_crop.png`: real crop of the source question on PDF
  page 6.
- `verification.md`: adversarial proof check.
- `novelty_search.md`: bounded duplicate and literature search.

Ledger: `runs/fa_banach_001/ledger/results/2003.11698_integral_map_jump_line_obstruction.json`.

