# Literature-implied answer to Problem 49

status: `literature_implied_answer (full Problem 49)`

source: Shota Mori, *The heat kernel on SL(2,R)*, arXiv:1909.03670v3.

supporting theorem: Junfang Li and Xiangjin Xu, *Differential Harnack
inequalities on Riemannian manifolds I: linear heat equation*,
arXiv:0901.3849, Theorem 1.4.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1909.03670_later_time_heat_l2_density_via_harnack/`

ledger: `runs/fa_banach_001/ledger/results/1909.03670_later_time_heat_l2_density_via_harnack.json`

## Source question

Problem 49 on PDF page 25 asks whether, for every `t, epsilon > 0`,

```text
L2(SL(2,R), rho(t+epsilon,g) dg)
```

is a dense subspace of

```text
L2(SL(2,R), rho(t,g) dg).
```

## Identification

The paper equips `SL(2,R)` with a left-invariant Riemannian metric. Such a
metric is complete, and its Ricci tensor has a global lower bound because left
translations are isometries. Apply Li--Xu's parabolic Harnack inequality to
the positive heat solution `u(g,s)=rho(s,g)` at the same spatial point and at
times `t` and `t+epsilon`. It gives a finite constant `C(t,epsilon)` such that

```text
rho(t,g) <= C(t,epsilon) rho(t+epsilon,g)  for every g.
```

Therefore the later-time weighted space embeds continuously into the
earlier-time space. Every compactly supported continuous function belongs to
both spaces, and these functions are dense in the earlier-time weighted
`L2` space. This proves Problem 49 in full.

The same argument works for every connected noncompact Lie group with a
left-invariant Riemannian metric; compact groups follow directly from
positivity and compactness of the two heat kernels.

## Provenance and scope

This is an agent-identified implication of a theorem published before the
source question, not a new theorem of this run. Li and Xu do not discuss
Mori's later Problem 49. The relation is therefore stored under
`literature_implied_answers`.

The packet resolves only Problem 49. It makes no claim about the matrix-entry
density question (Problem 48) or the holomorphic Problems 46--47 for
`SL(2,C)`.

The bounded novelty check searched the run registry and exact phrases from
Problem 49, together with arXiv:1909.03670 and the author/title. No later paper
explicitly stating an answer was found. The official arXiv record remains v3
(2 October 2019). The decisive theorem is the earlier Li--Xu Harnack theorem.

## Files

- `main.tex`: compact identification note and proof.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1909.03670v3.
- `supporting_paper_0901.3849.pdf`: Li--Xu's Harnack theorem.
- `verification.md`: hypothesis and scope audit.
