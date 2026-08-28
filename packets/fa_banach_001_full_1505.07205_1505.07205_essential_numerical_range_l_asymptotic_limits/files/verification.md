# Verification report

Candidate: complete separable characterization of the `L`-asymptotic limits of operators similar to unitaries, answering the open problem after Theorem 4.2 of arXiv:1505.07205.

## Claim checked

On a separable infinite-dimensional complex Hilbert space, for every fixed Banach limit `L`, the operators of the form `A_{T,L}` with `T` similar to a unitary are exactly the positive invertible operators `A` satisfying `1 in W_e(A)`. Moreover, for every such `A`, one can choose a single `T` for which the equality holds for every Banach limit.

## Verdict

`likely valid` as a candidate full result within the stated separable scope. The necessity and sufficiency arguments are self-contained apart from the standard self-adjoint Weyl--von Neumann theorem. Publication-level novelty is not established.

## Adversarial step audit

| Step | Status | Notes |
| --- | --- | --- |
| Formula for `A_{SUS^{-1},L}` | valid | Direct expansion gives `S^{-*} Phi^U_L(S^*S) S^{-1}`. |
| Invertibility of the orbit mean `C` | valid | The positive unital map preserves the uniform lower and upper bounds of `S^*S`. |
| Commuting normalization | valid | Shift invariance makes `C` commute with `U`; `R=SC^{-1/2}` represents the same `T` and satisfies `Phi(R^*R)=I`. |
| Identification of `A^{-1}` | valid | `A=(RR^*)^{-1}`, while `R^*R` is unitarily equivalent to `RR^*` by polar decomposition. |
| Essential-spectrum one-sided correction | valid | If the essential spectrum lies above or below 1, the appropriate positive part is finite rank and yields a finite-rank orbit mean bounded below. |
| Finite-rank trace contradiction | valid | On any `N` orthonormal vectors the orbit-mean mass is at most `Tr(F)`; a lower bound `delta I` would grow as `N delta`. |
| `W_e(A)` versus `W_e(A^{-1})` | valid | For positive invertible self-adjoint `A`, both conditions say that the essential spectral interval crosses 1. |
| Weyl--von Neumann input | standard external theorem | In the separable self-adjoint case, `B=D+K` with `D` diagonal self-adjoint, `K` compact self-adjoint, and identical essential spectra. |
| Diagonal rearrangement, endpoint case | valid | An infinite diagonal subsequence converging to 1 gives uniform moving averages after a fixed-head estimate; an infinite complement can be reserved for negative indices. |
| Diagonal rearrangement, interior case | valid | A mechanical balanced word mixes subsequences approaching points on opposite sides of 1 with uniformly bounded interval discrepancy. Perturbation errors form a null sequence. |
| Passage from moving averages to every Banach limit | valid | Uniform moving-average convergence is almost convergence; each fixed translated diagonal tail has Banach limit 1. |
| Compact orbit contribution | valid | The bilateral shift tends weakly to zero; compactness turns this into norm convergence after applying `K`, so every matrix coefficient tends to zero ordinarily. |
| Final construction | valid | With `B=A^{-1}`, `R=B^{1/2}`, and `T=RUR^{-1}`, the normalized orbit mean gives `A_{T,L}=B^{-1}=A` for every `L`. |

## Counterexample and edge-case checks

- Scalar test: `A=cI` satisfies the condition only for `c=1`, agreeing with direct similarity normalization.
- Compact perturbation test: `A=I+K>0` always satisfies the essential condition; the construction correctly absorbs `K` because compact shift conjugates vanish.
- One-sided essential spectrum: if `sigma_e(A)` is contained strictly in `(1,infinity)` or `(0,1)`, the theorem rules it out. The finite-rank trace lemma identifies the obstruction.
- Endpoint case: `1` may be an essential spectral endpoint rather than an isolated eigenvalue. The convergent-subsequence branch of the diagonal lemma covers it.
- Banach-limit dependence: necessity uses an arbitrary fixed `L`; sufficiency creates almost-convergent diagonals, so no choice of Banach limit is hidden.
- Finite dimension: excluded. The trace contradiction needs arbitrarily long orthonormal lists, and the source already has a distinct finite-dimensional theorem.
- Nonseparable dimension: excluded from sufficiency. The necessity proof survives, but the diagonal construction is countable.

## Literature boundary

- The exact open problem appears after Theorem 4.2 on PDF page 39 of arXiv:1505.07205.
- arXiv:1407.0525 treats ordinary strong asymptotic limits for contractions and explicitly leaves the unitary-similar Banach-limit description open.
- arXiv:1407.1275 concerns the finite-dimensional matrix problem.
- arXiv:2010.14740 discusses Banach/Cesaro asymptotic limits and similarity but does not state the essential-numerical-range classification found here.
- Exact-phrase and keyword searches across the run indexes, arXiv, and the web found no prior theorem matching the result. This was a bounded search, not a definitive priority determination.

## Confidence and recommendation

Mathematical-validity confidence: 93/100 within the separable scope.

Human-review recommendation: retain as a candidate full separable solution. Before publication, independently check the diagonal rearrangement lemma and perform a broader literature search around invariant means of inner automorphisms, essential numerical range, and unitary orbit averages.

## Artifact verification

- `solution_packet.pdf`: six pages; all six final rendered pages were visually inspected. No clipping, overlap, missing glyphs, or unreadable evidence text was found.
- Extracted-text smoke check: 10,126 characters; the main theorem, both proof lemmas, source question, and literature references are present.
- LaTeX build: `latexmk` completed with resolved references and no warnings, overfull boxes, or underfull boxes.
- Numerical command: `conda run --no-capture-output -n sandbox python code/check_shift_average.py`.
- Numerical result: balanced-word interval discrepancy stayed below 1; maximum moving-average error decreased from `0.10247869` at width 10 to `0.00010159` at width 10,000.
- SHA-256 `source_paper.pdf`: `f77c35c73e67bbd5c1e7b0925d4018da152787ecd8f1cf7da79093a05d004bf5`.
- SHA-256 `solution_packet.pdf`: `7758da6599bdab4aa490865b8c4f7c9f9e77fe91ae61b78e0d379756e774bc5c`.
- SHA-256 `figures/open_problem_crop.png`: `3f7b9f14cedc82d9d84905a9a44e67f293b52d00c28751a05673c752a4396e43`.
