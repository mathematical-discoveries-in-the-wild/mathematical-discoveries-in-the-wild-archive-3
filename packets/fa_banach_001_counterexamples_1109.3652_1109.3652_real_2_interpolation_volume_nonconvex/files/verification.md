# Verification report

Verdict: `candidate_counterexample_likely_valid_full_negative_answer`

Model: `GPT5.6`

## Source-target verification

- The local source PDF is arXiv:1109.3652 by Cordero-Erausquin and Klartag.
- Conjecture 10 appears on PDF page 11 in the section on real
  interpolations.
- It asks for convexity of the logarithmic partition function for real
  2-interpolations whose endpoints are even, convex, and 2-homogeneous.
- The surrounding text explicitly says these properties propagate along the
  interpolation.  The candidate family has them at every time.
- The nearby Fact 11 proves only a special midpoint statement for the dual
  pair `f` and `Lf`; it does not answer Conjecture 10.

## Geometric calculation audit

For the inverse Gauss parametrization

`X(theta) = h(theta)n(theta) + h'(theta)t(theta)`

and `q = h+h''`, direct differentiation gives `X' = q t` and
`det(X,X') = hq`.  On the boundary of `K`, for
`F = norm_K^2 / 2`, homogeneity and tangential differentiation give

- `Hess F(X,X) = 1`,
- `Hess F(X,X') = 0`, and
- `Hess F(X',X') = q/h`.

For `u(rX(theta)) = r^2 a(theta)`, the squared dual Hessian norm is therefore

`r^2 (4a^2 + (h/q)(a')^2)`.

The cone-coordinate Jacobian is `r hq`.  Using the exact radial integrals
`1`, `2`, and `8` for powers `r`, `r^3`, and `r^5` against
`exp(-r^2/2)`, and using `integral a hq = 0`, gives

- `Var(u) = 8D/M`,
- `integral energy = 2(4D+A)/M`, and hence
- `alpha'' = (A-4D)/M`.

The factors and sign were independently rederived in ordinary polar
coordinates.  In particular, `alpha = -log Z` gives
`alpha'' = E(F_tt) - Var(F_t)`, and the 2-interpolation PDE contributes the
factor one half in front of the Hessian energy.

## Exact symbolic audit

`code/verify_rayleigh.py` checks symbolically that, for
`h = 1 + epsilon cos(4 theta)` and `a = cos(2 theta)`,

- `M = pi(2 - 15 epsilon^2)`,
- `integral a hq = 0`,
- `A = pi(4 - 4 epsilon + 2 epsilon^2)`,
- `D = pi(1 - 7 epsilon - 15 epsilon^2/2)`, and
- `A-4D = 8 pi epsilon(3+4 epsilon)`.

The script runs with exact rational arithmetic and assertions.  At
`epsilon = -1/100` it returns exactly `-148*pi/625`.  Also
`h >= 99/100` and `q >= 17/20`, so the body is analytic and strictly convex
with a comfortable positivity margin.

## PDE realization audit

Writing `F(t,x) = r^2 f(t,phi)` in Euclidean polar coordinates gives the
spatial Hessian matrix

`[[2f, f_phi], [f_phi, 2f+f_phiphi]]`

in the polar orthonormal frame.  Substituting
`grad(F_t) = r(2v,v_phi)`, with `v=f_t`, into the interpolation equation gives
exactly the angular PDE displayed in `main.tex`.  Its denominator is the
Hessian determinant.  At the initial datum it is positive.

The equation is analytic and solved explicitly for `f_tt`; it may contain
`f_phiphi` and `f_tphi`, as allowed by the Cauchy--Kowalevski theorem.  The
initial body, the change from normal angle to Euclidean polar angle, and the
speed are analytic because `hq>0`.  Local analytic solutions on angular
charts agree by uniqueness; compactness of the circle yields a uniform time
interval.  Periodicity follows by uniqueness.  Positivity of the Hessian and
of `f` persists after shrinking the interval.

The reduced ansatz makes 2-homogeneity automatic.  Reflection symmetries of
both Cauchy data are preserved by uniqueness, so every time slice is even and
unconditional.  Choosing a closed smaller interval inside the analytic
existence interval avoids an endpoint-regularity issue before rescaling to
`[0,1]`.

## Regularity caveat

A globally twice differentiable exactly 2-homogeneous function is quadratic.
The source nevertheless formulates Conjecture 10 for arbitrary norm squares,
so the only nontrivial reading is smooth strong convexity away from the
origin.  The candidate answers that intended conjecture.  A human reviewer
should explicitly confirm this interpretation before publication.

## Computational reproduction

Run:

`conda run --no-capture-output -n sandbox python code/verify_rayleigh.py`

from the packet directory.  No floating-point calculation is used.

## Remaining review risk

No mathematical gap is currently known.  The most non-elementary step is
standard analytic local existence and periodic patching.  Novelty is not
certified; see `novelty_search.md`.
