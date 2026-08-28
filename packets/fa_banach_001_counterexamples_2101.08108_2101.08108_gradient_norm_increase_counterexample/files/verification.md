# Verification notes

Status: `candidate_counterexample_likely_valid`  
Confidence: 97/100  
Result type: counterexample to one explicit conjectural bullet

## Target and transcription

The target is the fourth bullet of Remark 4.2 on source PDF page 18:

> the L2 norm of D^+- *phi(u(t,.)) is nonincreasing in time.

The screenshot in `figures/open_problem_crop.png` is a direct crop of page 18
of `source_paper.pdf`. The published 2021 Springer version retains the same
statement.

## Adversarial checks

1. **Source hypotheses on phi.** The piecewise function used in the packet is
   `C1` at both junctions: the values and derivatives agree at `0` and `2`.
   Its derivative is bounded, hence it is globally Lipschitz. It is
   nonnegative on `[0,infinity)` and vanishes at zero, exactly as required by
   source hypotheses (1') and (2).

2. **Initial-data hypotheses.** With `0<=rho<=1`, the datum
   `u_0=2-rho/2` lies in `[3/2,2]`, so it is nonnegative, has finite internal
   `L1` norm, and has finite `L-infinity` norm. Here `rho` is the grid
   restriction of a standard smooth compactly supported bump, so its relevant
   discrete derivative norms are finite. It is already an internal grid
   function, and the source projection `P` fixes it.

3. **No Neumann boundary ambiguity.** The bump `rho` is supported a fixed
   positive distance from the boundary. Consequently `v_0=phi(u_0)` and
   `v_t(0)=phi'(u_0) Delta_X v_0` vanish in a grid boundary layer. At time
   zero, the source Neumann Laplacian therefore agrees on their support with
   `sum D_i^- D_i^+`, and ordinary hyperfinite summation by parts has no
   boundary term.

4. **Energy differentiation.** For `v=phi(u)` and
   `E_+=(1/2)||D^+v||_2^2`, the chain rule and grid equation give exactly

   ```text
   E_+'(0)
     = <D^+v_0,D^+v_t(0)>
     = -<Delta_X v_0,v_t(0)>
     = -<Delta_X v_0,phi'(u_0)Delta_X v_0>.
   ```

   The same calculation applies to `D^-`; the two energies agree by a grid
   shift because the profiles vanish in a boundary layer.

5. **Strict sign.** On the set `rho>0`, one has `3/2<=u_0<2` and
   `phi'(u_0)<0`. On `rho=0`, one has `u_0=2` and `phi'(u_0)=0`. A nonzero
   compactly supported grid function cannot have zero grid Laplacian at every
   point of its positive support (use a maximum point and connectedness).
   Therefore at least one strictly positive summand remains and `E_+'(0)>0`.

6. **Norm versus squared norm.** The initial gradient is nonzero, so strict
   increase of `E=(1/2)||D v||_2^2` implies a positive right derivative of the
   norm itself. A differentiable nonincreasing function cannot have such a
   derivative.

7. **Independent exact check.** The script uses the five-node datum
   `(2,2,3/2,2,2)`. It obtains

   ```text
   phi(u) = (0,0,3/8,0,0),
   E(0) = 9/64,
   E'(0) = 45/64 > 0.
   ```

   All arithmetic is performed with exact rational numbers. Mesh scaling
   multiplies the final derivative by a positive power and cannot change its
   sign.

## Scope and novelty audit

- Disproved: only the fourth bullet in source Remark 4.2.
- Unaffected: the first three Dirac-Young-measure bullets and all principal
  theorems of the paper.
- Cheap run indexes had no hit for arXiv:2101.08108 or the target claim.
- The official published version was checked and still states the conjecture.
- Exact-phrase, author/title, gradient-energy, correction, and erratum searches
  on 2026-08-27 found no explicit counterexample or correction.
- Novelty remains provisional because the citation search was bounded.

## Recommended human focus

Check the source's convention for `D^+-` at the domain boundary against the
boundary-layer localization. The localization is designed so that every
reasonable zero-extension or Neumann convention gives the same derivative at
time zero.
