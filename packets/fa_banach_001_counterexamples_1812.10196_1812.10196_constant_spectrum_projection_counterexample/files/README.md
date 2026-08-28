# Constant-spectrum matrix counterexample

Status: **candidate full counterexample, likely valid**, to pointwise-spectral
reverse-Hölder criteria for matrix maximal regularity.

Source: Julian Bailey, *The Kato Square Root Problem for Divergence Form
Operators with Potential*, arXiv:1812.10196, Section 5.3, printed page 42.

## Full negative result

In \(\mathbb R^3\), let \(v=\mathbf 1_{B(0,1)}\) and

\[
W(x)=\operatorname{diag}(1-v(x),v(x)).
\]

Then \(W(x)\) is a rank-one orthogonal projection almost everywhere:

\[
W^2=W,\qquad \operatorname{rank}W=1,\qquad
\operatorname{spec}W=\{0,1\}.
\]

Thus both ordered eigenvalues, every Schatten norm, the trace, and every
spectral moment are constant. Nevertheless \(W\notin\mathcal W_2\). The
second channel is the scalar operator \(-\Delta+\mathbf1_B\), which has an
explicit bounded zero-energy solution. Its cutoffs have a fixed nonzero
potential term while the operator residual decays as \(R^{-1/2}\).

Consequently, no condition that sees only the pointwise eigenvalue list and
is satisfied by the constant spectrum \(\{0,1\}\) can imply the matrix
\(\mathcal W_2\) estimate. This includes applying a scalar reverse-Hölder
condition to the operator norm, any Schatten norm, or the trace.

## Positive repair and remaining frontier

The packet also proves that \(W\in\mathcal W_2\) if

\[
\lambda_{\min}(W)\in RH_q,\quad q\ge2,\qquad
\lambda_{\max}(W)\le\kappa\lambda_{\min}(W).
\]

This \(L^2\) theorem needs no off-diagonal sign condition and allows complex
Hermitian potentials.

Davey--Isralowitz, arXiv:2207.05790, define a genuinely matrix-valued
reverse-Hölder class by requiring all fixed-direction quadratic forms
\(\langle W(\cdot)e,e\rangle\) to satisfy scalar reverse-Hölder estimates
uniformly. The projection example is excluded from that class. Whether their
directional matrix \(\mathcal B_2\) condition alone implies
\(\mathcal W_2\) remains a geometry-sensitive frontier.

## Verification and novelty

The analytic proof is in solution_packet.pdf.
code/verify_cutoff_counterexample.py checks the projection identities,
interface matching, and \(R^{-1/2}\) residual decay.

A bounded search through 2026-08-27 covered the run indexes, exact source
question, projection-valued and constant-spectrum matrix potentials, matrix
reverse-Hölder classes, and source-level inspection of arXiv:2207.05790 and
arXiv:2401.00479. No equivalent counterexample was found. Novelty confidence
is moderate because the construction is elementary.

The counterexample is a full negative result for pointwise-spectral criteria,
not a full characterization of all geometry-sensitive matrix conditions.

## Files

- solution_packet.pdf: proof and literature-boundary packet.
- source_paper.pdf: arXiv:1812.10196.
- supporting_paper_2207.05790.pdf: directional matrix reverse-Hölder class.
- supporting_paper_2401.00479.pdf: closest later maximal-regularity theorem.
- figures/open_problem_crop.png: source question.
- code/verify_cutoff_counterexample.py: reusable numerical sanity check.
- verification.md: reviewer checklist and recorded output.
