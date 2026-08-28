# Verification report

Status: `candidate_full_solution_likely_valid`

## Mathematical checks

- Checked the failure-of-ULA quantifiers. One fixed scale R and expansion h
  work for every proposed localization diameter S, while the finite witness F
  may depend on S; this is exactly what is needed to negate p-ONL.
- Checked that singleton sets force every vertex of the finite proximity graph
  to have positive degree, so the degree-weighted random walk is well-defined.
- Checked the coarea calculation and constants:
  edge expansion h, maximum degree D, and Cauchy-Schwarz give
  `sum_edges |g_x-g_y|^2 >= h^2/(2D^2) sum_x d_x g_x^2`.
- Checked the complex scalar monotonicity inequality by reducing its minimum to
  equal arguments; the real constant is `4(p-1)/p^2`.
- Checked the duality-map pairing. Symmetrization over unoriented edges has no
  missing factor, and Hölder gives a uniform lower bound on `||(I-P)w||_p`.
- Checked the uniform-convexity step for both p<2 and p>2. Only positivity of
  the ℓp modulus is used; no Hilbert identity is assumed.
- Checked the degree conjugation: multiplication by `d_x^{-1/p}` is an
  isometry from counting ℓp to degree-weighted ℓp and preserves supports.
- Checked vectors with coordinates outside F: the extended operator ignores
  them, so the local upper bound only improves.
- Checked the ULA-to-Property-A bridge for general bounded-geometry metric
  spaces. At each scale, proximity graphs have uniformly bounded degree;
  metric diameter bounds give cardinality bounds, outer boundary controls the
  graph's inner boundary up to the degree, and graph-distance supports are
  controlled in the original metric.
- Checked the finite-propagation commutator lemma. The partial-translation
  decomposition depends only on the controlled support relation and therefore
  works on every ℓp; each commutator has norm at most LR.
- Checked the endpoint separately: the ℓ1 column formula is exact even for
  uncountable X because every ℓ1 vector has countable support.

The proof has no computational dependency.

## Literature check

Bounded searches used:

- the exact wording of Question 6.6;
- `p-operator norm localization`, `p-ONL`, `independent of p`,
  `Property A converse`, and `uniform local amenability`;
- arXiv ids 1809.00532, 1811.10457, 1912.00806, and their citation context;
- the run's registry, solution, attempt, and proof-gap indexes.

Chung-Nowak arXiv:1811.10457 explicitly leaves the p-ONL converse open and
suggests ULA as a route. No later proof or counterexample was found through
27 August 2026. This is bounded novelty evidence, not exhaustive priority
certification.

## Scope check

The packet fully answers the natural direct replacement of ℓ2 by ℓp in all
five clauses of Proposition 6.3: equivalence for 1<p<∞ and failure at p=1. It
does not preclude a different endpoint localization condition.

## Rendering check

The packet was compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error -outdir=tmp main.tex`. Every final PDF page was rendered and
visually inspected for clipping, overflow, formula integrity, source-image
readability, and page transitions.

## Human-review recommendation

Review as a likely valid full solution. Highest-value checks are Lemma 2's
duality-map estimate, Theorem 3's quantifier order, and the final reduction
from metric ULA to Elek's bounded-degree graph theorem.
