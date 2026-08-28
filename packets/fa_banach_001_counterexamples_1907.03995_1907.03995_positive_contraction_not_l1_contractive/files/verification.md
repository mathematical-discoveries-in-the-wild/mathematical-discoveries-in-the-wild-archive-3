# Verification report

Status: exact finite-dimensional counterexample; candidate likely valid.

## Algebra

- `U=diag(J,J)` is real unitary, `U^T=-U`, and `U^2=-I`.
- For `R(x)=U x^T U*`, direct substitution gives `R^2=I`; Hilbert-Schmidt
  invariance makes `R` a self-adjoint unitary.
- On a rank-one positive matrix `xi xi*`, the second rank-one term is
  `eta eta*`, where `eta=U conjugate(xi)` and `xi* eta=0`.  Hence `T` is
  positive.
- The orthogonal eigenspace decomposition gives eigenvalues `1,-1,0`, so
  the `S_2 -> S_2` norm is exactly one.
- Direct matrix-unit substitution gives `T(x1)=-x1`,
  `T(x2)=-(E33+E44)`, and `T(x3)=-x3`.

## Input norm

- The displayed factors multiply to the three `x_n`.
- Their two aggregate square sums are
  `diag(sqrt(3),3,sqrt(3),sqrt(3))` and
  `diag(sqrt(3),1,1,1)`.
- Their Hilbert-Schmidt norms are `sqrt(18)` and `sqrt(6)`, giving the
  upper bound `sqrt(6 sqrt(3))`.
- For an arbitrary factorization, entrywise Cauchy-Schwarz supplies six
  constraints.  The grouped quantities satisfy `PR>=3sqrt(3)` and
  `QS>=3sqrt(3)`, so the product of aggregate Hilbert-Schmidt norms is at
  least `6sqrt(3)`.  This matches the upper factorization.

## Output norm

- The natural partial-isometry factorizations have aggregate square sums
  `diag(0,2,2,2)` and `diag(2,0,2,2)`, proving an upper bound `sqrt(12)`.
- The six unit entries form a 2-regular bipartite graph on three rows and
  three columns.  Entrywise Cauchy-Schwarz, followed by two scalar
  Cauchy-Schwarz inequalities, forces the product of aggregate
  Hilbert-Schmidt norms to be at least `12`.
- Thus the ratio is exactly `sqrt(2/sqrt(3))`, which is strictly larger
  than one.

## Scope and literature

- The example is for `p=2` and the finite semifinite von Neumann algebra
  `M_4(C)`, sufficient to refute the universal question.
- Exact-phrase searches for the source question and its terminology found
  no later answer.  OpenAlex listed two citing works; both concern
  isometries/Jordan homomorphisms rather than positive contractions.
- This literature check is bounded.  Human review should prioritize the
  two exact norm lower bounds and the source's factorization convention.

## Executable and render checks

- `code/verify_counterexample.py` confirms all three output identities, the
  superoperator singular values (six ones and ten zeros), the strict ratio
  `1.0745699318235418`, and positivity on 500 seeded random rank-one inputs.
- `latexmk` completed after two passes with no unresolved references,
  overfull boxes, or underfull boxes.
- All four pages of the final 150-dpi PDF render were visually inspected;
  the source crop and all displayed formulas are complete and unclipped.
