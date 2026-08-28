# Problem 5.14(iii): product counterexample

Status: **candidate full solution (likely valid; human review requested)**

Source: Karsten Kruse, *Vector-valued Fourier hyperfunctions and boundary
values*, arXiv:1912.03659v2 (5 November 2025), Problem 5.14(iii), source PDF
page 46.

## Result

The printed equivalence is false. Let \(\mathfrak c=|\mathbb R|\), choose a
set \(I\) with \(|I|=2^{\mathfrak c}\), and give
\(E=\mathbb C^I\) the product topology. Then:

- arbitrary products of strictly admissible spaces are strictly admissible,
  coordinatewise;
- \(E\) is complete and therefore sequentially complete;
- \(E\) is nonmetrizable, so it is not Fréchet;
- \(E\) has no countable fundamental family of bounded sets, while every
  strong dual of a Fréchet space has one;
- \(|E|=2^{2^{\mathfrak c}}>\mathfrak c\), while every PLS-space has
  cardinality at most \(\mathfrak c\).

Thus \(E\) belongs to none of the three classes in Theorem 4.3 but is strictly
admissible. This fully answers Problem 5.14(iii) as literally printed. It does
not answer parts (i), (ii), or (iv).

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: current arXiv v2 source.
- `figures/open_problem_crop.png`: source PDF page 46 crop containing all of
  Problem 5.14.
- `verification.md`: proof audit and novelty-search bounds.

Human review should focus on whether the authors intended an unstated
restriction to a smaller class of “natural” spaces and on the standard
cardinality lemma for PLS-spaces.
