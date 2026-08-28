# Verification Report

Candidate: arXiv:2004.10833, Remark 5.19(c)

## Claim Checked

For every `0 < alpha < 1` and `1 < p < infinity`, `p != 2`, the equality
`^+-W^{alpha,p}(R) = W-tilde^{alpha,p}(R)` conjectured by Feng--Sutton is
false.  Both one-sided spaces are `F^alpha_{p,2}`, whereas the Gagliardo space
is `B^alpha_{p,p}`; explicit lacunary frequency packets distinguish them.

## Verdict

`likely valid`

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source scope | valid | Remark 5.19(c), printed p. 64, asserts the equality for `p != 2`, `0 < alpha < 1`; the same text appears in arXiv:2007.10245. |
| Weak derivative Fourier symbol | valid | Testing against compactly supported smooth functions and Fourier-dualizing gives symbols `(i xi)^alpha` and `(-i xi)^alpha`.  The constructed functions lie in `L^1 cap L^p`, so the source's original testing integral is meaningful. |
| Phase removal | valid | `(+- i xi)^alpha = |xi|^alpha exp(+- i pi alpha sgn(xi)/2)`.  This phase and its inverse are `cos(theta) I` plus or minus `sin(theta) H`; the Hilbert transform is bounded on `L^p` exactly in the asserted interior range. |
| Graph space identification | valid/external | The previous step reduces the graph norm to `||u||_p + ||(-Delta)^(alpha/2)u||_p`, equivalent to the Bessel-potential space `H^{alpha,p}=F^alpha_{p,2}`. |
| Gagliardo identification | valid/external | For `0 < alpha < 1`, `1 < p < infinity`, the double-difference norm is the standard `B^alpha_{p,p}` norm. |
| Sparse packet formula | valid | Disjoint dyadic packets with a common envelope reduce the Triebel--Lizorkin square function to `||a||_2 |eta|` and the Besov sum to `||a||_p ||eta||_p`. |
| Sequence choice | valid | `beta=(1/2+1/p)/2` lies between `1/p` and `1/2`; therefore `k^-beta` belongs to exactly one of `ell^2`, `ell^p`, in the direction stated. |
| Function convergence | valid | The physical-space series is absolutely summable in `L^1` and `L^p` because of the factor `2^(-4 alpha k)` and polynomial `a_k`. |
| Real-valued witness | valid | If both real and imaginary parts belonged to the excluded complexified space, their complex sum would too; hence at least one component is a real witness. |

## Counterexample Search

Small cases checked: no finite computation is probative here.  Finite packet
sums belong to both spaces; the separation is necessarily an infinite
summability effect.

Result: `not applicable`.

## External Dependencies

- M. Riesz boundedness of the Hilbert transform on `L^p`, `1 < p < infinity`:
  standard and correctly applied.
- Littlewood--Paley characterization `H^{alpha,p}=F^alpha_{p,2}`: standard.
- Difference characterization `W^{alpha,p}=B^alpha_{p,p}` for
  `0 < alpha < 1`: standard.
- Independence of Besov/Triebel--Lizorkin norms from the chosen admissible
  dyadic resolution: standard and used to isolate the sparse packets.

## Gaps

- No claim is made for `p=1` or `p=infinity`; the Hilbert-transform argument
  does not extend to those endpoints.
- A full citation-database audit was not available.  Exact-phrase and bounded
  arXiv searches found no explicit later resolution.

## Confidence

Score: `93/100`.

Reason: the proof is a direct reduction to classical, stable function-space
identifications and an explicit `ell^2` versus `ell^p` construction.  The only
meaningful review risk is matching the source's weak testing convention to the
Fourier multiplier without a hidden domain convention; the packet handles
this on witnesses in `L^1 cap L^p`.

## Human Review Recommendation

`send to human`

Check first the Fourier-duality sign convention in Lemma 1 and then the sparse
projection equivalence in Lemma 2.  Neither affects membership if the sign is
reversed, but both should match the source notation exactly.

