# Full-solution packet: correlated Gaussian weights have the Smirnov property

Status: `candidate_full_solution_likely_valid`

Source paper: Eberhard Mayerhofer, *The Smirnov Property for Weighted Lebesgue Spaces*, arXiv:2101.02470.

Target: Remark 2.10 asks whether a bivariate standard normal density with nonzero correlation has the Smirnov property. In probabilistic language: if `(X,Y)` is the correlated Gaussian pair, `F(X),G(Y)` are integrable, and `F(X)+G(Y)` lies in `L^q`, must each summand lie in `L^q`?

Answer claimed here: yes, for every `1 < q < infinity` and every nondegenerate bivariate Gaussian distribution. Conditional expectations give

`A = F + P_rho G` and `B = P_rho F + G`,

where `P_rho` is the Gaussian noise operator. Therefore `B - P_rho A = (I-P_{rho^2})G` belongs to `L^q`. A resolvent lemma proves that, for `0 <= t < 1`, an `L^1` function `g` with `(I-P_t)g` in `L^q` must itself be in `L^q` modulo constants. The lemma uses the exact Hermite spectral gap on `L^2`, interpolation to make a high power a strict contraction on `L^q`, and an `L^1` fixed-point argument. It follows that `G` and then `F` belong to `L^q`.

Packet files:

- `main.tex`: self-contained full proof, scope, uniqueness consequence, adversarial checks, novelty check, and references.
- `solution_packet.pdf`: rendered proof packet.
- `verification_report.md`: explicit adversarial verification report.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: readable crop of the exact source question.

Uniqueness consequence:

- This resolves the missing Smirnov hypothesis for every nondegenerate bivariate Gaussian weight.
- For correlation `rho`, the packet computes the source theorem's separate likelihood-ratio condition (2.3): it holds exactly when `p*abs(rho) < 1`, where `p` is the theorem's exponent. Equivalently, for its conjugate Smirnov exponent `q`, the range is `q > 1/(1-abs(rho))`.
- Mayerhofer's uniqueness conclusion therefore applies in that sharp range whenever the theorem's stated marginal assumptions also hold. Outside it, the Smirnov result remains valid but condition (2.3) fails.

Duplicate and novelty check:

- The four cheap indexes were searched for `2101.02470`, the exact title, `bivariate normal`, `Gaussian`, `Smirnov property`, and `Ornstein-Uhlenbeck`; no matching result or attempt was found.
- The source context was inspected. Remark 2.10 and the conclusion explicitly label this as unknown, so it is not a same-paper extraction false positive.
- Bounded external searches on 2026-08-26 used the exact question and the Gaussian-noise/operator formulation. They found the source and its 2024 published version, which still states the question as unknown, but no later resolution or this proof.
- This was not a comprehensive MathSciNet or zbMATH search, so novelty confidence is moderate while proof confidence is high.

Human review focus:

- Verify the `L^q` invertibility of `I-(P_t-Pi)` via a strict-contraction power.
- Verify the `L^1` assertion that every `P_t`-fixed mean-zero function is zero.
- Confirm the precise scope of the source theorem's uniqueness conclusion under its other hypotheses.

Ledger record: `runs/fa_banach_001/ledger/results/2101.02470_correlated_gaussian_smirnov_property.json`.
