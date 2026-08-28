# Partial solution packet: the model-space closed-range dichotomy

## Source

- Konstantin M. Dyakonov, *Carleson-type embeddings with closed range*,
  arXiv:2505.15079.
- Future-research proposal: page 6, asking for a corresponding closed-range
  theory for the star-invariant spaces `K_theta^p`, `1 <= p < infinity`, and
  predicting Bergman-type behavior.
- Model: GPT5.6.

## Classification

- Status: `candidate_partial_likely_valid`.
- Scope: a complete abstract sampling/interpolation dichotomy for every
  `1 <= p < infinity`; a concrete frame/Riesz classification of every bounded
  embedding for the Hilbert space `K_theta^2`; and an exact infinite product-
  inner family.
- Limitation: no new geometric characterization of all sampling and
  interpolation measures for arbitrary inner `theta` and exponent `p`.

## Main result

Let `mu` be a positive measure on the open disk inducing a bounded restriction
operator `J_mu:K_theta^p -> L^p(mu)`. Then `J_mu` has closed range exactly in
one of two cases:

1. `mu` is a sampling measure (the injective branch);
2. the kernel is nonzero, `mu` is atomic on a discrete zero set, and the
   restriction map is onto the corresponding weighted sequence space (the
   interpolation branch).

In the second branch, closed range automatically means surjectivity. The key
new mechanism is that division by an inner Blaschke factor preserves
`K_theta^p`: a single nonzero kernel function produces all coordinate vectors
in the trace range.

For `p=2`, the interpolation branch is equivalent to the weighted reproducing
kernels `{sqrt(a_n) k_{z_n}^theta}` being a Riesz sequence. On an atomic
uniqueness support, closed range is instead equivalent to the same family
being a frame for all of `K_theta^2`.

## Concrete family

For `theta=B_1 B_2`, with `B_1` an infinite interpolating Blaschke product and
`B_2` nonconstant inner, the measure `sum a_n delta_{z_n}` on the zeros of
`B_1` induces a bounded embedding precisely when

```text
sup_n a_n/(1-|z_n|^2) < infinity.
```

Under boundedness, the range is closed precisely when
`a_n` is comparable to `1-|z_n|^2`; the kernel is `B_1 K_{B_2}^2`.

## Verification and novelty

- `verification.md` audits support discreteness, the division lemma, density,
  the closed-range alternatives, and the Hilbert adjoint argument.
- `code/verify_finite_product_example.py` checks the finite Blaschke-product
  matrix model and kernel Gram identity over 500 deterministic random cases.
- Cheap run indexes had no exact duplicate. Exact arXiv/web searches on
  2026-08-26 found the source paper, the known reverse-Carleson/sampling
  literature, and model-space interpolation literature, but no paper stating
  this noninjective closed-range dichotomy or its weighted-kernel criterion.
  This is bounded novelty evidence, not a priority claim.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: compiled and visually checked packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: source page-6 future-work passage.
- `code/verify_finite_product_example.py`: finite-dimensional sanity check.
- `verification.md`: proof and artifact verification report.
