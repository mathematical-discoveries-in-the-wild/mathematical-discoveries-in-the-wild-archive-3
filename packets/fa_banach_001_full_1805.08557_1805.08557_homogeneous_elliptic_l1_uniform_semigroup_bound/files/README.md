# Uniform L1 semigroup bound for homogeneous elliptic operators

Status: candidate full solution, likely valid, awaiting specialist review.

This packet gives a complete affirmative answer to Question 4.5 of
arXiv:1805.08557 in the constant-coefficient setting fixed by the paper.
For a positive homogeneous elliptic polynomial symbol `P` of even order `m`,

\[
\|e^{-tP(D)}u\|_1\le M_P\|u\|_1 \qquad(t>0),
\]

where `M_P` is independent of time and of `u`. Hence the question's requested
estimate holds with `beta=0`. Combining the bound with the paper's homogeneous
Nash inequality yields the predicted `O(t^{-d/m})` L2-decay.

The mechanism is exact heat-kernel scaling: the time-one kernel is Schwartz,
and every positive-time kernel is an L1-norm-preserving dilation of it. No
positivity of the kernel is needed.

Contents:

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of Question 4.5 and its
  stated decay consequence on source PDF page 14.
- `VERIFICATION.md`: mathematical, source, novelty, and artifact checks.
- `code/make_open_problem_crop.py`: reproducible source crop.

The result does not address variable-coefficient or nonhomogeneous elliptic
operators; those are outside the question's surrounding Section 4 framework.
