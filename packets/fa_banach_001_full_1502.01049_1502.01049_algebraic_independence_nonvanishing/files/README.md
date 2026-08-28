# Algebraic independence forces simultaneous nonvanishing

Status: **candidate full affirmative answer (likely valid; human review requested)**

Source: Philippe Ryckelynck and Laurent Smoch, *On the functional equation
alpha u + C star (chi u) = f*, arXiv:1502.01049, second conjecture in the
final-comments paragraph on source PDF page 15.

## Result

The second conjecture is true, with the genericity hypothesis inherited from
its description as a variant of Theorem 4.1.

Let `psi^(1),...,psi^(l)` be the source paper's generic matricial polynomial
functions, and assume all their coefficients are algebraic over `Q`. If the
`2d^2` entries of `(zeta,xi)` generate a field of transcendence degree `2d^2`
over `Q`, then every entry `psi^(k)_(i,j)(zeta,xi)` and every determinant
`det psi^(k)(zeta,xi)` is nonzero.

The proof has two steps. Theorem 4.1's proof shows that every quantity in the
conclusion is a nonzero polynomial in the `2d^2` matrix entries. Maximal
transcendence degree says exactly that those entries are algebraically
independent over `Q`; because the coefficient field is algebraic over `Q`,
they remain algebraically independent over the coefficient field. A nonzero
polynomial therefore cannot vanish at the prescribed tuple.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv source PDF.
- `figures/open_problem_crop.png`: source PDF page 15 evidence crop.
- `verification.md`: proof audit and reviewer focus.
- `novelty_search.md`: bounded novelty/literature search log.

The source's third conjecture, concerning genericity for arbitrary `N >= 2`,
is not addressed. Human review should focus on whether “variant of Theorem
4.1” indeed imports the genericity hypothesis; without it the statement is
false (take the zero polynomial).
