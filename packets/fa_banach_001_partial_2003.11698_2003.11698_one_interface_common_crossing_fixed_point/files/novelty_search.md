# Bounded novelty and literature search

Search date: 2026-08-26.

## Local run indexes

Searched `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
and `proof_gaps/index.tsv` for:

- `2003.11698` and the exact source title;
- `Schauder fixed point`, `integral process variable`, and `variability`;
- `common crossing`, `transversal interface`, `hyperplane interface`, and
  `jump line`;
- `bounded compression`, `regular Lagrangian flow`, `Riesz energy`, and
  `almost every initial point`.

The only target-specific hit was the same lane's companion partial obstruction.
No overlapping active claim or prior source-level solution was found.

## Source and follow-ups

The 2023 version of arXiv:2003.11698 still states the fixed-point variability
issue as its main open problem. Focused source searches confirm that it proves
smooth curves with finitely many interface hits are variable, but does not use
that observation to construct a fixed point. Searches in the authors’
arXiv:2105.06249 and arXiv:2407.06907 found no matching one-interface
fixed-point theorem.

## Bounded-compression search

Focused searches combined `bounded compression`, `regular Lagrangian flow`,
`BV coefficient`, `Riesz potential`, `occupation measure`, and the source term
`variability`. They located regular-flow existence theory and ordinary
occupation-measure estimates, but no theorem deriving the source's
componentwise variability condition from bounded compression by averaging over
initial points.

The primary external input is Luigi Ambrosio, *Transport equation and Cauchy
problem for BV vector fields*, Invent. Math. 158 (2004), 227–260,
doi:10.1007/s00222-004-0367-2. It supplies existence, uniqueness, and bounded
compression of a regular Lagrangian flow for `BV` vector fields with bounded
divergence and standard growth. It does not state the Riesz-energy variability
conclusion. That conclusion is the packet's separate Tonelli/kernel lemma.

## Closest external literature

1. Burden, Sastry, Koditschek, and Revzen, *Event-Selected Vector Field
   Discontinuities Yield Piecewise-Differentiable Flows*, arXiv:1407.1775,
   proves well-defined flows for piecewise-smooth vector fields transverse to
   event surfaces. This supports the naturality of the crossing hypothesis,
   but the work does not formulate the source paper’s Riesz-potential
   variability condition, the sharp `sp<1` estimate, or the rough common-row
   clock theorem.
2. Rodrigo López Pouso, *Schauder’s fixed-point theorem: new applications and
   a new version for discontinuous operators*, Boundary Value Problems 2012,
   Article 92, uses null contact with discontinuity curves to recover fixed
   points for discontinuous boundary-value problems. The continuity mechanism
   is philosophically close to the packet’s absolutely continuous theorem,
   but its equations and conclusions are different.

Focused web/arXiv queries combined the exact source phrase with `fixed point`,
`one interface`, `transversality`, `piecewise Lipschitz vector field`, and
`Riesz potential`. They returned the source and the general discontinuous-flow
literature above, but no matching fixed-point-plus-variability statement.

## Novelty assessment

The existence/uniqueness of transversal piecewise-smooth flows is classical.
The candidate contribution is the explicit bridge to the source open problem:

- a general theorem that bounded compression forces `(s,1)`-variability for
  almost every initial point, simultaneously for every `s<1`;
- removal of all driver occupation/upper-regularity conditions from the
  source's full Doss construction for generic initial points;
- a non-Doss existence-and-variability result for Ambrosio flows driven by
  Lipschitz time signals;
- a rough-driver fixed-point construction using a common normal row and a
  monotone clock projection;
- a sharp componentwise `(s,p)`-variability estimate `sp<1` for the resulting
  integral process;
- a direct Schauder proof for the more flexible absolutely continuous
  common-crossing class;
- an exact tangential-collapse example showing why such output geometry is
  needed.

No matching bounded-compression variability lemma or combined theorem was
found in this bounded search. Independent prior observation remains possible.
Because the strongest rough-driver application still uses Doss and holds only
for almost every initial point, the packet uses the conservative label
**candidate substantial partial result, likely valid**.
