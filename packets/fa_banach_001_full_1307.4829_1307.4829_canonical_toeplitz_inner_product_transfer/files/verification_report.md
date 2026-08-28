# Verification report

## Mathematical checks

1. **Exact target:** Section 5, page 31 of arXiv:1307.4829 asks for canonical-inner-product analogues of Theorems A-C and specifically suggests a direct operator-theoretic transfer.
2. **Norm-change operator:** radiality makes the change-of-inner-product operator diagonal on homogeneous polynomials with strictly positive coefficients. Its difference from identity splits into an exterior modified Toeplitz operator with a vanishing scalar symbol, a compactly supported analytic form, and (for positive alpha) finite Taylor blocks.
3. **Invertibility:** identity plus compact is Fredholm of index zero; coefficientwise positivity gives injectivity.
4. **General symbol transfer:** outside a fixed ball, the multiplier `q(z)=(|z|/(1+|z|))^alpha` exactly converts the modified high-degree weight to the canonical weight. It is bounded above and below there and converges to one.
5. **Boundedness necessity:** normalized exponential functions recover a uniform lower bound by `mu(B(a,r))` without using canonical-kernel estimates.
6. **Compact and Schatten errors:** fixed-ball forms are approximated by Taylor truncations with factorial tails; Taylor blocks involving the low projection are finite rank.
7. **Berezin lower bound:** the canonical kernel is obtained by applying the inverse norm-change operator to the modified kernel. Compactness of the difference and weak convergence of normalized modified kernels preserve the source near-diagonal lower estimate at infinity.
8. **Smooth exterior-identical weight:** for `phi_c(z)=|z|^2/2+(alpha/2)log(1+|z|)`, the two radial complex-Hessian eigenvalues are `1/2+alpha/(4r(1+r))` and `1/2+alpha/(8r(1+r)^2)`. They are uniformly positive outside a sufficiently large ball. Extending `g(s)=sF'(s)` inward with positive bounded derivative gives a `C^2` radial weight equal to `phi_c` outside that ball and with Hessian uniformly comparable to the Euclidean form.
9. **Exact canonical off-diagonal estimate:** the smoothed generalized-Fock kernel has exponential off-diagonal decay by Isralowitz-Virtanen-Wolf, arXiv:1402.2567, Lemmas 2.1-2.2. The exact and smoothed inner products differ by `A=I+T_h` with compactly supported bounded real `h`; `K^c_z=A^{-1}L_z`. The correction `(A^{-1}-I)L_z` decays exponentially in `z` by support localization and in `w` by self-adjoint kernel symmetry, hence exponentially in `|z-w|`.
10. **Quasi-Banach closure:** the exact normalized canonical kernel bound implies `tilde_mu_c(z) <= C sum_j mu(B(a_j,r)) exp(-epsilon|z-a_j|)`. For `0<t<1`, subadditivity and integration give the `L^t` bound by the lattice `ell_t` quasi-norm.

## Scope audit

- Boundedness and compactness are claimed for `1 <= p < infinity`.
- Schatten membership is claimed only on the Hilbert space `F^2_alpha`.
- The canonical Berezin `L^t` equivalence is claimed for the full range `0 < t < infinity`.

## Literature search bounds

Searched the local registry, solutions, attempts, and proof-gap indexes by arXiv id, exact title, and the terms canonical/natural inner product, Fock-Sobolev, Toeplitz, reproducing kernel, compactness, and Schatten. Bounded external searches used the exact open-problem phrases and source title. Results inspected included the 2023 paper *On Toeplitz operators between different Fock-Sobolev-type spaces*, which retains the modified kernel. No exact canonical transfer was located as of 2026-08-27.

## Supporting-source check

- The official arXiv PDF for arXiv:1402.2567 is included as `supporting_paper_1402.2567.pdf`.
- Its generalized-Fock hypotheses are `phi in C^2` and `c omega_0 < dd^c phi < C omega_0` uniformly.
- Lemmas 2.1-2.2 give the exponential off-diagonal kernel bound and the near-diagonal/diagonal bounds used in the packet.

## Artifact QA

- The upgraded seven-page packet compiled to PDF with no LaTeX warnings, undefined references, overfull boxes, or underfull boxes.
- All seven final pages were rendered at 144 dpi and visually inspected. No clipping, overlaps, broken glyphs, or unreadable elements were found.
- The final source crop was separately inspected at original resolution and contains the complete Section 5 question.
