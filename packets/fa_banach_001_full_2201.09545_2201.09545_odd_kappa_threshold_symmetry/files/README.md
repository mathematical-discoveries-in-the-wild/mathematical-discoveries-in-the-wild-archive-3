# Odd-kappa symmetry of finite-order threshold sets

Status: candidate full solution, likely valid, pending human review.

This packet answers the open problem following Lemma 3.3 of Golénia--Mandich,
arXiv:2201.09545.  For every dimension `d`, every positive integer `kappa`,
and every nonnegative integer `m`,

```text
Theta_{m,kappa}(Delta) = -Theta_{m,kappa}(Delta).
```

The source proves this only for even `kappa` and asks whether it also holds
for odd `kappa`.  Under simultaneous coordinatewise negation,
`g_{j kappa}` acquires the parity factor `(-1)^(j kappa-1)`.  The same factor
appears at every witness point in the defining relation for each fixed `j`,
so the relation and its nonpositive weights are preserved.  This proves the
missing odd case and, in fact, gives one proof for all `kappa`.

Files:

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: the source question on arXiv PDF page 12.
- `code/verify_parity.py`: symbolic parity diagnostic.
- `verification.md`: proof and rendering audit.
- `novelty.md`: bounded literature-search record.

The result concerns the finite-order witness sets `Theta_{m,kappa}`.  It does
not settle the paper's broader conjectures about the full threshold set,
countability, or Mourre bands.
