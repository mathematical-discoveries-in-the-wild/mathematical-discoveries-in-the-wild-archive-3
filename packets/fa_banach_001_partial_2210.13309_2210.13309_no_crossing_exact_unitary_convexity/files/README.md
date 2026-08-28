# Exact unitary convexity on the simple-spectrum stratum

Status: **candidate partial result, likely valid, pending human review**.

This packet gives an affirmative answer to Question 7.2 of arXiv:2210.13309
whenever the majorizing field `B` has simple spectrum at every point of the
compact base. More precisely, if `A` and `B` are self-adjoint and continuously
diagonalizable in `C(X,M_n)`, `A \prec_c B`, and `B(x)` has `n` distinct
eigenvalues for every `x`, then there are continuous unitaries
`U_0,...,U_{n-1}` such that

```text
A = (1/n) sum_k U_k^* B U_k.
```

Thus the conclusion is exact, uses equal weights, and needs only `n` unitary
conjugates. The proof uses the nonnegative part of the permutohedral toric
variety as a continuous Schur-Horn slice, followed by cyclic diagonal-phase
averaging. The only unresolved part of the source question is the collision
locus where eigenvalues of `B` meet.

Files:

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:2210.13309.
- `source_question_crop.png`: source Question 7.2 and its context.
- `supporting_lian_2309.01747.pdf`: generic torus orbit closures and weighted
  permutohedra.
- `supporting_sottile_math0212044.pdf`: nonnegative toric part/moment-polytope
  homeomorphism.
- `code/verify_dephasing.py`: numerical checks of the equal-weight identity.
- `code/verification_output.txt`: captured checker output.
- `verification.md`: proof audit and code boundary.
- `novelty.md`: bounded literature-status audit.

Human review should focus on the standard toric-slice lemma, especially the
identification of the weighted moment map with the diagonal map on a Hermitian
orbit and the joint continuity as the simple eigenvalue vector varies.
