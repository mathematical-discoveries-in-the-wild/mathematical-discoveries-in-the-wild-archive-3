# Fourier-algebra restriction to isotropy is always surjective

Status: `candidate_full_solution_likely_valid_needs_human_review`

## Source problem

Joseph DeGaetani and Mahya Ghandehari, *On the restriction maps of the
Fourier and Fourier-Stieltjes algebras over locally compact groupoids*,
arXiv:2411.14624. Remark 3.10, on printed page 13, asks whether Theorem 3.7
holds in full generality: for an arbitrary locally compact Hausdorff groupoid
with a Haar system, is

```text
R_u : A(G) -> A(G_u^u)
```

surjective?

## Result

Yes. For every locally compact Hausdorff groupoid `G` with a left Haar system
and every unit `u`, the restriction map above is a contractive surjective
algebra homomorphism. No etaleness, second countability, sigma-compactness,
Condition (*), unimodularity, or right-invariance assumption is needed.

## Proof mechanism

Put `H=G_u^u`, `X=G^u`, and let `sigma` be the representation of `H` on
`L2(X,lambda^u)` obtained by restricting the groupoid regular representation.
The source proof already gives

```text
R_u(A(G)) = A_sigma(H) subset A(H)
```

without using etaleness. The missing reverse inclusion is obtained without
orbit disintegration. The left action of `H` on `X` is free and proper. For
each `f in C_c(X)`, the averaging operator

```text
(W_f xi)(x) = integral_H xi(h) f(h^{-1}x) dh
```

is a bounded intertwiner from the left regular representation of `H` to
`sigma`. Properness gives the Schur bound. Continuity, full support of the
Haar-system measure, and compactly supported extension from one closed orbit
show that the family `{W_f}` has zero common kernel. Therefore the ranges of
the adjoints `{W_f^*}` span the regular Hilbert space densely. Coefficients
whose vectors lie in these ranges are explicit finite sums of coefficients of
`sigma`; approximation in coefficient norm gives `A(H) subset A_sigma(H)`.
This proves equality and surjectivity without an abstract central-support step.

## Files

- `solution_packet.pdf`: theorem, full proof, audit, and novelty check.
- `main.tex`: packet source.
- `source_paper.pdf`: local copy of arXiv:2411.14624.
- `figures/open_problem_crop.png`: Remark 3.10 from printed page 13.
- `verification.md`: focused verifier report.

## Human review recommendation

Reviewers should check the compact-support orbital-average bound and the
closed-orbit extension step. They should also compare the source's Claim 1 in
the proof of Theorem 3.7 with the reduction stated here; its displayed proof
uses only the general continuous-section extension theorem, not etaleness.
