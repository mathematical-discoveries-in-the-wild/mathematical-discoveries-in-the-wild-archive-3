# Verification notes

Status: `candidate_substantial_partial_likely_valid`  
Confidence: 93/100  
Result type: substantial partial result (solved infinite family)

## Target and transcription

The target is Conjecture 1 on source PDF page 9:

> The unique (up to multiplicative factors) positive harmonic function
> associated to the Laplacian operator (H1)--(H5) is h_1 in Theorem 1.

The screenshot in `figures/conjecture_1_crop.png` is a direct crop of page 9
of `source_paper.pdf`.

## Adversarial checks

1. **Killing convention.** For `i,j >= 1`, a small step can hit an axis but
   cannot overshoot it. Extending `ij` by zero on the complement therefore
   agrees with `(i+X)(j+Y)` at every possible one-step endpoint. No hidden
   boundary correction is missing.

2. **Moment calculation.** Square symmetry gives `E X = E Y = 0` and
   `E[XY]=beta-beta-beta+beta=0`. Hence
   `E[(i+X)(j+Y)]=ij`, including the boundary-adjacent cases.

3. **Kernel boundary terms.** With the source convention
   `K=xy-sum p_{k,l}x^(1-k)y^(1-l)`, direct substitution gives
   `K(x,0)=-alpha*x-beta*(x^2+1)` and `K(0,0)=-beta`. Combining these with
   `H(x,0)=1/(1-x)^2` produces
   `K H=-(psi(x)+psi(y))/2`. The sign was checked against the source's simple
   walk formula; under the source's positive-derivative Riemann-map
   normalization, its `h_1` may be a negative scalar multiple of the positive
   representative. Conjecture 1 is explicitly only up to multiplicative
   factors, so the result concerns the line spanned by `h_1`.

4. **Boundary-value identification.** On the kernel curve, `y=conj(x)` and
   `K=0`, whence `psi(x)+psi(conj(x))=0`; real coefficients make this exactly
   `Re psi(x)=0`. Also

   ```text
   psi'(x) = 2(alpha+2 beta)(x+1)/(1-x)^3.
   ```

   The bounded kernel domain lies in the unit disk, and irreducibility excludes
   `-1` from its boundary, so there is no critical point in its closure. The
   sole pole is the double pole at the corner `1`; square symmetry gives corner
   angle `theta=pi/2`. There can be no extra interior component of
   `Re psi=0`: it cannot close by the maximum principle, meet the smooth
   boundary by local injectivity, or end away from the pole. The resulting map
   is proper. For `beta>0`, the regular-value equation `psi(x)=beta` reduces
   to `2(alpha+2 beta)x=0`, so the proper degree is one. For `beta=0`, the two
   roots over any positive regular value are reciprocal and exactly one lies
   in the unit disk. The degree-one proper-map step identifies `psi`, up to
   positive scale, with the paper's unique Riemann map to the right half-plane.
   This is also consistent with the source small-step formula
   `2 T_(pi/theta)(mu(x))`, since `T_2` is quadratic.

5. **Degenerate parameters.** `alpha>0` guarantees irreducibility. `beta=0`
   is allowed: after removing holding, the kernel curve is the simple-walk
   curve and the displayed `psi` is a positive multiple of
   `x/(1-x)^2`. `gamma` changes the harmonic equation only by a positive
   scalar and causes no new case. The excluded case `alpha=0` splits the walk
   into parity classes and does not satisfy the intended irreducibility.

6. **Coefficient extraction.** The source uses `P_1(X)=X`, so
   `H_1=(psi_1(x)+psi_1(y))/K`. If `psi_1=c psi`, the kernel identity gives
   `H_1=-2c/((1-x)^2(1-y)^2)`, hence `h_1(i,j)=-2cij`. There is no asymptotic
   or formal-series gap.

7. **Positive uniqueness input.** The law has finite support and zero drift,
   so it satisfies the high-moment hypotheses of the standard uniqueness
   theorem cited by the source immediately before Conjecture 1. The new work
   identifies the source generator with that known positive ray; it does not
   reprove Martin-boundary uniqueness.

## Scope and novelty audit

- Proved: the full square-symmetric small-step family, with optional holding.
- Not proved: general asymmetric small-step laws; non-small-step laws allowed
  by the source; uniqueness beyond the standard theorem's hypotheses.
- Cheap run indexes had no hit for arXiv:2012.08947 or this theorem.
- Bounded web/arXiv queries on 2026-08-27 found the original paper and its
  separate simple and king examples, but no explicit family theorem.
- Novelty confidence is provisional because no exhaustive citation search was
  performed.

## Recommended human focus

Check the proper-map/argument-principle sentence in Lemma 1 against the precise
orientation of the source kernel domain. The boundary identity, derivative,
corner order, and coefficient algebra are explicit and independently
checkable.
