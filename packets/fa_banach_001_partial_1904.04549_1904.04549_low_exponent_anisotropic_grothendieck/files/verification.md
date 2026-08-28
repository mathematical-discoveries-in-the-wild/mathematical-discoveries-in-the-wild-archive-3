# Verification Report

## Claim checked

For `p=(p1,...,pm) in [1,2]^m`, every bounded multilinear map from
`ell_1^m` to a Hilbert space is anisotropically multiple `(q;p)`-summing if
and only if `q_k >= p_k` for every `k`.

## Verdict

Substantial partial result likely valid.

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Mixed Minkowski direction | valid | For `r<=s`, `ell_s(ell_r)` is bounded by the transposed `ell_r(ell_s)` norm. Thus swapping an outer 2 with an inner 1 increases the comparison norm, exactly as required. |
| Vertex sorting | valid | Repeated adjacent swaps put all 1-levels outside all 2-levels. The same permutation is applied to the variables and their sequences, preserving `||T||`. |
| Inner block | valid/external | Source Theorem 4.6 at `p=q=2` gives the multiple `(2;2)` estimate into every Hilbert target. The resulting full inner array belongs to a Hilbert `ell_2` sum. |
| Outer block | valid/external | The same theorem at `p=q=1`, applied to the outer multilinear map with that Hilbert target, gives the outer `ell_1` estimate. |
| Degenerate blocks | valid | If there are no 1-levels or no 2-levels, only the corresponding endpoint theorem is used. |
| Weak-space interpolation | valid/external | For finite sequences, `ell_p^{w,N}(ell_1)=ell_p^N tensor_epsilon ell_1`. The injective interpolation result used in arXiv:1805.12500 gives `[W_1^N,W_2^N]_theta=W_p^N` with constants uniform in `N`. |
| Coordinatewise interpolation | valid | All cube vertices have uniform bounds. Interpolating one coordinate and its mixed output level at a time yields every point of `[1,2]^m`; vector-valued `ell_p` interpolation handles the nested output. |
| Infinite sequences | valid | Constants are independent of truncation length, so taking the supremum over finite truncations proves the full inequality. |
| Real scalars | valid | Complexification changes only a constant depending on multilinearity degree, not the coincidence statement. |
| Output monotonicity | valid | Increasing any mixed exponent decreases that level's counting-measure sequence norm; iterating gives `||a||_q <= ||a||_p` coordinatewise. |
| Necessity | valid | A rank-one product map with one nontrivial coordinate reduces the claimed inequality to the scalar inclusion `ell_{p_k} subset ell_{q_k}`, forcing `p_k<=q_k`. |
| High-exponent Hadamard obstruction | valid | Sylvester orthogonality gives `T_N(x_i,e_j)=delta_ij`; the outer mixed norm is `N^(1/q_k)` while the weak norms are at most `N^max(1/p_k-1/2,0)` and exactly `N^(1/p_l)`. Comparing powers proves the ordered pairwise inequality. |

## Computational regression

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1904.04549_low_exponent_anisotropic_grothendieck/code/verify_mixed_norm_reductions.py
```

The script checks 2,000 random arrays for every dimension from two through
five. It verifies the adjacent Minkowski swap, complete vertex sorting,
coordinatewise mixed-norm monotonicity, and the finite Sylvester identities
and weak-norm bounds in the high-exponent obstruction. This is a
direction/order check, not a proof of the operator theorem.

## Scope audit

- The theorem covers every anisotropic tuple with all input exponents in
  `[1,2]`, without ordering or equality assumptions.
- It is exact in that regime.
- It gives a new necessary condition for tuples with an input exponent above
  2, but does not give a complete high-exponent classification.
- Bounded local and primary arXiv searches found no duplicate theorem.

Confidence: proof 93/100; novelty 82/100.

Human review recommendation: send to human, prioritizing uniform injective
interpolation in the weak sequence spaces.
