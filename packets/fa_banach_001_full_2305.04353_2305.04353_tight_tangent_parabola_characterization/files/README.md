# Full solution packet: tight tangent parabolas characterize 3-convexity

## Source

- Dan-Stefan Marinescu and Constantin P. Niculescu, *Old and new on the
  3-convex functions*, arXiv:2305.04353 (2023).
- Problem 1, page 9: whether a continuous function on an interval,
  differentiable in its interior and admitting a tight tangent parabola at
  every interior point, must be 3-convex.
- Model: GPT5.6.

## Classification

- Status: `full_solution_likely_valid`.
- Result type: full affirmative solution of Problem 1 as stated.
- Human review is recommended, especially for the local BV/mollification
  bridge that removes the tempting but unjustified extra `C^1` assumption.

## Result

Yes. If `P_c` is a tight tangent parabola at the midpoint `c` of
`[c-h,c+h]`, its quadratic term cancels between the symmetric endpoints.
The one-sided graph inequalities give

```text
f'(c) <= (f(c+h)-f(c-h))/(2h).                         (*)
```

On each compact interior interval, one fixed radius in `(*)` bounds `f'`
from above. The mean value theorem then makes `f-Mx` nonincreasing, so `f` is
locally BV and its distributional derivative decomposes as
`Df=f' dx+nu` with `nu<=0` singular. Nonnegative mollification preserves
`(*)`: the singular term can only decrease the derivative. Taylor expansion
then gives `f_epsilon'''>=0`. Thus every mollification is 3-convex, and passage
to the locally uniform limit proves that `f` is 3-convex.

## Verification and novelty

- `verification.md` checks every implication and identifies the two standard
  real-analysis facts used in the regularization step.
- The evidence crop reproduces the definition and the complete problem from
  page 9 of the source PDF.
- The run indexes had no exact duplicate. Bounded exact-title, exact-question,
  author, and core-keyword searches on 2026-08-26 found only the source and
  its journal version, not a later explicit solution. This is bounded novelty
  evidence, not a priority claim.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: page-9 definition and Problem 1.
- `verification.md`: proof, artifact, and novelty verification report.
