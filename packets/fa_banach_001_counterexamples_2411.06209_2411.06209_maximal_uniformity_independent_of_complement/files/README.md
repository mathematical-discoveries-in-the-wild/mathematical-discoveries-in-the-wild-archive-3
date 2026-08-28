# Maximal unstable uniformity is independent of the complement

Status: `candidate_full_negative_solution_likely_valid`

## Source conjecture

Adam Czornik, Konrad Kitzing, and Stefan Siegmund, *Dichotomies uniform on
subspaces and formulas for dichotomy spectra*, arXiv:2411.06209, Remark 39(b)
on PDF/printed page 20.

The authors conjecture that, for one-sided time, there is a bounded invertible
coefficient system whose maximal unstable uniformity dimension `u2` depends
on the choice of the complementary subspace `L2`.

## Result

The conjecture is false. A stronger transfer theorem holds: if

```text
R^d = L1 direct-sum L2 = L1 direct-sum L2'
```

and the system has a dichotomy with uniformity dimensions `(j1,j2)` on
`(L1,L2)`, then it has a dichotomy with the same dimensions and the same
exponential rate on `(L1,L2')`. Consequently the maximal unstable uniformity
dimension is the same for every complement of the fixed stable space `L1`, in
every dimension.

## Proof idea

Choose finitely many stable basis lines. Their one-dimensional estimates give
an absolute bound `||Phi(n)s|| <= K exp(-alpha n)||s||` for every `s` in
`L1`. Every subspace of another complement is the graph `v -> v+Tv` over a
subspace of the original complement. The graph correction `Phi(n)Tv` decays
like `exp(-alpha n)`, while `Phi(n)v` grows like `exp(alpha n)`. Their ratio
therefore decays like `exp(-2 alpha n)`. After a finite time the graph has the
same unstable estimate; invertibility patches the finitely many earlier
times.

## Files

- `solution_packet.pdf`: complete statement, proof, source evidence, and review notes.
- `main.tex`: self-contained packet source.
- `source_paper.pdf`: the source paper PDF.
- `figures/open_problem_crop.png`: Theorem 38 and Remark 39 from source page 20.
- `verification.md`: proof audit and bounded novelty check.

## Human review recommendation

Check the passage from one-dimensional stable estimates to the absolute
time-zero bound on all of `L1`, and the quantifiers in the graph transfer for
an arbitrary `j2`-plane. Those are the only new steps; the final finite-time
patch is also stated and proved in the packet.
