# Literature-implied answer: quaternion RIP threshold improves to 4/sqrt(41)

status: `literature_implied_answer`

source: Agnieszka Badeńska and Łukasz Błaszczyk, *Compressed sensing for
real measurements of quaternion signals*, arXiv:1605.07985.

supporting result: Yi Gao and Mingde Ma, *A new bound on the block restricted
isometry constant in compressed sensing*, Journal of Inequalities and
Applications 2017:174, DOI 10.1186/s13660-017-1448-2.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1605.07985_quaternion_block_rip_upgrade/`

ledger: `runs/fa_banach_001/ledger/results/1605.07985_quaternion_block_rip_upgrade.json`

## Identification

On PDF page 12, after Corollary 5.1, the source conjectures that its sufficient
condition `delta_(2s) < 1/3` is not optimal for quaternion `l1` recovery with a
real measurement matrix.

Realify each quaternion coordinate as one block in `R^4`. Then quaternion
`l1` is exactly the mixed block norm `l2/l1`, and the real sensing operation is
`A = Phi tensor I_4`. The scalar `k`-RIC of `Phi` equals the block `k`-RIC of
`A`: one inequality follows by summing the four componentwise RIP inequalities,
and the reverse follows by restricting to the real quaternion component.

Gao--Ma's Theorem 1 (PDF page 3) gives exact recovery of every block
`s`-sparse signal, and stable noisy recovery, when

`delta_(2s|I) < 4/sqrt(41) approximately 0.6246`.

Therefore their theorem applies verbatim after realification and strictly
improves the source's `1/3` threshold. This fully affirms the stated
nonoptimality conjecture for the source's real-measurement setting.

## Literature status and scope

The implication is agent-identified. Gao and Ma do not mention quaternion
signals or arXiv:1605.07985, and the source predates their paper. Accordingly
this is recorded as a literature-implied answer, not a new proof or an explicit
later-paper resolution.

The packet does not claim that `4/sqrt(41)` is optimal. It also does not address
genuinely quaternion-valued sensing matrices; it answers exactly the source's
real-matrix conjecture.

## Files

- `main.tex` and `solution_packet.pdf`: compact status note and identification proof.
- `source_paper.pdf`: arXiv:1605.07985.
- `supporting_paper_gao_ma_2017.pdf`: decisive block-recovery theorem.
- `verification.md`: independent scope and algebra checks.

