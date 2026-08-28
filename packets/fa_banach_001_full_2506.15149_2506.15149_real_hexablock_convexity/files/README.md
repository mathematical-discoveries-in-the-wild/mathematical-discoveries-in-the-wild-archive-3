# Convexity of the real hexablock

Status: `full_solution_likely_valid`

Source: Indranil Biswas, Sourav Pal, and Nitin Tomar, *The Hexablock: a
domain associated with the mu-synthesis in M_2(C)*, arXiv:2506.15149v2
(2026), PDF page 38.

## Full resolution

The source conjectures that `H intersect R^4` is convex and proves in
Proposition 6.3 that this is equivalent to concavity of an explicit height
function `K` on the real tetrablock tetrahedron.  The packet proves the exact
closed form

```text
K(x1,x2,p) = 1/2 * [
    sqrt((1+p)^2 - (x1+x2)^2)
  + sqrt((1-p)^2 - (x1-x2)^2)
].
```

If

```text
L1 = 1-x1+x2-p,  L2 = 1-x1-x2+p,
L3 = 1+x1+x2+p,  L4 = 1+x1-x2-p,
```

then the real tetrablock is exactly `L1,L2,L3,L4 > 0` and

```text
K = 1/2 * (sqrt(L2*L3) + sqrt(L1*L4)).
```

The geometric mean is concave on the positive quadrant.  Thus `K` is
concave, and source Proposition 6.3 gives convexity of `H intersect R^4`.

## Key mechanism

Writing `u=beta1+beta2`, `v=beta1-beta2`, `U=artanh(u)`, and
`V=artanh(v)` turns the source maximizers into

```text
z1 = tanh((U+V)/2),  z2 = tanh((U-V)/2).
```

Substitution into the source height cancels the hyperbolic terms and yields
the closed form above.  This avoids the complicated three-variable Hessian
calculation proposed in the paper.

## Review files

- `solution_packet.pdf`: theorem, proof, verification, and novelty audit.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source PDF page 38 showing the conjecture
  and Proposition 6.3.
- `verification.md`: adversarial step check.
- `code/verify_closed_form.py`: independent numerical identity and Jensen
  checks.

## Scope and novelty check

The result settles the exact conjecture for the open real hexablock.  It does
not assert convexity of the full complex hexablock or resolve the source's
other problems.  On 26 August 2026 we searched all four run indexes, the local
parsed arXiv corpus, and bounded arXiv/web results using the source id/title,
`real hexablock`, `intersection of the hexablock`, and the radical/geometric
mean formula.  The later hexablock papers arXiv:2507.14589,
arXiv:2507.16176, and arXiv:2608.00819 do not advertise this result in their
abstracts, and no prior proof or closed form was found.  This supports, but
does not establish, novelty.

Human review recommendation: **send to human**, focusing first on the
half-angle substitution and facet-coordinate factorization.
