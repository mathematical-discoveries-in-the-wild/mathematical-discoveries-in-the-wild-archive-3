# Verification report

## Verdict

**Likely valid as a substantial partial theorem.** The proof is exact and
non-numerical. The bounded-compression lemma is fully general, its Doss and
regular-Lagrangian-flow applications have been checked against their stated
hypotheses, and the packet completely treats the stated structured
one-interface classes. The source's literal general rough-driver fixed-point
problem remains outside the claim.

## Bounded-compression theorem

| Step | Status | Adversarial check |
| --- | --- | --- |
| Tonelli interchange | valid | The integrand is nonnegative and measurable, so no prior integrability is needed. |
| Use of compression | valid | The pushforward inequality bounds the initial-point integral at each time by `L` times Lebesgue integration over the common range. |
| Kernel integral | valid | The exponent is `n-1+s<n` exactly for `s<1`; polar integration gives `C R^(1-s)/(1-s)` uniformly in the measure point `z`. |
| Local finiteness of `D phi` | valid | `U` is bounded with compact closure and `phi in BV_loc`, hence `|D phi|(U)<infinity`. |
| One null set for all `s` | valid | Prove the result for a countable sequence `s_j↑1`. On bounded distances, every lower-exponent kernel is bounded by a constant times `1` plus a higher-exponent kernel. |
| Matrix coefficients | valid | There are finitely many entries, so their full-measure sets may be intersected. |

## Doss-flow application

| Step | Status | Adversarial check |
| --- | --- | --- |
| Compression | valid | `Phi_t=f∘translation∘f^{-1}` has inverse Lipschitz constant at most `Lip(f)Lip(f^{-1})`, uniformly in `t`; therefore `Leb(Phi_t^{-1}(A))≤C Leb(A)`. |
| Bounded range | valid | On a bounded initial ball, `f^{-1}(B)` is bounded; adding compact `Y([0,T])-Y_0` and applying Lipschitz `f` preserves boundedness. |
| No circularity | valid | The explicit Doss formula defines the path first. Compression proves variability; the bi-Lipschitz `BV` composition estimate in the second half of source Lemma 5.7 then transfers it to the Doss coordinate, after which source Theorem 2.13 proves the integral equation. |
| Match to Definition 3.1 | valid | The Doss path is `gamma`-Hölder and variable for all `s<1`, so choose `(1-gamma)/gamma<s<1`. |
| Scope | valid with explicit qualifier | The conclusion is for almost every initial point. The exceptional set may depend on `sigma` and `Y`, and the construction still uses Doss. |

## Ambrosio-flow application

| Step | Status | Adversarial check |
| --- | --- | --- |
| Spatial regularity | valid | A bounded linear combination of the `BV_loc` columns is in `BV_loc`; time coefficients are integrable. |
| Divergence | valid | `div b_t=sum_k dotY_t^k div sigma^(k)` belongs to `L^1_t L^infinity_x`. |
| Growth | valid | Global boundedness of `sigma` and `dotY in L^infinity` supplies Ambrosio's standard growth hypothesis. |
| Compression and range | valid | The regular Lagrangian flow has uniform bounded compression, and bounded velocity keeps trajectories from a bounded initial set in a common bounded set. |
| Solution notion | valid with explicit qualifier | The conclusion is uniqueness in the regular-Lagrangian-flow class for almost every initial point, not pointwise ODE uniqueness at every start. |
| Match to source definition | valid | Trajectories are Lipschitz (`alpha=1`); view `Y` as `C^gamma`, `gamma<1`, and choose `s>1-gamma`. |

## Rough clock-row theorem

| Step | Status | Adversarial check |
| --- | --- | --- |
| One-sided fixed points | valid | `sigma_± ∈ C_b^2` is more than enough for standard Young ODE existence and uniqueness when `gamma>1/2`. The packet includes the local contraction estimate and bounded-field continuation argument. |
| Predetermined crossing | valid | Multiplication by `nu^T` turns either one-sided equation into the constant-integrand identity `h(X_t)=h(x_0)+lambda·(Y_t-Y_0)`. Thus the branch used in construction agrees with the branch selected by `X`. |
| Concatenation at the jump | valid | There is at most one crossing. Both one-sided Young solutions meet continuously. A one-point choice of coefficient representative has zero integral against continuous `Y`; additivity gives the global equation. |
| Uniqueness | valid | Every solution has the same normal clock and hence the same switching time. Young uniqueness applies separately before and after it. |
| Local `BV` structure | valid | The distributional derivative consists of bounded bulk gradients in the two half-spaces plus the trace jump times `nu H^{n-1}|_H`. |
| Hyperplane potential | valid | Tangential scaling gives `∫_{R^{n-1}} (|w|²+d²)^(-(n-1+s)/2) dw = C d^{-s}` for `s>0`; the `n=1` case is the corresponding point mass. |
| Time integrability | valid | Bi-Lipschitz crossing gives `d(X_t,H)≥m|t-tau|`; hence the `p`th power is locally `|t-tau|^{-sp}`, integrable exactly for `sp<1`. |
| Match to source definition | valid | The solution is `gamma`-Hölder and is `(s,1)`-variable for every `s<1`. Since `gamma>1/2`, one may choose `(1-gamma)/gamma < s < 1`, giving `gamma*s+gamma>1`. |

## Equality with the source integral

The construction first defines the integral as the sum of ordinary Young
integrals on the two sign intervals. Once variability is established, the
source generalized Lebesgue–Stieltjes integral exists. On each sign interval
the integrand is Hölder, so the definitions agree; the source restriction
property and continuity of `Y` permit concatenation across the unique jump.
Changing the coefficient value at the one crossing time has no effect.

## Schauder theorem

| Step | Status | Adversarial check |
| --- | --- | --- |
| Candidate set | valid | Fixed initial value, uniform Lipschitz bound, and a lower normal-increment inequality define a nonempty closed convex equicontinuous set; Arzelà–Ascoli gives compactness in `C([0,T])`. |
| Self-map | valid | The velocity bound and common positive normal velocity integrate directly to the two candidate inequalities. |
| Continuity despite the jump | valid | A limit candidate has strictly increasing signed distance and contacts the interface at most once. Away from that null time the side stabilizes under uniform convergence; dominated convergence gives uniform convergence of Picard images. |
| Existence | valid | Ordinary Schauder applies to the continuous self-map of a nonempty compact convex set. |
| Uniqueness | valid | Any solution has strictly increasing signed distance. Before the common first hit, two solutions solve the same locally Lipschitz one-sided ODE and agree by Gronwall; they then have the same hit and agree on the other side. |
| Variability | valid | The same bulk-plus-hyperplane measure bound and linear normal crossing imply `sp<1`. |

## Sharpness and scope

- For a nonzero jump at a linear crossing, the potential is also bounded below
  by a constant times `|t-tau|^{-s}`. Thus `sp<1` is sharp.
- The rough theorem requires a single flat interface, smooth one-sided
  branches, a common normal row, and a monotone bi-Lipschitz driver projection.
- The absolutely continuous theorem allows state-dependent normal motion but
  does not cover a fully rough driver.
- The companion matrix example confirms that ellipticity and the source Doss
  assumptions alone cannot substitute for output transversality.
- With `Y=(B,B)`, every initial point on the example's jump hyperplane has a
  solution trapped in that hyperplane and no variability solution. This
  proves that the almost-everywhere qualifier in the compression theorem is
  genuine rather than an artifact of the proof.

## Human-review focus

The main points for expert review are (1) the exact invocation of the source's
Doss chain rule after variability has been established, (2) the standard
global hypotheses in the quoted Ambrosio regular-flow theorem, and (3) the
agreement between the piecewise Young integral and the source fractional
integral at one jump. None affects the elementary bounded-compression energy
estimate itself.
