# Discrete and SIN group algebras are zero Jordan product determined

Status: `candidate_substantial_partial_likely_valid`.

Source: J. Alaminos, M. Brešar, J. Extremera, and A. R. Villena,
*Zero Jordan product determined Banach algebras*, arXiv:1902.04846;
Journal of the Australian Mathematical Society 111 (2021), 145–158.
The target is Question 3.7 on source PDF page 8.

## Claimed result

If `G` is a locally compact SIN group, then `L^1(G)` is zero Jordan product
determined. In particular, `ell^1(G)` is zero Jordan product determined for
**every discrete group**. This includes torsion-free nonamenable groups such
as free groups and nondiscrete nonamenable groups such as `F_2 x R`.

The proof maps one explicit diagonal-synthesis identity in the Wiener algebra
`A(T^2)` into the group algebra. It shows that every commutator belongs to

```text
J(A) = closure span {ab : a,b in A and ab+ba=0}.
```

The source paper's commutator criterion then gives zero Jordan product
determination. For discrete groups the anticommuting witnesses already lie in
`ell^1(G)`. For SIN groups, a conjugation-invariant contractive approximate
identity moves the multiplier witnesses into `L^1(G)` without losing exact
anticommutation.

## Scope

This fully resolves the discrete-group subproblem and gives a substantial
nondiscrete extension, but it is still a partial answer to Question 3.7 for
arbitrary locally compact groups. In the non-SIN case a general approximate
identity need not commute with the cyclic multiplier calculus; the present
argument then gives only approximate, rather than exact, anticommutation.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `verification.md`: adversarial proof and scope audit.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: source Theorem 3.6 and Question 3.7.

## Novelty check

A bounded search was performed on 2026-08-27. The cheap run indexes and close
web/arXiv searches were checked for arXiv:1902.04846 together with `zero
Jordan product determined`, `all discrete groups`, `SIN group`, `central
approximate identity`, `Wiener algebra`, and `diagonal synthesis`. The source
article and general algebraic papers were found, but no explicit statement of
either theorem in this packet. This is not an exhaustive citation-database
search, so novelty remains provisional.

## Human review recommendation

Send to an expert in Banach algebras or abstract harmonic analysis. Review
should concentrate on the separated-support Wiener lemma and on the central
approximate-identity transfer. Both are proved in the packet rather than
invoked as black boxes.
