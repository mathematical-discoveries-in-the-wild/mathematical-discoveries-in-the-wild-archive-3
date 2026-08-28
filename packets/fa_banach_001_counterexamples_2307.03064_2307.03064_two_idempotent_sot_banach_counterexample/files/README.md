# Counterexample packet: two idempotents do not suffice on every separable Banach space

Status: \`candidate_counterexample_likely_valid\`

Source paper: Jean-Christophe Bourin, *A Journey into Matrix Analysis*, arXiv:2307.03064.

Target: Question 5.2.9 on source PDF page 82 asks whether, for a separable Banach space \`X\` and every \`T\` in \`L(X)\`, there are idempotents \`P_n,Q_n\` such that \`P_n+Q_n\` converges strongly to \`T\`.

Answer claimed here: no, even for a separable infinite-dimensional space. Allexandrov--Kutzarova--Plichko construct a closed subspace \`X\` of the Gowers--Maurey hereditarily indecomposable space which fails the compact approximation property. On an indecomposable space every idempotent is finite-rank or finite-codimensional. Consequently every sum of two idempotents is a finite-rank perturbation of one of \`0\`, \`I\`, or \`2I\`. If such sums converged strongly to \`(1/2)I\`, a constant-scalar subsequence would yield uniformly bounded finite-rank operators converging strongly to \`I\`. They converge uniformly on compact sets, giving the bounded approximation property and hence the compact approximation property, a contradiction.

Packet files:

- \`main.tex\`: complete proof packet with source statement, proof intuition, theorem, proof, verification notes, limitations, and references.
- \`solution_packet.pdf\`: rendered proof packet.
- \`verification_report.md\`: explicit adversarial verification report.
- \`source_paper.pdf\`: original arXiv source paper.
- \`supporting_paper_allexandrov_kutzarova_plichko_1999.pdf\`: decisive existence source for the HI space without CAP.
- \`figures/open_problem_crop.png\`: readable full-width crop of Question 5.2.9.

Duplicate and novelty check:

- The four cheap indexes were searched for \`2307.03064\`, the exact title, the exact question phrase, \`two idempotents\`, \`strong limit\`, \`bounded approximation property\`, \`compact approximation property\`, and the supporting authors; no matching result or attempt was found.
- The surrounding source text was inspected. Question 5.2.9 is the final item in Section 5.2 and is not answered nearby, so it is not a same-paper extraction false positive.
- Bounded external searches on 2026-08-26 used the exact question wording and close variants such as \`strong limit of sums of two idempotents\` and \`strong operator sums of two idempotents Banach space\`. They found the source paper and unrelated work on algebraic sums or linear combinations of idempotents, but no later answer or this CAP obstruction.
- This was not a comprehensive MathSciNet or zbMATH search; novelty confidence is therefore moderate while proof confidence is high.

Human review focus:

- Confirm that the 1999 supporting proposition supplies a closed separable HI subspace without CAP over the intended scalar field.
- Check the passage from a constant \`0/1/2\` subsequence to uniformly bounded finite-rank approximants of the identity.

Ledger record: \`runs/fa_banach_001/ledger/results/2307.03064_two_idempotent_sot_banach_counterexample.json\`.
