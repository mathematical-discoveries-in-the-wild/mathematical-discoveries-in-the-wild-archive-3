# One-sided weak fractional Sobolev spaces are not Gagliardo spaces for `p != 2`

Status: `counterexample_likely_valid`  
Model: `GPT5.6`  
Source: Feng--Sutton, arXiv:2004.10833v2, Remark 5.19(c), printed p. 64  
Repeated source: Feng--Sutton, arXiv:2007.10245v1, concluding remark (c)

## Result

For every `0 < alpha < 1` and every `1 < p < infinity`, each of the two
one-sided spaces from the source satisfies

`^-W^{alpha,p}(R) = ^+W^{alpha,p}(R) = H^{alpha,p}(R) = F^alpha_{p,2}(R)`

with equivalent norms.  The Gagliardo--Slobodeckij space in the conjecture is

`W-tilde^{alpha,p}(R) = B^alpha_{p,p}(R)`.

These spaces coincide when `p=2`, but not when `p != 2`.  More precisely:

- if `2 < p < infinity`, there is a real function in the Gagliardo space but
  in neither one-sided weak-derivative space;
- if `1 < p < 2`, there is a real function in both one-sided spaces but not in
  the Gagliardo space.

Thus the conjectured equality in Remark 5.19(c) is false for every interior
exponent `p != 2`.

## Proof mechanism

On the real line, the source's left and right weak fractional derivatives have
Fourier symbols `(i xi)^alpha` and `(-i xi)^alpha`.  Each is a unimodular phase
times `|xi|^alpha`.  The phase and its inverse are linear combinations of the
identity and the Hilbert transform, so their `L^p` graph norms are equivalent
to the Bessel-potential norm for `1 < p < infinity`.

To separate this `F^alpha_{p,2}` norm from the Gagliardo
`B^alpha_{p,p}` norm, take a fixed band-limited Schwartz envelope `eta` and
put frequency packets at scales `2^(4k)` with amplitudes
`a_k 2^(-4 alpha k)`.  Littlewood--Paley membership is then exactly
`(a_k) in ell^2`, while Gagliardo/Besov membership is exactly
`(a_k) in ell^p`.  Choosing `a_k = k^(-beta)` with `beta` strictly between
`1/2` and `1/p` gives the required witness in the appropriate direction.

## Verification and scope

The verifier report checks the weak/distributional Fourier identity, the
Hilbert-transform inverse, the two classical function-space identifications,
the sparse packet calculation, convergence in `L^1 cap L^p`, and passage to a
real-valued witness.  No numerical computation is used in the proof.

The result does not settle the endpoint cases `p=1` or `p=infinity`, the
source's separate comparison with its Fourier-`L^p` space, or the finite-domain
conjecture in Remark 5.19(d).

The bounded novelty search covered all four run indexes, exact source wording,
the repeated arXiv:2007.10245 formulation, exact-title/author/core-term arXiv
searches, and the later visible Feng--Sutton arXiv work.  It found no later
paper explicitly resolving this exact conjecture.  The ingredients are
classical, so novelty confidence is moderate: the contribution is the precise
operator identification and explicit packet counterexample for this source
conjecture, not a new general separation theorem for Besov and
Triebel--Lizorkin spaces.

Human review recommendation: `send_to_human`.  The main review point is the
distributional identification of the source's weak derivative with the
one-sided Fourier multiplier on the packet witnesses.

The final four-page PDF compiled without warnings, every page was visually
inspected, and its SHA-256 is
`4c7acf677fc462994a149c35123fdd280b5f8503d50d53ec32f40136041cb55f`.
