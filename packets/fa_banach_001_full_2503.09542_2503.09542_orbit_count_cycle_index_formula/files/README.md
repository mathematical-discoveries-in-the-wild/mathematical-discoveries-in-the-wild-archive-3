# Exact cycle-index formula for left-right orbits of subsets of permutations

Status: **candidate full solution, likely valid**.

This packet gives a complete explicit formula and a constructive scalar recurrence for Question 3.5 in Aman Kushwaha and Raghavendra Tripathi, *A note on Erdos matrices and Marcus-Ree inequality*, arXiv:2503.09542, Linear Algebra and its Applications 725 (2025), 223-247. The source asks for the number `f_{n,k}` of equivalence classes of `k`-subsets of `S_n` under left and right multiplication and whether these numbers satisfy some recurrence.

## Result

For partitions `lambda, eta` of `n`, the packet computes the cycle counts of the transformation

`sigma -> mu sigma nu^{-1}`

directly from the cycle types of all powers of `mu` and `nu`. Burnside's lemma then gives

`f_{n,k} = sum_{lambda,eta} (z_lambda z_eta)^{-1} [x^k] product_l (1+x^l)^{c_l(lambda,eta)}`.

All quantities in this expression are given explicitly by gcd, lcm, centralizer-size, and Mobius-inversion formulas. Thus it determines `f_{n,k}` for every `n` and `k` without enumerating subsets of `S_n`.

For the recurrence clause, the fixed-subset polynomials span an explicit finite-dimensional space. A basis Wronskian gives a scalar differential equation for `F_n(x)=sum_k f_{n,k}x^k`; coefficient extraction yields a scalar finite-shift recurrence in `k` whose coefficients are computed from partition power-types, not from previously tabulated `f_{n,k}`. This answers the recurrence question in the natural fixed-`n`, coefficient direction. No low-order recurrence uniform in `n` is claimed.

## Files

- `main.tex`: self-contained statement, proof, verification notes, limitations, and novelty audit.
- `solution_packet.pdf`: rendered human-review packet.
- `source_paper.pdf`: the arXiv v3 source paper.
- `figures/open_problem_crop.png`: full-width crop of Question 3.5 on PDF page 12.
- `code/verifier.py`: exact-arithmetic implementation of the formula plus direct finite-group checks.
- `code/recurrence_verifier.py`: symbolic construction and exact verification of the scalar Wronskian recurrence.

## Verification

From the repository root, run:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/full/2503.09542_orbit_count_cycle_index_formula/code/verifier.py

conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/full/2503.09542_orbit_count_cycle_index_formula/code/recurrence_verifier.py
```

The script:

1. reproduces every value printed in the source through `n=5, k=12`, including `732149722382`;
2. independently enumerates the cycles of the left-right action for every pair of conjugacy types for `1 <= n <= 4`; and
3. checks that those direct cycle counts agree with the power-type and Mobius-inversion formula.
4. reports the fixed-subset polynomial span dimensions `1,2,4,10,19` for `1 <= n <= 5`;
5. constructs the fourth-order Wronskian operator for `n=3`; and
6. verifies its differential equation and scalar coefficient recurrence exactly.

The computation is a consistency check, not a substitute for the proof.

## Novelty status

The bounded search covered the run indexes, the exact arXiv id and title, exact question phrases, related left-right subset-orbit phrases, recurrence and Wronskian variants, and OEIS A381842 through 2026-08-26. The source and the OEIS entry contain only the initial values, `f_{n,2}=p(n)-1`, and complement symmetry; neither states the formula or recurrence in this packet. No later matching answer was found. Novelty confidence is moderate rather than definitive because these are natural applications of Burnside's lemma and Wronskian elimination and may occur in older literature under different terminology.

## Human review recommendation

Prioritize the fixed points of a power, the conjugator count, Mobius inversion for action cycles, and the fixed-subset generating polynomial. Then verify that the Wronskian coefficients are constructed independently of `f_{n,k}` and that coefficient extraction gives the displayed scalar recurrence. A reviewer should confirm that recurrence in `k` for each fixed `n` is the intended reading of the source's unspecified recurrence clause. A separate literature specialist should search older work on two-sided translation orbits of subsets of finite groups before any novelty claim is publicized.
