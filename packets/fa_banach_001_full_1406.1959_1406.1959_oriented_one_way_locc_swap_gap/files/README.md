# Unbounded oriented one-way LOCC gap by subsystem swap

Status: **candidate full result, likely valid, pending human review**.

For the oriented class `LOCC^{A->B}` displayed in Section 2.3 of
arXiv:1406.1959, this packet answers the first question in Section 7.3:
there is no absolute constant comparing its distinguishability norm from
below with unrestricted finite-round `LOCC`.

The key lemma is exact. If

```text
Delta = sum_i |i><i| tensor Delta_i
```

is classical on Alice's side, then communication in the reverse direction
does not improve on product measurements:

```text
||Delta||_(LOCC B->A) = ||Delta||_LO.
```

Swapping the tensor factors in the source's Theorem 3 data-locking pair gives
states with unrestricted `LOCC` norm `2` and fixed-direction
`LOCC^{A->B}` norm at most `C/sqrt(d)`. Hence the norm ratio grows at least
as a constant times `sqrt(d)`.

Convention boundary: this resolves the oriented class exactly as displayed
in the source. It does not resolve a symmetrized convention taking the union
or maximum of both one-way directions.

Files:

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:1406.1959.
- `code/verify_collapse.py`: randomized finite-dimensional checks of the
  collapse inequality.
- `code/verification_output.txt`: captured checker output.
- `verification.md`: proof audit and convention boundary.
- `novelty.md`: bounded literature-status audit.

