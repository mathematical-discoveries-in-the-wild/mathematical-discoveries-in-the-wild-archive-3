# Finite-type diametral-dimension question answered negatively

Status: `literature_already_answered`

## Original question

Nazli Dogan, *Some Remarks on Diametral Dimension and Approximate
Diametral Dimension of Certain Nuclear Frechet Spaces*, arXiv:1908.01838v2,
Question 1.1 on PDF page 2.

For a nuclear Frechet space `E` with `DN` and `Omega`, the question asks
whether coincidence of `Delta(E)` with the diametral dimension of a power
series space forces the analogous coincidence for `delta(E)`, and conversely.
The source proves the infinite-type equivalence. In finite type it proves
`delta(E)=delta(Lambda_1(epsilon))` if and only if both
`Delta(E)=Delta(Lambda_1(epsilon))` and `E` has a prominent bounded set,
leaving open whether the `Delta` equality alone suffices.

## Later answer

Nazli Dogan, *On Power Series Subspaces of Certain Nuclear Frechet Spaces*,
arXiv:2210.13593v1, explicitly repeats the problem as Question 1.2 and states
on PDF page 2 that it has a negative answer in finite type.

For an unstable finitely nuclear exponent sequence `alpha`, the paper
constructs a nuclear Frechet Kothe space `K_alpha` satisfying `DN` and
`Omega`. Propositions 3.6 and 3.7 (PDF pages 20--22) prove

```text
Delta(K_alpha) = Delta(Lambda_1((alpha_{n+1}))),
delta(K_alpha) != delta(Lambda_1((alpha_{n+1}))).
```

Remark 3.8 identifies this as a negative answer to Question 1.2. Theorem 4.8
(PDF page 26) also records that the example has no prominent bounded set.
The supporting author explicitly knows she is answering the earlier question
and cites the original paper.

## Scope

This is an already-known literature counterexample, not a new result of this
run. The original paper's infinite-type theorem and finite-type converse
remain valid; only the unrestricted finite-type forward implication fails.

## Files

- `solution_packet.pdf`: compact identification note.
- `source_paper.pdf`: arXiv:1908.01838v2.
- `supporting_paper_2210.13593.pdf`: later answering paper.
- `main.tex`: packet source.

