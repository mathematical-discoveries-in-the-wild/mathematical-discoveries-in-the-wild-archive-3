# Verification report

Verdict: `candidate_full_solution_likely_valid`

## Dependency audit

1. **Global fixed-point presentation.**  The proof assumes the standard
   Doplicher--Roberts/Carpi--Conti conclusion explicitly invoked in Problem
   5.6: there is a complete field net `F`, its compact internal gauge group
   `G`, and a closed subgroup `H<G` with `B=F^G` and `A=F^H`.  This is stated
   as a hypothesis in the theorem rather than hidden in the notation.

2. **Local UCP classification.**  For every double cone `O`, Proposition 9.7
   of Bischoff--Del Vecchio--Giorgetti identifies all unital completely
   positive maps on `F(O)^H` fixing `F(O)^G` with `P(G//H)`, affinely and
   homeomorphically.  Their Section 9.2 and Example 9.26 are the exact
   double-coset and AQFT passages cited by the source problem.

3. **Restriction consistency.**  The integral formula uses the same global
   gauge automorphisms on every local algebra.  Therefore its restriction
   from `O2` to `O1 subset O2` is the local formula at `O1`.  Injectivity of
   the local parametrization then forces the two representing measures to
   coincide.  Directedness of double cones makes the measure independent of
   `O` globally.

4. **Poincare covariance.**  The gauge group consists of unbroken internal
   symmetries, hence commutes with the Poincare representation.  The
   integrated maps therefore satisfy the covariance identity.

5. **Faithfulness and vacuum preservation.**  Gauge automorphisms preserve
   the vacuum state.  Their probability averages do too.  Because the local
   vacuum state is faithful, a vacuum-preserving positive map cannot kill a
   nonzero positive element, so the maps meet the source's faithfulness
   requirement.

6. **Extreme points.**  The relative UCP set is a face of the global UCP
   set: if a convex combination fixes `B`, apply it to each unitary of `B`;
   a unitary is an extreme point of the operator-norm unit ball, forcing both
   summands to fix it.  Thus relative quantum operations are exactly the
   extreme points of `P(G//H)`, namely the Dirac masses.

7. **Hypergroup structure.**  Proposition 9.7 identifies composition and
   the vacuum adjoint with double-coset convolution and involution locally.
   Since the global family is determined by any one local component, the
   same identities hold globally.

## Bounded novelty check

On 27 August 2026, exact-title, exact-phrase, arXiv-id, author/keyword, and
`QuOp(A|B)` searches were run on the local run indexes and the live arXiv/web
index.  They found the source paper, the 2022/2023 conformal-net antecedent,
and the 2021 local-subfactor theorem, but no later paper claiming a solution
of Problem 5.6 or the Poincare analogue of the extension theorem.  This is a
bounded search, not a claim of exhaustive novelty.

## Mechanical checks

There is no numerical or symbolic computation in the proof.  The final PDF
was compiled with `latexmk`, checked for LaTeX warnings and overfull boxes,
rendered to page images, and visually inspected.  See the packet build log in
`tmp/` for the exact compilation record.

## Main review focus

The only substantial external-input check is the passage from the precise
standing hypotheses of the source problem to the fixed-point presentation
`B=F^G subset F^H=A` with the local hypotheses of Proposition 9.7.  The new
local-to-global step itself uses only compatibility, injectivity, and the
directedness of double cones.
