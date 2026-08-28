# Verification notes

## Counterexample checks

1. With \(v=\mathbf1_{B(0,1)}\),
   \(W=\operatorname{diag}(1-v,v)\) satisfies \(W^2=W\) and
   \(\operatorname{rank}W=1\) almost everywhere.
2. Its ordered eigenvalues are the constant functions \(0\) and \(1\).
   Consequently all Schatten norms equal one, and
   \(\operatorname{tr}(W^k)=1\) for every integer \(k\ge1\).
3. The two radial formulas for
   \[
   h(r)=\frac{\sinh r}{r\cosh1}\quad(r\le1),\qquad
   h(r)=1-\frac{1-\tanh1}{r}\quad(r\ge1)
   \]
   agree in value and first derivative at \(r=1\). Hence
   \((-\Delta+\mathbf1_B)h=0\) distributionally without a surface delta.
4. For \(U_R=(0,\eta_Rh)\), the second channel gives
   \(\|WU_R\|_2=\|\mathbf1_Bh\|_2>0\), independent of \(R\).
5. The cutoff residual is \(O(R^{-2})\) on an annulus of volume \(O(R^3)\),
   hence \(\|(-\Delta I+W)U_R\|_2=O(R^{-1/2})\).
6. Each cutoff belongs to \(H^2(\mathbb R^3;\mathbb C^2)=D(-\Delta I+W)\)
   because \(W\) is bounded and the value/derivative matching removes the
   only possible interface singularity.

## Positive theorem checks

1. Vector Kato domination gives
   \[
   |(H+\varepsilon)^{-1}F|
   \le(-\Delta+\lambda_{\min}+\varepsilon)^{-1}|F|.
   \]
2. Bailey's scalar theorem controls
   \(\lambda_{\min}(-\Delta+\lambda_{\min}+\varepsilon)^{-1}\) on \(L^2\).
3. Eigenvalue comparability converts this into a uniform bound for
   \(W(H+\varepsilon)^{-1}\), without entrywise sign assumptions.
4. Applying the bound to \(F=(H+\varepsilon)u\), then sending
   \(\varepsilon\downarrow0\), proves the matrix maximal estimate.

## Numerical sanity check

Run:

    conda run --no-capture-output -n sandbox python code/verify_cutoff_counterexample.py

The expected output records exact projection spectra at \(v=0,1\), matching
errors at machine precision, fixed potential norm \(1.4650804067\), and
\(\sqrt R\) times the residual stabilizing near \(23.206\).

The computation is a sanity check only; the packet proof is analytic.

## Literature boundary

- Bailey, arXiv:1812.10196, Section 5.3 asks for a matrix
  reverse-Hölder-type sufficient condition.
- Davey--Isralowitz, arXiv:2207.05790, Definition 2.1 introduces a
  directional matrix class \(\mathcal B_q\). The example here is not in that
  class because the coordinate quadratic forms are
  \(\mathbf1_B\) and \(\mathbf1_{\mathbb R^3\setminus B}\), neither scalar
  reverse Hölder.
- Addona--Leone--Lorenzi--Rhandi, arXiv:2401.00479, impose comparable
  eigenvalues, reverse-Hölder control of the smallest eigenvalue, and
  nonpositive off-diagonal entries for their broader \(L^p\) theorem.
- Exact and close searches through 2026-08-27 found no displayed
  constant-spectrum projection counterexample.

Verdict: likely valid full counterexample to pointwise-spectral criteria;
the broader geometry-sensitive source problem remains open.
