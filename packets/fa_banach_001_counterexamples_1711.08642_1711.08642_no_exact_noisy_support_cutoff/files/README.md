# Exact noisy support cutoff fails for oversmoothing ell1 regularization

Status: `candidate_counterexample_likely_valid`

## Source question

Daniel Gerth and Bernd Hofmann, *On ell1-regularization under continuity of
the forward operator in weaker topologies*, arXiv:1711.08642. In the final
discussion, printed pages 18-19, the authors identify as an open problem the
claim that the support of an oversmoothing ell1-regularized approximation is
not larger than the truncation index `n(delta)`.

The packet addresses the exact localization interpretation needed by the
truncation argument:

`supp(x_alpha^delta) subset {1,...,n(delta)}`.

## Result

That inclusion is false, even for the polynomial diagonal model used in the
announced follow-up paper. Take

- `A e_k = k^(-beta) e_k`, with `beta>0`;
- `x_k^dagger = k^(-eta)`, with `1/2 < eta <= 1`;
- the prototype-rate minimizer `n(delta)` and the follow-up parameter choice
  `alpha = c_alpha delta^2/(sqrt(n(delta)) phi(delta))`.

For every sufficiently small `delta`, add the admissible noise
`delta e_(n(delta)+1)`. Coordinatewise soft thresholding then gives a nonzero
coefficient at `n(delta)+1`. The key estimate is

`alpha/(delta sigma_(n+1)) <= c_alpha 2^beta/sqrt(n) -> 0`.

Thus exact noisy support localization cannot close the source proof route.
This does not disprove convergence rates or quantitative tail estimates.

## Files

- `solution_packet.pdf`: complete proof and review notes.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `supporting_paper_gerth_hofmann_2019.pdf`: announced follow-up.
- `figures/open_problem_crop_1.png`, `figures/open_problem_crop_2.png`: source
  statement across printed pages 18-19.
- `code/verify_counterexample.py`: numerical soft-threshold sanity check.
- `verification.md`: independent step checklist and scope caveats.

## Human review recommendation

Check the interpretation of "support ... not larger than n(delta)" as the
initial-segment inclusion required to make `(I-P_n)x_alpha^delta=0`. Under
that interpretation, the counterexample is elementary and decisive. It does
not separately settle a possible cardinality-only interpretation.

