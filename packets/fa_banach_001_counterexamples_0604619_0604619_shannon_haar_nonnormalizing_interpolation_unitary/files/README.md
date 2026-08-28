# Shannon-Haar counterexample to interpolation-unitary normalization

Status: `candidate_counterexample_likely_valid`

Source: David R. Larson, *Unitary systems and wavelet sets*,
arXiv:math/0604619. The target is Problem 4 on source PDF page 28.

## Claimed result

Let \(\psi_S\) be the Shannon dyadic orthonormal wavelet. For every dyadic
orthonormal wavelet \(\eta\) whose Fourier transform is nonzero almost
everywhere, the interpolation unitary \(V_{\psi_S}^{\eta}\) does **not**
normalize the commutant \(\{D,T\}'\). The Haar wavelet is an explicit such
\(\eta\). Thus Problem 4 has a negative answer.

The obstruction is the positive-frequency projection. In the Fourier domain it
belongs to the commutant because its symbol is invariant under dyadic dilation.
On the Shannon wavelet, however, it is the same as a nonconstant periodic
translate-coefficient mask \(p\). Interpolation transports that translate series
unchanged to the target wavelet. If the conjugated projection were still in the
commutant, it would have a dyadic-dilation-invariant multiplier symbol \(h\).
Since the Fourier transform of the target wavelet is nonzero almost everywhere,
the transported-vector identity forces \(h=p\) almost everywhere, contradicting
the failure of \(p(s)=p(2s)\).

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `verification.md`: adversarial step check.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: source PDF page 28 crop containing Problem 4.

## Novelty check

A bounded search was performed on 2026-08-27. The run's four lightweight
indexes had no hit for arXiv:0604619 or the normalization question. Exact and
close arXiv/web searches for `interpolation unitary`, `normalize commutant`,
`Shannon Haar`, and Larson's Problem 4 found the source paper and the related
2006 exposition arXiv:math/0604615, but no later explicit solution or
counterexample. This is not an exhaustive citation-database search, so novelty
remains provisional pending expert review.

## Human review recommendation

Send to a wavelet/operator-algebra expert. The key check is the periodic-mask
transport identity in the proof; all other steps are direct consequences of the
source paper's commutant characterization. The elementary Haar Fourier formula
verifies that the explicit witness satisfies the nonvanishing hypothesis.
