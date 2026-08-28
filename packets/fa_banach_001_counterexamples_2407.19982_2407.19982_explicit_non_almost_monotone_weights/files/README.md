# Explicit weights that are not almost monotone

Status: candidate full answer by explicit counterexample, likely valid, awaiting specialist review.

This packet answers item (4) on page 15 of Prakash A. Dabhi,
"On inversion of absolutely convergent weighted Dirichlet series in two
variables" (arXiv:2407.19982). The paper asks whether a weight on
`N` or `N^2` can fail to be almost monotone. The answer is yes for both
semigroups.

Write an exponent `r` in base 4 and read the same digits in base 2:

```text
r = sum d_i 4^i,       c(r) = sum d_i 2^i,       0 <= d_i <= 3.
```

Base-4 carrying can only decrease `c`, so `c` is subadditive. Therefore

```text
omega(n) = 2^(v_2(n) + c(v_2(n)))
```

is a multiplicative-semigroup weight on `N`. It is nonadmissible, since its
spectral growth along powers of 2 tends to 2. But at consecutive exponents
`4^j-1` and `4^j`, its downward ratios tend to infinity, even though
`2^(4^j-1)` divides `2^(4^j)`. Hence no almost-monotonicity constant exists.
The lift `Omega(m,n)=omega(m)` gives the requested example on `N^2`.

Contents:

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of the definition and open
  question on source PDF page 15.
- `VERIFICATION.md`: mathematical, source, novelty, and artifact checks.
- `code/verify_digit_weight.py`: bounded exhaustive sanity check.
- `code/make_open_problem_crop.py`: reproducible source crop.

The proof is elementary and does not rely on the finite computation. The main
human-review focus is the base-4 carry lemma and the match to the paper's two
branches in the definition of almost monotonicity.
