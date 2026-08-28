# A positive contraction need not be ell^1-contractive

Status: `candidate_counterexample_likely_valid`

## Source question

Christian Le Merdy and Safoura Zadeh, *ell^1-contractive maps on
noncommutative L^p-spaces*, arXiv:1907.03995.  Immediately after Remark 5.2
on printed page 21, the authors ask whether every positive contraction is
ell^1-contractive: “We do not know if any positive contraction is
ell^1-contractive.”

## Proof intuition

The skew unitary `U` sends each vector to an orthogonal partner.  Thus, on a
rank-one positive input, `T` subtracts two orthogonal rank-one projections
from the scalar matrix that dominates both; this proves positivity.  On the
Hilbert-Schmidt space, the transpose-twist is an involutive isometry, so an
orthogonal eigenspace decomposition makes contractivity immediate.

The failure of ell^1-contractivity comes from row-column incidence.  The
chosen input matrices admit an unusually efficient weighted factorization,
whereas their images form a 2-regular bipartite pattern.  Entrywise
Cauchy-Schwarz forces sharp lower bounds for both factorization norms, and the
output bound is strictly larger than the input bound.

## Result

The answer is no, already for the Hilbert-Schmidt class `S_4^2`.

Let `J=[[0,1],[-1,0]]`, `U=diag(J,J)`, and define

```text
T(x) = (Tr(x) I_4 - x - U x^T U*)/2.
```

The map is positive: on a rank-one positive matrix `xi xi*`, the two vectors
`xi` and `U conjugate(xi)` are orthogonal, so the expression in parentheses
is positive.  It is an `S_2`-contraction because it is an orthogonal signed
projection: it acts by `1`, `-1`, and `0` on three mutually orthogonal
subspaces.

For the three matrices

```text
x1 = E41-E23,
x2 = -(E11+E22),
x3 = E31+E24,
```

an exact entrywise factorization argument gives

```text
||(x1,x2,x3)||_{S_4^2(ell^1)} = sqrt(6 sqrt(3)),
||(T x1,T x2,T x3)||_{S_4^2(ell^1)} = 2 sqrt(3).
```

Hence the amplification ratio is `sqrt(2/sqrt(3)) > 1`.

## Files

- `solution_packet.pdf`: complete self-contained counterexample.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: source question and neighboring results.
- `code/verify_counterexample.py`: independent matrix and norm sanity checks.
- `verification.md`: independent algebra and norm checklist.

## Human review recommendation

Check the two exact lower bounds for the vector-valued norms.  They use only
entrywise Cauchy-Schwarz and the factorization formula in source Lemma 2.3
(Lemma 2.6 in the arXiv source).  No numerical optimization enters the proof.
