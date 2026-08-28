# Scalar-collision counterexample to exact continuous unitary convexity

Status: **candidate full counterexample, likely valid, pending human review**.

This packet gives a negative answer to Question 7.2 of arXiv:2210.13309.
It constructs diagonal self-adjoint fields `A,B in C(X,M_3)` on the compact
metric space `X=[0,1] x closed_unit_disk` such that `A \prec_c B` but
`A` is not in the exact finite convex hull of the continuous unitary orbit of
`B`.

The construction thickens a scalar collision in the two independent
trace-zero directions of `R^3`. A hypothetical fixed-weight finite unitary
average would then induce, on the collision interval, a fixed-weight
decomposition of the nonconstant Birkhoff-edge path

```text
D_s = alpha(s) I + (1-alpha(s)) P
```

into continuous unistochastic fields. The zero pattern forces every summand
to be exactly `I` or the 3-cycle `P`, hence constant along the connected
collision interval. This contradicts the variation of `alpha`.

Files:

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:2210.13309.
- `source_question_crop.png`: published Question 7.2 and context.
- `code/verify_construction.py`: deterministic algebra/support checks.
- `code/verification_output.txt`: captured checker output.
- `verification.md`: proof audit and computation boundary.
- `novelty.md`: bounded literature-status audit.

Human review should focus on the first-order limit at the scalar collision and
the support-rigidity lemma for unistochastic `3 x 3` matrices.

