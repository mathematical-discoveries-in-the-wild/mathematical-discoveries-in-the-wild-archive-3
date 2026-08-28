# Literature-implied answer: Gaussian row/column equivalence

status: `literature_implied_answer (full Gaussian question)`

source: Stiene Riemer and Carsten Schütt, *On the Expectation of the Norm
of Random Matrices with Non-Identically Distributed Entries*,
arXiv:1203.3713.

supporting theorem: Rafał Latała, Ramon van Handel, and Pierre Youssef,
*The dimension-free structure of nonhomogeneous random matrices*,
arXiv:1711.00807, Theorem 3.1 (the probabilistic form of Theorem 1.1).

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1203.3713_gaussian_row_column_equivalence_via_1711.00807/`

ledger: `runs/fa_banach_001/ledger/results/1203.3713_gaussian_row_column_equivalence_via_1711.00807.json`

## Identification

On page 3 of arXiv:1203.3713, immediately after display (2), Riemer and
Schütt state that they know no coefficient matrix for which the expected
Gaussian operator norm is not of the same order as the sum of the expected
maximal Euclidean row and column norms.

Theorem 3.1 on page 16 of arXiv:1711.00807 proves the corresponding row-norm
equivalence for every symmetric Gaussian matrix. Apply it to the symmetric
block dilation

```text
        X = [ 0   G  ]
            [ G^T 0  ].
```

Then `||X|| = ||G||`, while the largest row norm of `X` is the maximum of
the largest row norm and largest column norm of `G`. The expectation of this
maximum and the sum of the two expectations differ by at most a factor of
two. This gives the full Gaussian equivalence suggested in arXiv:1203.3713,
with universal constants.

## Provenance and scope

This is an agent-identified implication, not a new theorem of this run.
Latała--van Handel--Youssef explicitly say that their theorem settles
Latała's symmetric Gaussian conjecture, but the inspected text does not
explicitly identify Riemer--Schütt's rectangular row/column formulation.
That formulation follows immediately by block dilation, so this packet is
stored under `literature_implied_answers`.

The conclusion covers arbitrary deterministic coefficient matrices with
independent standard Gaussian multipliers. It does not extend the source
paper's arbitrary independent mean-zero estimate (Theorem 2.2) beyond the
Gaussian class.

## Files

- `main.tex`: compact theorem-identification note and proof.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1203.3713.
- `supporting_paper_1711.00807.pdf`: decisive supporting theorem.
- `source_tex/`: exact arXiv TeX sources used to verify the passages.
