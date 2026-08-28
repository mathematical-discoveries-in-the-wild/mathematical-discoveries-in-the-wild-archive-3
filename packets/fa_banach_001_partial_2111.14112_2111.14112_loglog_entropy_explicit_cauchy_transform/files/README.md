# Explicit disk-algebra Cauchy transforms under log-log entropy

Status: `candidate_substantial_partial_likely_valid`.

Limani and Malman, arXiv:2111.14112v3, Introduction, PDF page 6, ask for
an explicit formula for a nonzero measurable function supported on an
arbitrary closed set whose Cauchy transform belongs to the disk algebra.
Their explicit construction gives the much stronger class `A^infinity` under
the Beurling-Carleson entropy condition.

This packet gives an explicit formula under the strictly weaker condition

    sum_k |I_k| log log(e^e/|I_k|) < infinity,

where the `I_k` are the complementary arcs.  A logarithmically weakened
version of the source's exterior-pole cutoff decays like a negative power of
`log(1/dist)` at the closed set.  Extending its conjugate boundary trace by
zero across the set produces a Dini-continuous function.  The classical Dini
theorem for conjugate functions then puts its analytic projection in the disk
algebra.  An anti-analytic cancellation identity turns this projection into
the desired Cauchy transform supported on the closed set.

The new hypothesis is genuinely weaker than Beurling-Carleson entropy.  A
family with about `e^k/k^2` gaps of length `e^-k` has finite log-log entropy,
infinite Beurling-Carleson entropy, and positive remaining measure after a
small common scaling.

The arbitrary-closed-set problem remains open.  Bounded searches through
2026-08-27 for the exact problem together with `Dini`, `log log`, and
`Beurling-Carleson` found no matching extension.  Novelty confidence is
moderate.

Files:

- `main.tex` and `solution_packet.pdf`: complete review packet.
- `source_paper.pdf`: Limani--Malman source paper.
- `figures/open_problem_crop.png`: the exact open statement on PDF page 6.
- `code/check_entropy_example.py`: numerical check of the strictness example
  and the Whitney log-log summability comparison.

Human review should focus on the boundary derivative estimate, the Dini
modulus argument, and the use of continuity of the conjugate function.
