# The positive generator for reflection-symmetric small-step walks

Status: `candidate_substantial_partial_likely_valid`.

Source: V. H. Hoang, K. Raschel, and P. Tarrago, *Constructing discrete
harmonic functions in wedges*, arXiv:2012.08947v2 (2023). The target is
Conjecture 1 on source PDF page 9.

## Claimed result

Conjecture 1 holds for every irreducible small-step law in the quarter plane
that is invariant under the full symmetry group of the square. Write

```text
p(+-1,0) = p(0,+-1) = alpha,
p(+-1,+-1) = beta,
p(0,0) = gamma,
4 alpha + 4 beta + gamma = 1,
```

with `alpha > 0` and `beta,gamma >= 0`. Then the source paper's first
generator `h_1` is a nonzero scalar multiple of

```text
h(i,j) = i j  (i,j >= 1),   h = 0 off the open quadrant.
```

Consequently, the line spanned by `h_1` contains the unique positive killed
harmonic function. This gives a continuous family containing the simple walk,
the king walk, all mixtures of their step laws, and lazy versions.

The key exact formula is the conformal coordinate

```text
psi(x) = [beta(x^2+1) + 2(alpha+beta)x] / (1-x)^2.
```

The kernel functional equation for the generating function of `ij` gives the
boundary condition for this map automatically. Its derivative vanishes only
at `-1`, outside the kernel domain, so the source Riemann map is a positive
scalar multiple of `psi`. Substitution in the source formula for `H_1` then
gives the result coefficient by coefficient.

## Scope

This is a theorem for an infinite two-parameter family (one essential
parameter after ignoring holding), but it does not settle Conjecture 1 for
asymmetric small-step laws or for walks with larger negative jumps. The
uniqueness of the positive killed harmonic function is the standard
quarter-plane result already invoked immediately before the source
conjecture; finite support meets its moment hypotheses.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `verification.md`: adversarial proof and scope audit.
- `source_paper.pdf`: original arXiv source.
- `figures/conjecture_1_crop.png`: source Conjecture 1.

## Novelty check

A bounded check was performed on 2026-08-27. The run indexes and close
web/arXiv searches were checked for arXiv:2012.08947 together with
`reflection symmetric small step`, `quarter plane`, `h(i,j)=ij`, `positive
harmonic function`, and `conformal map`. The source's separate simple-walk and
king-walk examples were found, but no statement of the family theorem above.
The check was not exhaustive, so novelty remains provisional.

## Human review recommendation

Send to an expert in random walks in cones or kernel boundary-value methods.
Review should focus on the one-sheeted conformal-map identification in Lemma 1
of the packet. All remaining steps are direct finite algebra or an explicitly
identified standard uniqueness input.

