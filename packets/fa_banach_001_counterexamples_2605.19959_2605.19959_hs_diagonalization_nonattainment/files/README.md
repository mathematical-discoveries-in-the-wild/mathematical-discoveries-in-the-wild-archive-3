# Nonattainment of the Hilbert--Schmidt basis-learning objective

Result type: `counterexample`

Status: candidate full counterexample to optimizer existence, likely valid
pending expert review.

Source:

- Hamidreza Kamkari, Mohammad Sina Nabizadeh, and Justin Solomon,
  “Learning Orthonormal Bases for Function Spaces,” arXiv:2605.19959v1
  (2026).
- Target: Definition 1 on PDF page 4 and Theorem 2/equation (7) on PDF
  page 5.
- Local source: `source_paper.pdf`.
- Source evidence: `figures/source_theorem2.png`.

## Claimed contribution

The maximum in the source's variational diagonalization problem need not
exist, even on `H=L2([0,1])` for the real Fourier basis and a positive
trace-class covariance operator with continuous kernel.

Pair the Fourier basis and let `R` rotate every pair by 90 degrees.  Give the
ordered basis `R phi_i` the simple eigenvalues `2^(-i)`, and use
`p(i)=2^(-i)`.  The spectral upper bound is `sum_i 4^(-i)=1/3`.  Equality
forces the full infinite quarter-turn (up to diagonal signs), whose
displacement from the identity is not Hilbert--Schmidt.  Hence it is not in
the source's admissible class.  The finite block rotations are admissible and
have exact values

```text
F(Q_m) = 1/3 - 1/(15*16^m),
```

so `1/3` is the supremum but is not attained.

The operator is a literal continuous-function covariance: with Rademacher
signs `eps_i`, the uniformly convergent random Fourier series
`X=sum_i 2^(-i/2) eps_i R phi_i` has covariance `A`.

## Scope caveat

This fully answers the implicit optimizer-existence question negatively.  It
does not refute the conditional ordering conclusion when a maximizer exists,
and it does not rule out using the full orthogonal group or adding a
Hilbert--Schmidt compatibility hypothesis on the target eigenbasis.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/source_theorem2.png`: source theorem crop.
- `code/check_counterexample.py`: exact arithmetic regression.
- `verification_report.md`: mathematical, build, and novelty checks.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

A bounded run-index, arXiv, exact-title, exact-theorem, and focused
Hilbert--Schmidt/nonattainment search on 27 August 2026 found no correction or
later response.  The source remains at v1.  Novelty confidence is moderate
pending specialist review.

## Human review focus

Check that the source intends `SO(HS)` literally as Definition 1.  Under both
the stationary definition and the later time-dependent Hilbert--Schmidt-flow
variant, every admissible `Q` satisfies `Q-I` Hilbert--Schmidt, which is the
only group property used by the obstruction.
