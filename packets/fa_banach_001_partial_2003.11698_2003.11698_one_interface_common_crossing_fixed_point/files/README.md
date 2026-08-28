# Variability from bounded compression and transversal fixed points

- **Source:** Michael Hinz, Jonas M. Tölle, and Lauri Viitasaari,
  *Variability of paths and differential equations with BV-coefficients*,
  arXiv:2003.11698; Ann. Inst. H. Poincaré Probab. Statist. 59 (2023),
  2036–2082.
- **Source target:** the open problem on replacing the Doss transform by
  standard fixed-point arguments, specifically by proving under reasonable
  assumptions that the integral process is variable (PDF p. 6, Section 1.2).
- **Status:** candidate substantial partial result, likely valid. It proves a
  generic-start theorem for the source's full multidimensional Doss class, a
  non-Doss regular-flow theorem, and complete pointwise fixed-point results for
  structured one-interface classes. It still does not give the requested
  general rough-driver fixed-point theorem at every prescribed start.
- **Model:** GPT5.6.

## Main result: bounded compression

Let `Phi_t(x)` be a measurable family of trajectories whose time slices push
Lebesgue measure forward with density bounded uniformly in time, and suppose
bounded initial sets have bounded trajectory range. Then, for every
`phi in BV_loc`, Tonelli gives

```text
∫_B E_s(x) dx
 ≤ L T ∫_U ∫_K |y-z|^(-n+1-s) dy |D phi|(dz) < infinity
```

for every `s<1`. The last inequality is exactly local integrability of the
Riesz kernel, since `n-1+s<n`. Consequently, for almost every initial point,
the trajectory is `(s,1)`-variable simultaneously for every `s<1` and every
entry of a finite matrix coefficient.

Two applications follow.

1. The source's Doss flow is a bi-Lipschitz conjugate of translations and
   hence has uniform bounded compression. Under the paper's full
   multidimensional Doss hypotheses, for arbitrary `gamma`-Hölder `Y` with
   `gamma>1/2`, the Doss trajectory is a variability solution for almost every
   initial point—without any driver occupation, upper-regularity, or
   Riesz-energy hypothesis.
2. If a bounded `BV_loc` matrix has bounded distributional divergence in
   every column and `Y` is Lipschitz, Ambrosio's theorem supplies a unique
   regular Lagrangian flow with bounded compression. Almost every trajectory
   is therefore a variability solution. This application uses no Doss map,
   invertibility, curl-free inverse, or angle condition.

The generic qualifier is sharp: the explicit uniformly elliptic jump example
has an entire exceptional hyperplane of starting points whose solutions remain
in the jump set and fail every positive variability class.

## Pointwise Young–Picard theorem

Let a bounded matrix coefficient be `C_b^2` on each side of one hyperplane and
allow a genuine jump across that hyperplane. Suppose both one-sided branches
have the same normal row `lambda`, and suppose the scalar driver projection

```text
h(x_0) + lambda · (Y_t - Y_0)
```

is an increasing bi-Lipschitz clock. For every Hölder driver of exponent
`gamma > 1/2`, the discontinuous equation has a unique solution obtained by
standard Young–Picard fixed points: solve the smooth minus equation before the
clock crosses zero and the smooth plus equation afterward. The jump-potential
estimate gives

```text
X ∈ V(sigma, s, p) whenever s p < 1.
```

For `p=1`, choose `(1-gamma)/gamma < s < 1`; this is exactly a variability
solution in the source paper's sense. Tangential driver coordinates may remain
genuinely Hölder-rough.

## Pointwise Schauder theorem

For absolutely continuous drivers, the common-row identity can be replaced by
a state-dependent common-crossing inequality: both one-sided velocities have
normal component at least `c>0`. Candidate paths with normal speed at least
`c` form a compact convex set. They meet the interface at most once, so the
otherwise discontinuous global Picard map is continuous by dominated
convergence. Schauder gives a fixed point, one-sided Gronwall gives uniqueness,
and the same Riesz estimate gives the sharp range `s p < 1`.

## What this does not answer

This is not the literal full solution of the source question. The generic
rough-driver theorem still constructs paths by Doss, not by a standard fixed
point. The non-Doss theorem is for Lipschitz time drivers and almost every
initial point. The standard fixed-point theorems are pointwise and allow rough
drivers, but impose a single-interface crossing geometry. The packet labels
the result substantial partial rather than full for precisely these reasons.

## Human-review recommendation

Prioritize review of the bounded-compression theorem and its Doss application:
the estimate is elementary, the scope gain is large, and source Lemma 5.7
supplies the final change-of-variables step without circularity. Next verify
the standard time-dependent hypotheses in the Ambrosio corollary. The two
interface fixed-point theorems have already undergone a separate adversarial
audit recorded in `verification.md`.

## Files

- `solution_packet.pdf`: rendered expert-facing packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: local copy of the source paper.
- `supporting_ambrosio_2004_overview.pdf`: open-access overview of the regular
  Lagrangian flow theorem used in the non-Doss corollary.
- `figures/open_problem_crop.png`: direct crop of the source question.
- `verification.md`: adversarial proof audit.
- `novelty_search.md`: bounded duplicate and literature search.

Ledger:
`runs/fa_banach_001/ledger/results/2003.11698_one_interface_common_crossing_fixed_point.json`.
