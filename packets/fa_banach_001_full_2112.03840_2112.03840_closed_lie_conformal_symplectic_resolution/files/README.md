# Closed-Lie resolution of the higher-dimensional homogeneous-kernel problem

Status: `candidate_full_solution_likely_valid`

This packet gives a complete answer to the open problem in arXiv:2112.03840, reiterated in arXiv:2504.04127, in the natural category of closed transitive linear Lie subgroups of `GL^+(d,R)`.

In every even dimension `d=2m`, the positive conformal-symplectic group `CSp^+(2m,R)` has exactly two generic diagonal orbits on pairs. Its strongly homogeneous measurable kernels therefore form a two-dimensional space, with one-dimensional symmetric and antisymmetric classes. The canonical parity-matched kernel is

\[
K_m(x,y)=\omega(x,y)^{-m}.
\]

The packet constructs its homogeneous finite-part distribution and proves a Radon/Hilbert-derivative formula, conformal-symplectic covariance, output homogeneity, the resulting global `L^p` obstruction, formal adjoint parity, and exact cancellation conditions for ordinary symmetric principal values.

In every odd dimension `d>=3`, Kramer's classification of closed connected linear groups transitive on the punctured space reduces the possibilities to similarity groups, `SL(d,R)` and its scalar extensions, and `G_2 R_{>0}` in dimension seven. Direct orbit calculations then exhaust the kernel alternatives:

- similarity and exceptional-similarity groups have infinite-dimensional Case-A kernel spaces;
- `SL(d,R)` has only the constant Case-A kernel;
- every proper scalar extension of `SL(d,R)`, including `GL^+(d,R)`, has only the zero kernel and is Case B.

Thus no odd-dimensional closed transitive group produces a nonzero essentially unique Case-B kernel. The even construction and odd obstruction together resolve the source problem in the closed linear Lie category. Nonclosed pathological subgroups remain outside the stated result.

The bounded novelty search found related work on powers of the standard symplectic form and homogeneous-distribution operators (arXiv:0906.2874). The packet does not claim novelty for those ingredients or for Kramer's group classification; its candidate contribution is their exact synthesis in the source framework.

## Files

- `solution_packet.pdf`: theorem, full proof, operator properties, verification, and scope boundary.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2112.03840v1.
- `supporting_paper_kramer_2003.pdf`: decisive classification source.
- `figures/open_problem_crop.png`: page 31 source-problem evidence crop.
- `verification.md`: adversarial proof audit and bounded novelty-search record.
- `code/check_csp_kernel.py`: finite-dimensional covariance and parity sanity checks.
