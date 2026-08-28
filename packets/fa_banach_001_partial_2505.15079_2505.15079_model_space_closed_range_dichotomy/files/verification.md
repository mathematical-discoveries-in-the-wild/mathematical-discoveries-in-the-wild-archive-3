# Verification report

## Claim checked

The packet gives a complete structural closed-range dichotomy for bounded
embeddings `K_theta^p -> L^p(mu)`, `1 <= p < infinity`, and an exact Riesz-
kernel formulation for `p=2`.

## Logical checks

1. **Injective branch.** A bounded injective operator has closed range iff its
   inverse on that range is bounded. This is exactly the sampling inequality.
2. **Support reduction.** If nonzero `F` lies in the embedding kernel, then
   `F=0` `mu`-almost everywhere. If a support point had `F(z) != 0`, continuity
   would give a neighborhood of positive `mu`-measure on which `F` is bounded
   away from zero. Hence `supp(mu)` is contained in the discrete zero set of
   `F`, and `mu` is a weighted sum of point masses.
3. **Division lemma.** If `F=b_a^m G` and `F` lies in `K_theta^p`, analyticity
   gives `G in H^p`. On the boundary, division by the inner function is
   multiplication by its conjugate, so a representation
   `F=theta conjugate(z h)` becomes
   `G=theta conjugate(z b_a^m h)`. Therefore `G in K_theta^p`.
4. **Coordinate traces.** Divide `F` by the full zero multiplicity at `z_n`.
   The quotient is nonzero at `z_n` and zero at every other support point.
   Hence every coordinate vector, and thus every finitely supported sequence,
   belongs to the range.
5. **Closed implies onto.** Finitely supported sequences are dense in the
   weighted `ell^p` target for every finite `p`. A closed range containing them
   is the whole target.
6. **Hilbert criterion.** Under the unitary identification
   `L^2(mu)=ell^2`, the restriction map is the analysis operator of
   `{sqrt(a_n) k_{z_n}^theta}`. It is onto iff its adjoint synthesis operator
   is bounded below, exactly the Riesz-sequence condition.
7. **Product-inner family.** The decomposition
   `K_{B_1 B_2}^2=K_{B_1}^2 direct-sum B_1 K_{B_2}^2` makes the kernel exact.
   On zeros of `B_1`, the model kernels are ordinary Szego kernels. Their
   normalized family is Riesz precisely because `B_1` is interpolating;
   rescaling is Riesz precisely when the weight ratios are bounded above and
   below.

## Mechanical check

Command:

```text
conda run --no-capture-output -n sandbox python \
  code/verify_finite_product_example.py
```

The script generates 500 deterministic finite products `theta=B_1 B_2`, builds
the Malmquist-Walsh basis of `K_theta`, and checks:

- the restriction matrix on the zeros of `B_1` has full row rank;
- its nullity is `deg(B_2)`;
- its row Gram matrix agrees with the weighted reproducing-kernel Gram matrix.

This is a finite-dimensional sanity check, not a proof of the infinite result.

Recorded output:

```text
trials 500
max_gram_residual 4.057e-15
min_row_singular_value 1.575e-05
max_verified_nullity 5
PASS
```

## Novelty bounds

On 2026-08-26 the run indexes were searched by arXiv id, title, `closed range`,
`Carleson`, `model space`, `star-invariant`, `sampling`, and `Riesz sequence`.
External searches used exact combinations of the same terms and `K_theta`.
They found arXiv:2505.15079, arXiv:1205.3260 on reverse Carleson embeddings,
and arXiv:1709.09762 on model-space interpolation, but no source stating the
noninjective closed-range-to-surjectivity mechanism or the resulting complete
Hilbert dichotomy. The audit is bounded and does not establish priority.

## Artifact checks

- Source PDF: 13 pages; future-work passage located on page 6.
- Evidence image: genuine page-6 render containing the complete model-space
  proposal and its Bergman-pattern prediction.
- Final packet: compile log checked and every page visually inspected after
  the last build.

## Verdict

`candidate_partial_likely_valid`. The most important human-review points are
the boundary-form division identity for `K_theta^p` and the assertion that the
support of a measure annihilated by a continuous analytic function lies in its
zero set.
