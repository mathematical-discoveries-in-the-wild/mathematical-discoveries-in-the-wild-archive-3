# Complete classification of adjointable closed-submodule preservers

Status: `candidate_full_result_likely_valid`

Agent: `agent_lane_03`  
Model: `GPT5.6`  
Date: 2026-08-26

## Source question

Kamran Sharifi, *Invariant submodules of modular operators and Lomonosov type
theorem for Hilbert C*-modules*, arXiv:2506.01161, Problem 2.16 on PDF page
11, asks when an adjointable operator leaving every closed submodule invariant
must be a coefficient morphism.

The source statement needs two literal repairs: `T=0` forces the zero
coefficient to be allowed unless `T != 0` is assumed, and a nonunital algebra
naturally produces multiplier coefficients outside the algebra itself.

## Full result

Let `A` be any C*-algebra, let `E` be a nonzero right Hilbert `A`-module, and
put

```text
I_E = closure(span <E,E>).
```

For `T in L_A(E)`, the following are equivalent:

1. every norm-closed right `A`-submodule of `E` is `T`-invariant;
2. `T(x)=x z` for every `x`, for a unique `z in Z(M(I_E))`.

No injectivity, surjectivity, nonzero, unitality, finite generation, or
orthonormal-vector hypothesis is required.

For a full module, `I_E=A`, so the preservers are exactly `R_z` with
`z in Z(M(A))`. After the intended nonzero repair, Sharifi's demand that the
coefficient lie in `A` for every full module holds exactly for unital
C*-algebras. If `A` is nonunital, the identity preserver is implemented by
`1 in M(A)`, not by an element of `A`.

## Proof mechanism

- Closed submodules of `E` correspond to closed right ideals of `K(E)` by
  taking the compact operators with range in the submodule.
- Adjointability identifies `T` with a multiplier of `K(E)`. Submodule
  invariance makes this multiplier preserve every closed right ideal.
- A multiplier preserving every closed right ideal is central. The proof uses
  support projections in the bidual and Kadison transitivity in irreducible
  representations, so it also covers projectionless C*-algebras.
- A direct double-centralizer argument transfers `Z(M(K(E)))` to
  `Z(M(I_E))` and yields `T(x)=xz`.

## Relation to later literature

Michael Frank, arXiv:2507.11206, explicitly cites Sharifi's problem and proves
the central-multiplier conclusion for bijective bounded module morphisms on
full Hilbert modules. The current arXiv version says the merely injective
bounded-module case is out of reach. This packet uses the stronger
adjointability hypothesis in Sharifi's original question and removes
bijectivity and injectivity altogether.

The bounded novelty search found the standard submodule/right-ideal
correspondence and one-sided M-ideal framework, but no theorem stating this
adjointable preserver classification. This is bounded evidence only.

## Verification

`verification.md` contains the adversarial proof audit. The inherited exact
finite-matrix checker is a regression check for the centrality mechanism:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2506.01161_adjointable_submodule_preserver_classification/code/check_matrix_models.py \
  --max-dimension 7
```

Human review should focus on the open-support-projection step in the
right-ideal rigidity lemma and the double-centralizer construction that
transfers the center to the coefficient ideal.

## Files

- `solution_packet.pdf`: rendered full proof packet
- `main.tex`: LaTeX source
- `verification.md`: explicit verifier report
- `source_paper.pdf`: arXiv:2506.01161
- `supporting_paper_2507.11206.pdf`: adjacent bijective theorem
- `figures/open_problem_crop.png`: exact source problem crop
- `code/check_matrix_models.py`: exact finite-dimensional regression check
- ledger: `runs/fa_banach_001/ledger/results/2506.01161_adjointable_submodule_preserver_classification.json`
