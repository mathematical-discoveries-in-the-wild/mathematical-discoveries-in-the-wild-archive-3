# Candidate full solution: additive regularity of vector-valued convolution

Status: `candidate_full_solution_likely_valid`

Source: Karsten Kruse, *The approximation property for weighted spaces of differentiable functions*, arXiv:1806.02926, Banach Center Publications 119 (2019), 233-258, DOI 10.4064/bc119-14.

## Result

The open problem after Lemma 4.5 on page 16 asks whether, for a quasi-complete locally convex Hausdorff space `E`, functions `f in C^k(R^d,E)` and `g in C^n(R^d)` with at least one compactly supported satisfy

`f*g in C^max(k,n)` and `D^alpha(f*g)=(D^alpha f)*g` for every `|alpha|<=k`.

The packet proves the stronger theorem

`D^(alpha+beta)(f*g)=(D^alpha f)*(D^beta g)`

for `|alpha|<=k` and `|beta|<=n`. Hence `f*g in C^(k+n)` for finite `k,n`, and it is smooth if either index is infinite.

## Mechanism

Use the commuted representation `f*g=g*f`. Locally in `x`, compact support confines the integral to one fixed compact set even when only the vector-valued factor is compactly supported. Compact Pettis integration is continuous for uniform convergence in every continuous seminorm, so all available derivatives may be passed through the integral on either factor. Splitting derivatives between the two factors gives additive regularity.

## Packet contents

- `solution_packet.pdf`: reviewer-facing proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: local copy of arXiv:1806.02926.
- `figures/open_problem_crop.png`: rendered source-page crop showing the exact question.
- `tmp/`: build and rendering intermediates.

## Novelty and review

A bounded search on 2026-08-27 covered the exact printed sentence, arXiv id/title/author queries, related convolution terms, the published paper, ten OpenAlex-indexed citing works, and selected later work by Kruse including the 2023 habilitation. No explicit later resolution was found. The argument is elementary enough that an implicit folklore result remains possible; this is not a priority claim.

Recommended review focus: compact-range Pettis integration under quasi-completeness, the local support set `closure(U)-supp(f)`, and the mixed-derivative step yielding `C^(k+n)`.
