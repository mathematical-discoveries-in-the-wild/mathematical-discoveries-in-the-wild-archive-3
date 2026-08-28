# Verification report

Candidate: full closed-Lie resolution of the higher-dimensional homogeneous-kernel problem in arXiv:2112.03840, reiterated in arXiv:2504.04127.

## Claim checked

For every even `d=2m`, `G=CSp^+(2m,R)` gives a nonzero two-dimensional generic homogeneous-kernel space with one-dimensional swap-parity classes, and `omega(x,y)^(-m)` has the stated homogeneous finite-part realization. For every odd `d>=3`, no closed transitive subgroup of `GL^+(d,R)` gives a nonzero essentially unique Case-B kernel; the only essentially unique odd-dimensional kernel is the constant Case-A kernel for `SL(d,R)`.

## Verdict

`likely valid` as a candidate full result within the explicitly stated closed linear Lie-group category. The even-dimensional proof is constructive. The odd-dimensional proof depends decisively on Kramer's published classification and normalizer theorem, followed by short exhaustive orbit calculations. Publication-level novelty remains unestablished.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| `det(g)=c(g)^m` for `CSp^+` | valid | Divide by `sqrt(c(g))`; the quotient is symplectic and has determinant one. |
| `CSp^+` transitivity on nonzero vectors | valid | Extend a normalized symplectic pair to a symplectic basis. |
| Two generic `CSp^+` pair-orbits | valid | Same-sign pairs admit a conformal extension from their symplectic two-planes; sign is invariant because the multiplier is positive. |
| Even-dimensional kernel classification | valid | The relative character is `det(g)^(-1)=c(g)^(-m)` and the singular locus `omega=0` is null. |
| One-dimensional parity classes | valid | Swapping variables exchanges the positive and negative generic orbits. |
| Finite-part definition and covariance | valid | `Pf(t^-m)=(-1)^(m-1)/(m-1)! D^(m-1) pv(1/t)` is exactly homogeneous; `c^-m` cancels `det(g)=c^m`. |
| Radon/Hilbert formula | valid | Coarea reduces the pullback distribution to the one-dimensional Radon profile. |
| Output homogeneity and global `L^p` obstruction | valid | The radial integral is `integral r^(2m-1-mp) dr`; a nonzero homogeneous output cannot lie in a global finite `L^p`. |
| Formal adjoint parity and ordinary-PV criterion | valid | Both follow from the one-dimensional finite-part parity and Taylor expansion of the Radon profile. |
| Scalar-extension residue obstruction | valid | The degree `-m` residue is proportional to `(A+(-1)^(m-1)B) delta^(m-1)` and cannot be removed through the Euler equation. The claim is limited to scalar pullback regularizations. |
| `G^0` transitive when `G` is closed and transitive | valid | `Lie(G^0)=Lie(G)` makes every `G^0` orbit open; connectedness of the punctured space leaves one orbit. |
| Kramer's odd-dimensional list | externally verified | Theorems 6.14 and 6.17 in the included 2003 paper reduce odd-dimensional connected possibilities to similarities, `SL/GL^+`, and `G_2` similarities in dimension seven, with the needed normalizer information. |
| Reduction of disconnected odd groups | valid | Similarity normalizers add nothing in `GL^+`; if `G^0=SL(d)`, every component contributes a positive scalar, giving precisely scalar extensions. |
| Similarity-group kernels | valid | Fixed Gram parameters give `|x|^-d F(|y|/|x|,<x,y>/(|x||y|))`, an infinite-dimensional Case-A family. The `G_2` group inherits this family. |
| `SL(d)` kernels | valid | For `d>=3`, `SL(d)` is transitive on independent pairs, a conull set, so kernels are constant. This is Case A. |
| Proper scalar extensions | valid | `SL(d)` first forces constancy; covariance under one nontrivial scalar then forces that constant to vanish. The scalar can be combined with an `SL(d)` element to produce a stabilizer with nonunit determinant, proving Case B. |
| Exhaustion of odd alternatives | valid conditional on Kramer | The three kernel alternatives cover every group on Kramer's list and every allowed disconnected extension. |

## Counterexample search and low-dimensional checks

- `d=2`: `CSp^+(2,R)=GL^+(2,R)`, recovering the source's orientation-split model.
- `d=3`: the odd list yields `SO(3)R_{>0}`, `SL(3,R)`, and scalar extensions; their kernel spaces are respectively infinite-dimensional, one-dimensional constant, and zero.
- `d=7`: the exceptional `G_2R_{>0}` possibility cannot be essentially unique because every ordinary similarity kernel remains invariant under its smaller group.
- Potential finite disconnected enlargements are handled by the normalizer statement and the scalar-decomposition argument.
- For even `m=1,2,3`, the included numerical script checks determinant, covariance, and parity for random elementary conformal-symplectic matrices. It is a sanity check, not proof.

## External dependencies and literature boundary

- The exact source problem appears on PDF page 31 of arXiv:2112.03840v1 and is reiterated in arXiv:2504.04127v1.
- Kramer's *Two-transitive Lie groups*, J. Reine Angew. Math. 563 (2003), Theorems 6.14 and 6.17, is the decisive external classification input; a copy is included in the packet.
- Bounded searches of all four run indexes and targeted arXiv/web combinations found no paper explicitly connecting the conformal-symplectic construction or Kramer's classification to this source problem.
- arXiv:0906.2874 is close prior art on powers of the standard symplectic form, meromorphic homogeneous distributions, and intertwining operators. No novelty claim is made for those ingredients or for Kramer's classification.

## Gaps and limitations

- The theorem is for closed transitive linear Lie subgroups. Pathological nonclosed subgroups, for which measurable invariance need not automatically pass to the closure, are not claimed.
- The related representation-theoretic novelty search is bounded, not exhaustive.
- The even-dimensional residue obstruction concerns scalar pullback regularizations `u(omega(x,y))`; it does not rule out every hyperplane-supported, non-scalar counterterm.
- No adapted Banach-space boundedness theorem is claimed.

## Confidence

Score: 91/100 for mathematical validity within the stated closed-Lie category; substantially lower for publication-level novelty.

Human-review recommendation: retain as a candidate full closed-Lie result. Before publication, independently check the extraction of the odd cases from Kramer's Theorems 6.14 and 6.17 and conduct a broader representation-theoretic novelty review.

## Artifact verification

- `solution_packet.pdf`: eight pages; all eight rendered pages were visually inspected with no clipping, overlap, missing glyphs, or unreadable evidence text.
- Extracted-text smoke check: 16,840 characters; the odd-dimensional theorem, source-problem section, and Kramer reference are all present.
- LaTeX build: two-pass `latexmk` completed without warnings, overfull boxes, or unresolved references.
- Numerical command: `conda run --no-capture-output -n sandbox python code/check_csp_kernel.py`.
- Numerical result: 200 determinant/covariance/parity trials passed for each of `m=1,2,3`.
- SHA-256 `source_paper.pdf`: `f84a59ee7e1f8b4ebb582a7b2bf9233d6206e7c81a59d1b0944e8b5cfe50cf21`.
- SHA-256 `supporting_paper_kramer_2003.pdf`: `c59195dbec56933b1c6d2021818b0acb16d79f1f9ff4e92c4f87e4491f3afc33`.
- SHA-256 `solution_packet.pdf`: `fc509be9e75ce3a47ea9f643efb42b12e319b4c82834433d2d49e2d9f54bcfd9`.
- SHA-256 `figures/open_problem_crop.png`: `cbc709ce4ac51f4a1edae4624ffef2f3c53bd70b2db706e34de1fb229953ff51`.
