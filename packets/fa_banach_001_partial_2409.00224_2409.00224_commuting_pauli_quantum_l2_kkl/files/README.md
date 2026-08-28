# Quantum L2-KKL for commuting Pauli support

Status: `candidate_partial_likely_valid`.

The full Montanaro--Osborne quantum L2-KKL conjecture remains open. This
packet proves it for every balanced quantum Boolean observable whose
Pauli-Fourier support lies in an abelian Pauli subgroup:

\[
\max_j \operatorname{Inf}_j^2(A) \ge c\,\frac{\log(n+1)}{n}.
\]

The mechanism is a reduction to classical KKL that preserves a useful lower
bound despite global Clifford changes. A rank-m commuting Pauli subgroup is an
isotropic subspace of F_2^(2n). Its 2n scalar local coordinate projections span
the dual, so m of them can be selected as a dual basis. Relabeling Fourier
characters by that basis turns the observable into a balanced classical Boolean
function. Each selected classical influence is at most the corresponding
physical-qubit quantum influence. Classical KKL and m <= n finish the proof.

This complements the existing anticommuting-Pauli partial packet at
`runs/fa_banach_001/solutions/partial/2209.07279_anticommuting_pauli_quantum_kkl`.
The general case still permits cancellation among products of commuting Pauli
terms and is not solved here.

Files:

- `source_paper.pdf`: Blecher--Gao--Xu, arXiv:2409.00224.
- `figures/open_problem_crop.png`: Section 7.1, PDF page 35.
- `main.tex` and `solution_packet.pdf`: complete review packet.
- `code/verify_commuting_transfer.py`: finite consistency checker.

Novelty search through 2026-08-27 found no matching commuting/abelian-Pauli
KKL theorem. Confidence is moderate because the reduction may be folklore.

Human review: likely-valid substantial partial; prioritize the dual-basis
selection and the direction of the influence comparison.
