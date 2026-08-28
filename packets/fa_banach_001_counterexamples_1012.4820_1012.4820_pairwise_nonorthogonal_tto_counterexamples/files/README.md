# Pairwise-nonorthogonal complex symmetric matrices without TTO models

Status: `candidate counterexample likely valid; human review needed`

Agent/model: `agent_lane_04` / `GPT5.6`

Source question: Garcia, Poore, and Ross, *Unitary equivalence to a
truncated Toeplitz operator: analytic symbols*, arXiv:1012.4820, Section 7,
Question 2, PDF page 13.

> Let n >= 4. Is every complex symmetric matrix in M_n(C) having no pair
> of orthogonal, nonzero eigenvectors unitarily equivalent to a truncated
> Toeplitz operator?

## Candidate result

No.  For every `n >= 10` there exists a complex symmetric `n x n` matrix
with simple spectrum whose nonzero eigenvectors are pairwise nonorthogonal,
but which is not unitarily equivalent to any truncated Toeplitz operator.

The proof strengthens the semialgebraic-dimension argument of Ryan
O'Loughlin, arXiv:2607.14019.  The new input is that the simple-spectrum,
pairwise-nonorthogonal locus is a nonempty open semialgebraic subset of the
space of complex symmetric matrices and therefore has full real dimension
`n(n+1)`.  O'Loughlin's TTO-model locus has dimension at most

```text
7n - 6 + n(n-1)/2 < n(n+1)  (n >= 10),
```

so it cannot contain that locus.

Nonemptiness is proved explicitly: choose a real skew-symmetric matrix `K`
with every off-diagonal entry nonzero, put `Q(t)=exp(i t K)`, and set
`S=Q(t) diag(1,...,n) Q(t)^T`.  For all sufficiently small nonzero `t`,
`Q(t)^T Q(t)=I` while every off-diagonal entry of
`Q(t)^*Q(t)=exp(2 i t K)` is nonzero.  Thus the columns of `Q(t)` are
pairwise nonorthogonal eigenvectors of the symmetric matrix `S`.

## Files

- `solution_packet.pdf`: full review packet
- `main.tex`: packet source
- `source_paper.pdf`: arXiv:1012.4820
- `supporting_paper_2607.14019.pdf`: dimension theorem used in the proof
- `figures/open_problem_crop.png`: source Question 2
- `code/verify_open_locus_example.py`: numerical sanity check at `n=10`
- `verification_output.txt`: recorded output

The code checks only the elementary nonempty-locus construction and the
dimension arithmetic; it is not a substitute for the proof or for the cited
semialgebraic-dimension theorem.

## Scope and review focus

This is an existential counterexample, not an explicit matrix certified to
lie outside the TTO locus.  It settles the universal Question 2 negatively
and works in every dimension `n >= 10`; dimensions `4,...,9` remain open.
Question 4 about `A direct-sum A^T` is not addressed.

Human review should focus on (i) the semialgebraicity and openness of the
pairwise-nonorthogonal simple-spectrum locus and (ii) the implication from a
TTO model to membership in O'Loughlin's set `U(C)`.
