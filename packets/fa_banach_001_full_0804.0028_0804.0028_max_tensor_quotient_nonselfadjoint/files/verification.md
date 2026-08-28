# Verification report

## Claim checked

For an approximately unital closed ideal `A` in an operator algebra `B` and
an approximately unital operator algebra `D`, the canonical map

```text
(B tensor_max D)/(A tensor_max D) -> (B/A) tensor_max D
```

is a completely isometric isomorphism.

## Mathematical checks

1. The ideal inclusion `A tensor_max D -> B tensor_max D` is completely
   isometric by the nondegenerate ideal-representation extension argument
   used in Proposition 2.5 of the source.  That argument only needs the cai of
   `A` and `D`; it does not use selfadjointness of `D`.
2. Functoriality gives the canonical completely contractive quotient map in
   the displayed direction.
3. A completely isometric representation of the quotient, composed with the
   quotient map, has the standard maximal-tensor factorization
   `pi(b) theta(d)` with commuting completely contractive representations.
4. On `K = closure(theta(D)H)`, the equations
   `pi(a) theta(d)=0` imply `pi(a)|K=0` for every `a in A`; hence `pi|K`
   factors completely contractively through `B/A`.
5. Every represented tensor operator vanishes on `K^perp` and has range in
   `K`, so restriction to `K` preserves every matrix norm.  This is the step
   that handles possibly degenerate representations.
6. The induced representation of `(B/A) tensor_max D` gives the reverse norm
   inequality at all matrix levels.  The canonical map is therefore a
   complete isometry.  Its range is closed and contains the dense algebraic
   tensor product, hence is onto.
7. The published erratum to the source paper changes later AWEP statements
   but does not modify Lemma 2.7 or the open question used here.

No unproved lemma specific to this packet remains.  The only invoked external
facts are standard defining properties of the maximal operator-algebra tensor
product and the standard extension of a nondegenerate representation of an
approximately unital ideal.

## Bounded novelty check

Checked on 2026-08-27:

- arXiv and web searches for the exact title, `Blecher Duncan Lemma 2.7
  nonselfadjoint D quotient`, `operator algebra maximal tensor product
  projective quotient`, and close variants;
- the published 2011 paper and its three-page published erratum;
- citation/search hits for projectivity of maximal tensor products.

The search found Han's 2011 projectivity theorem for the maximal **operator
system** tensor product, but no paper explicitly answering this
operator-**algebra** question and no occurrence of the exact quotient theorem
for two nonselfadjoint factors.  Novelty is therefore plausible, not
certified.

## Artifact checks

- `source_paper.pdf` is the 19-page arXiv PDF.
- `figures/open_problem_crop.png` is a readable full-text-width crop from PDF
  page 4 and includes the complete question sentence and Lemma 2.7 statement.
- The final packet was compiled with LaTeX, rendered to PNG, and visually
  inspected page by page for clipping, overlap, missing glyphs, and legibility.

## Human-review focus

Verify the standard factor-representation property for a possibly degenerate
representation of `B tensor_max D` in exactly the convention of Blecher--Le
Merdy Chapter 6.  The proof explicitly passes to the essential `D`-subspace,
so no nondegeneracy assumption should be hidden.
