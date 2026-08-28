# A weakness spike obstructs the nonmonotone rate formula

**Status:** candidate scoped counterexample, likely valid, pending expert review.

**Source:** A. S. Spivak and V. N. Temlyakov, *On weak greedy algorithms*,
arXiv:2604.26064, Theorem 1.1 and the monotonicity discussion on printed
pages 3-4.

## Result

The nonincreasing hypothesis in source Theorem 1.1 cannot simply be deleted.
Even allowing a universal multiplicative constant, the displayed mixed-norm
rate fails for arbitrary weakness sequences.

The counterexample uses the source paper's quoted Livshitz-Temlyakov lower
construction for constant weakness `epsilon`. Polynomially slow residuals
force the maximal dictionary correlation to be negligible along a
subsequence. At one such index, insert a weakness spike from `epsilon` to
`1/2`. The spike changes the residual negligibly, but the literal source
formula changes its mixed-norm exponent to `alpha=1/5` and predicts decay of
order `N^(-1/10)`. Choosing `b epsilon < 1/10` contradicts that prediction by
an unbounded factor.

## Scope

This is a complete negative answer only to the literal extension of the
source rate formula. It does not rule out a different order-sensitive bound
for arbitrary weakness sequences and does not settle the paper's broad
convergence-classification problems.

## Packet contents

- `solution_packet.pdf` / `main.tex`: statement, two lemmas, proof, and scope.
- `source_paper.pdf`: locally compiled source arXiv manuscript.
- `figures/theorem_1_1_crop.png`: source theorem.
- `figures/monotonicity_question_crop.png`: source question.
- `verification_report.md`: adversarial verification checklist.

## Bounded novelty search

The run solution index, ledger, attempts, and active/archive claims were
searched for arXiv:2604.26064, nonmonotone weakness sequences, WGA rate
bounds, and weakness spikes. Exact arXiv web searches on 2026-08-27 for the
source id, the source's monotonicity sentence, and the obstruction keywords
found no follow-up or matching result. This supports only bounded novelty;
priority remains subject to specialist review.

Ledger: `runs/fa_banach_001/ledger/results/2604.26064_nonmonotone_weakness_spike_rate_obstruction.json`.
