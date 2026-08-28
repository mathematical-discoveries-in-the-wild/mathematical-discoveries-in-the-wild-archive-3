# Noninjectivity of the natural hyperseries map

Status: **candidate full negative answer (likely valid; human review requested)**

Source: Diksha Tiwari and Paolo Giordano, *Hyperseries in the
non-Archimedean ring of Colombeau generalized numbers*, arXiv:2006.16141,
source PDF page 7, after Lemma 7(iii).

## Result

For every gauge pair satisfying the source hypothesis
`sigma >= rho^*`, the natural linear map

`lambda: rho-R_u -> rho_sigma-R_s`

is not injective. Set

`K_epsilon = ceil(exp(1/sigma_epsilon))`

and let `a_(n,epsilon)` be 1 at `n = K_epsilon` and 0 elsewhere. This
array is uniformly moderate but not uniformly negligible, so it is nonzero
in the domain. Every sigma-moderate hypernatural endpoint is eventually
smaller than `K_epsilon`; consequently every tested interval sum is
eventually exactly zero, and the image class vanishes.

The same construction gives infinitely many nonzero pairwise orthogonal
idempotents in the kernel.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source PDF.
- `figures/open_problem_crop.png`: source PDF page 7 crop.
- `verification.md`: proof audit and novelty-search bounds.
- `novelty_search.md`: bounded search log.

Human review should focus on the quantifier order in uniform negligibility
and the definition of sigma-moderate hypernaturals. Both are explicit in the
source, and they are exactly what the counterexample exploits.
