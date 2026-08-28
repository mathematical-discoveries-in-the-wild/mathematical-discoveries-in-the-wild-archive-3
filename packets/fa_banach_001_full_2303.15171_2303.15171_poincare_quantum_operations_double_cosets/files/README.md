# Poincare-covariant quantum operations are a double-coset hypergroup

Status: `candidate_full_solution_likely_valid`

## Source problem

Luca Giorgetti, *Quantum Operations in Algebraic QFT*, arXiv:2303.15171,
Problem 5.6 on printed page 9.  For a Haag-dual full Poincare-covariant
subnet `B subset A`, the problem proposes

```text
QuOp(A|B) = G//H,
```

where `G` is the Doplicher--Roberts gauge group of `B` and `H` is a closed
subgroup.

## Result

The proposed identification holds in the standard
Doplicher--Roberts/Carpi--Conti regime invoked in the problem.  More
precisely, suppose the subsystem classification supplies a complete field
net `F`, a compact internal gauge group `G`, and a closed subgroup `H<G`
such that

```text
B = F^G,       A = F^H.
```

Then there is an affine homeomorphism

```text
P(G//H)  -->  UCP(A|B).
```

For a probability measure `mu` on the double-coset space, the corresponding
family is obtained by integrating the gauge automorphisms against the
canonical `H`-bi-invariant lift of `mu`.  Its extreme points are exactly the
Dirac measures, so

```text
QuOp(A|B) = G//H
```

as a compact hypergroup.

## Proof intuition

The cited discrete-subfactor theorem already gives the whole probability
simplex `P(G//H)` at each fixed double cone.  A priori the representing
measure could depend on the double cone.  It cannot: if `O1 subset O2`,
compatibility says that the two local maps agree on `A(O1)`, while the local
double-coset parametrization at `O1` is injective.  Hence the two measures
are equal.  Since any two double cones lie in a third, one global measure
parametrizes the entire coherent family.  Internal gauge transformations
commute with the Poincare representation, so every such family is covariant.

## Scope

Problem 5.6 itself obtains `G` from Doplicher--Roberts reconstruction and
cites the Carpi--Conti classification.  Those results use their usual
standing assumptions (including the hypotheses needed for the fixed-point
realization and for the local inclusions to be irreducible local discrete
type III subfactors).  The theorem proves the problem in exactly that
intended setting.  If the very short axioms in Definition 5.1 of the survey
are read without those standing assumptions, the asserted gauge group and
fixed-point presentation need not even be available; no claim is made for
that broader reading.

## Files

- `solution_packet.pdf`: full theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2303.15171.
- `supporting_paper_2007.12384.pdf`: the local double-coset UCP theorem.
- `supporting_paper_math0312033.pdf`: the subsystem classification.
- `figures/open_problem_crop.png`: Problem 5.6 and its immediate context.
- `verification.md`: proof-dependency and topology/extremality audit.

## Human review recommendation

Check that the precise version of the Carpi--Conti classification intended
by Problem 5.6 yields the stated fixed-point realization on every local
algebra, with the minimality/locality assumptions required by Proposition
9.7 of arXiv:2007.12384.  After that input, the compatibility argument is
formal and the packet proves the full identification.
