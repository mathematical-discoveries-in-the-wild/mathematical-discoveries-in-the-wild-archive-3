# Verification report

## Claim checked

Under the exact assumptions of Problem 1 in arXiv:2305.04353, the existence
of a tight tangent parabola at every interior point implies 3-convexity.

## Logical checks

1. **Symmetric cancellation.** Writing
   `P_c(x)=f(c)+f'(c)(x-c)+A_c(x-c)^2`, the tight inequalities at `c-h` and
   `c+h` give `2h f'(c)<=f(c+h)-f(c-h)`. No second derivative of `f` and no
   bound on `A_c` is used.
2. **Local upper bound.** On a compact interval strictly inside `int I`, use
   one fixed admissible `h`. Continuity bounds the central secants uniformly,
   hence bounds `f'` from above.
3. **BV sign.** If `f'<=M`, the mean value theorem shows that `f-Mx` is
   nonincreasing. Therefore `f` is BV and the singular part `nu` in
   `Df=f' dx+nu` is a nonpositive measure. Because `f` is differentiable
   everywhere in the interior, the absolutely continuous density is the
   classical derivative almost everywhere.
4. **Mollification direction.** For a nonnegative mollifier,
   `f_epsilon'=f'*rho_epsilon+nu*rho_epsilon<=f'*rho_epsilon`. Convolution of
   the pointwise central-slope inequality gives
   `f'*rho_epsilon<=A_h f_epsilon`; hence the same inequality holds for
   `f_epsilon`. The sign is in the required direction.
5. **Smooth limit.** Taylor expansion gives
   `A_h f_epsilon=f_epsilon'+h^2 f_epsilon'''/6+o(h^2)`, so
   `f_epsilon'''>=0`. Smooth functions with nonnegative third derivative have
   nonnegative third divided differences. Local uniform convergence transfers
   this to every interior quadruple; continuity handles interval endpoints.

## Stress checks

- The proof does not invoke the source's `C^1` midpoint characterization;
  that would add a hypothesis absent from Problem 1.
- Possible singular BV behavior is not discarded. It is retained as `nu` and
  its nonpositive sign is exactly what makes the regularization inequality
  work.
- The parabola coefficient may depend arbitrarily on the point and may be
  unbounded. It cancels before the regularity argument.
- Degenerate intervals are irrelevant; 3-convexity is tested on four distinct
  ordered points.

## Artifact checks

- Source PDF: 20 pages; Problem 1 located on source page 9.
- Evidence image: real crop rendered from page 9, containing the definition
  and the complete question.
- Final PDF: compile log and every rendered page checked after final build.

## Novelty bounds

On 2026-08-26 the run registry, solution index, and attempts index were
searched by arXiv id, title, and the phrases `tight tangent parabola` and
`3-convex`. External exact-phrase searches used the arXiv id, full title,
quoted Problem 1 text, authors, and the same core terms. They returned the
source arXiv/journal versions but no distinct later paper explicitly claiming
a resolution. This is not an exhaustive priority search.

## Verdict

`full_solution_likely_valid`. The result is ready for expert review. The most
important review point is the local distributional-derivative decomposition
and its use under nonnegative convolution.
