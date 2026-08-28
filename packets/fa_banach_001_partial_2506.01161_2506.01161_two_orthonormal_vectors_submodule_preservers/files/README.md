# Submodule preservers on Hilbert modules with two orthonormal vectors

Status: `superseded_by_full_result`

This elementary graph-submodule packet has been superseded by the arbitrary-
module classification at
`runs/fa_banach_001/solutions/full/2506.01161_adjointable_submodule_preserver_classification/`.
Its compact corollaries and direct two-vector proof remain valid review
material.

Agent: `agent_lane_03`  
Model: `GPT5.6`  
Date: 2026-08-26

## Source questions

Kamran Sharifi, *Invariant submodules of modular operators and Lomonosov
type theorem for Hilbert C*-modules*, arXiv:2506.01161, asks:

- Problem 2.16, PDF page 11: characterize the C*-algebras for which an
  adjointable operator leaving every closed submodule invariant must be a
  coefficient morphism `I.a` with `a` nonzero.
- Problem 4.10, PDF page 17: for `I != K` compact, characterize the
  C*-algebras for which every closed submodule is `K`-invariant.

The source statements have two literal boundary issues. The zero operator
satisfies the hypothesis of Problem 2.16 but cannot have a nonzero faithful
coefficient. Problem 4.10 allows `K=0`, which automatically preserves every
submodule. The theorem below answers the natural repaired preserver question
on every module containing two orthonormal module vectors.

## Result

Let `A` be a unital C*-algebra and `E` a right Hilbert `A`-module containing
orthonormal vectors `e1,e2`, meaning

```text
<ei,ej> = delta_ij 1_A.
```

For `T in L(E)`, the following are equivalent:

1. every closed right `A`-submodule of `E` is `T`-invariant;
2. `T=R_z`, where `R_z(x)=xz` and `z` belongs to the center `Z(A)`.

No injectivity, surjectivity, or nonzero hypothesis on `T` is required.

The proof uses only closed cyclic graph submodules. Invariance of `e1 A` and
`e2 A` diagonalizes `T` on the two coordinates. Invariance of
`(e1+e2)A` equates the two coefficients. Invariance of
`(e1+e2 c)A` for arbitrary `c in A` forces that coefficient to commute with
every `c`. Finally, for `y` orthogonal to the two-coordinate summand,
invariance of `(e1+y)A` forces `Ty=yz`.

## Compact consequences

- On `A^n`, `n>=2`, the operators preserving every closed submodule are
  exactly the central scalar matrices `z I_n`, `z in Z(A)`.
- Since `K_A(A^n)=M_n(A)`, these are also exactly the compact preservers.
- On the standard module `ell_2(A)`, the only compact operator preserving
  every closed submodule is zero. Indeed, a compact operator sends the
  standard orthonormal sequence to zero in norm, while `R_z e_m` has constant
  norm `||z||`.
- Under a universal reading of Problem 4.10, no nonzero unital algebra works:
  on `A^2`, the compact projection `diag(1,0)` does not preserve
  `(e1+e2)A`.

## Relation to later literature

Michael Frank, *C*-submodule preserving module mappings on Hilbert
C*-modules*, arXiv:2507.11206, explicitly cites Sharifi's Problem 2.16.
Theorem 1.2 proves the central-multiplier conclusion for bijective bounded
module morphisms on arbitrary full Hilbert modules. The paper states that a
complete solution for merely injective preservers remains out of reach.

The result in this packet is therefore not the already-known bijective case:
it removes injectivity altogether, at the price of assuming two orthonormal
module vectors. It also gives the exact compact classification on `A^n` and
`ell_2(A)`.

## Verification

`code/check_matrix_models.py` forms the exact commutator constraints with all
matrix units in `M_d(Q)` for `1<=d<=7`. It verifies that their common
commutant has dimension one and checks the `diag(1,0)` graph-submodule
counterexample. These finite models are consistency checks, not a substitute
for the proof.

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2506.01161_two_orthonormal_vectors_submodule_preservers/code/check_matrix_models.py \
  --max-dimension 7
```

## Novelty scope and human review

The four run indexes were searched for both arXiv ids and the invariant-
submodule/coefficient-morphism terminology. Current arXiv searches used the
exact source problem, `C*-submodule preserving`, `Alg Lat`, central
multipliers, orthonormal module vectors, and non-bijective variants. They
found Frank's adjacent bijective theorem but no statement matching the
two-orthonormal-vector theorem or its compact corollaries. This is bounded
novelty evidence, not a publication-novelty guarantee.

Human review should focus on the closedness of the cyclic graph submodules,
the passage from their invariance to centrality, and the compactness argument
on `ell_2(A)`.

## Files

- `solution_packet.pdf`: rendered proof packet
- `main.tex`: packet source
- `source_paper.pdf`: arXiv:2506.01161
- `supporting_paper_2507.11206.pdf`: adjacent bijective result
- `figures/problem_2_16_crop.png`: source Problem 2.16
- `figures/problem_4_10_crop.png`: source Problem 4.10
- `code/check_matrix_models.py`: exact finite matrix consistency check
- Ledger:
  `runs/fa_banach_001/ledger/results/2506.01161_two_orthonormal_vectors_submodule_preservers.json`
