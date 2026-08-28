# Verification report

Status: `candidate_full_result_likely_valid`

## Claim audited

For harmonic underdamped Langevin dynamics with friction `gamma > 2` and the
rank-one orthogonal Mori projection onto the position observable `q`, the
optimal positive asymptotic `L^2` decay exponent changes from

```text
a = (gamma - sqrt(gamma^2-4))/2
```

for the centered Markov semigroup to exactly `2a` for the orthogonal semigroup
on `QH` modulo constants. The fluctuation force is `exp(-gamma t)p` and the
memory kernel is `-exp(-gamma t)`.

## Adversarial checks

1. **Source-convention check.** The source estimate is written with
   `exp(-lambda t)` but the open-problem prose says a smaller `lambda` means a
   larger gap and faster decay. These statements are incompatible. The packet
   does not silently inherit the mismatch: positive gaps satisfy `g_Q=2g>g`,
   while signed spectral edges satisfy `s_Q=-2g<s=-g`.

2. **Genuine degeneracy.** The diffusion matrix has rank one in the
   two-dimensional phase space. The Kalman span of `e_p` and `B e_p` is all of
   `R^2`, so the model is hypoelliptic rather than reducible.

3. **Invariant measure.** With
   `B=[[0,1],[-1,-gamma]]` and noise covariance
   `2 gamma e_p e_p^T`, the Lyapunov equation
   `B+B^T+2 gamma e_p e_p^T=0` holds. Hence the standard Gaussian is
   invariant, and `q,p` are orthonormal in the first Wiener chaos.

4. **No hidden normality assumption.** The first-chaos matrix is generally
   nonnormal. The proof uses Wick exponential vectors to obtain the exact
   second-quantization identity. It uses operator norms, not only the
   eigenvalues of a nonnormal matrix.

5. **Sharp original rate.** The centered semigroup norm is exactly the norm
   of its first-chaos restriction because the `n`th chaos norm is the `n`th
   power of a contraction norm. Diagonalizability for `gamma>2` gives both
   upper and lower bounds of order `exp(-a t)`, so `a` is optimal.

6. **Compression check.** `Kq=p` and `Kp=-q-gamma p`. Since `P` projects onto
   `q`, `QKQ p=-gamma p`. The projection is zero on every chaos of degree at
   least two and the generator preserves chaos degree, so those blocks are
   unchanged. Therefore
   `QH intersect 1^perp = span{p} direct-sum (sum_{n>=2} H_n)`.

7. **Sharp orthogonal rate.** The exact block norm is
   `max(exp(-gamma t), ||S(t)||^2)`. Since `gamma>2a`, its optimal exponent is
   `2a`. A tensor square of a slow first-chaos eigenvector supplies the lower
   bound, so this is not merely a hypocoercive estimate.

8. **Force and memory signs.** `QKq=p`, hence
   `F(t)=exp(tQKQ)p=exp(-gamma t)p`. With the source convention
   `M(t)=<q,K F(t)>` and `<q,q>=1`, one obtains
   `M(t)=-exp(-gamma t)`. The sign and normalization have both been checked.

9. **Boundary and scope check.** The theorem assumes `gamma>2`; the critical
   value has a Jordan block and would require separate polynomial-prefactor
   language. Underdamped `0<gamma<2`, higher-dimensional potentials,
   infinite-rank Zwanzig projections, and singular potentials are not claimed.

10. **Domain check.** Polynomial chaoses form a core for this Gaussian
    Ornstein-Uhlenbeck generator. The rank-one term is controlled by
    `<Kf,q>=<f,K^*q>` with `K^*q=-p`, hence it is bounded on `L^2`. The
    orthogonal generator is therefore the closure of the displayed block
    operator and generates the direct-sum contraction semigroup used in the
    proof.

## Computational regression

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2109.01990_harmonic_langevin_orthogonal_gap_doubling/code/check_chaos_spectrum.py \
  --max-degree 10
```

Tested frictions: `2.1, 2.5, 3, 5, 10`.

For each friction, the script checks:

- normalized product-Hermite generator matrices through total degree 10;
- every eigenvalue against `-(m a+n b)`;
- semigroup singular norms against the exact symmetric tensor power formula
  at times `0.07, 0.4, 1.3`;
- the compressed first-chaos generator;
- the fluctuation-force and memory-kernel formulas; and
- the retained finite-chaos spectral edge against `-2a`.

Result: all checks passed. Floating-point tolerance is `1e-6`; the looser
tolerance accommodates ill-conditioning of high nonnormal chaos matrices near
critical damping. The computation is not used as proof.

## Bounded novelty audit

- Searched the four cheap run indexes for arXiv:2109.01990, the exact title,
  hypocoercivity, Mori-Zwanzig orthogonal dynamics, and close spectral-gap
  phrases. No duplicate was found.
- Searched the web/arXiv by exact id/title and combinations of `lambda_Q`,
  `larger spectral gap`, `orthogonal dynamics`, `harmonic Langevin`, and
  `underdamped Langevin`.
- Inspected the relevant harmonic-example passages in arXiv:2604.20453 and
  2607.25855, and the Mori-semigroup results in arXiv:2503.20457. Their results
  concern well-posedness, deterministic oscillators, or infinite-rank
  Zwanzig projections, not the exact stochastic Mori gap comparison here.
- No exact duplicate was found as of 2026-08-26. This is a bounded audit.

## Human-review recommendation

Review the Wick-exponential derivation of the second-quantization identity and
the closure/core sentence identifying the direct-sum block generator. Also
confirm that Section 5's intended question is the faster-decay/larger-gap
claim, given the source's reversed inequality convention. Subject to that
convention repair, the result appears complete.

