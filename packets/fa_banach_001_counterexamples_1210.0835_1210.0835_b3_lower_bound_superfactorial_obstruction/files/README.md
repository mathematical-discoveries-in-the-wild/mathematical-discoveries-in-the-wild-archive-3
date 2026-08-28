# The proposed B3 factorial lower bound is impossible

This packet gives a candidate disproof of inequality (27) proposed in
Question 6 on PDF page 5 of arXiv:1210.0835v1.

## Result

For every `m>=1`,

```text
|B_3(2m+1)| <= binom(m+5,3)/(4^(m+4)(m!)^2).
```

Hence `(m! |B_3(2m+1)|)^(1/m)` tends to zero.  No positive absolute
constant `C` can make the requested lower bound
`|B_3(2m+1)| >= C^m/m!` hold eventually.

The proof uses only the path denominator and the fact that there are three
negative steps; it bounds the absolute sum, so cancellation is irrelevant.

## Scope

This disproves the fallback estimate in Question 6.  It does not give an
asymptotic formula for `B_3(2m+1)` and does not decide the associated
antiperiodic Hill-operator basis question.  It shows that the route through
inequality (27) cannot work.

## Files

- `main.tex`: source question, definitions, theorem, and proof.
- `solution_packet.pdf`: rendered counterexample packet.
- `verification.md`: proof and render audit.
- `source_paper.pdf`: arXiv:1210.0835v1.
- `figures/open_problem_crop.png`: Question 6 and inequalities (27)-(28).
- `code/verify_b3.py`: exact rational enumeration check.

Status: candidate counterexample/disproof, likely valid.  Independent expert
review should focus on the selected-vertex product bound and the exact match
between the normalized path variables and the source definitions.

