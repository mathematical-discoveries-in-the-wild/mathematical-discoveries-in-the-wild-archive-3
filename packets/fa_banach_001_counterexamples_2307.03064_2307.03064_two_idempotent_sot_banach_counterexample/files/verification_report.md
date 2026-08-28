# Verification Report

Candidate: arXiv:2307.03064, Question 5.2.9

## Claim Checked

There is a separable infinite-dimensional Banach space \`X\` and an operator \`T=(1/2)I_X\` which is not a strong-operator limit of sums \`P_n+Q_n\` of two idempotents on \`X\`.

## Verdict

\`likely valid\`

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Existence of \`X\` | external, verified | Allexandrov--Kutzarova--Plichko (1999) state that a closed subspace of the Gowers--Maurey HI space can be chosen without the compact approximation property. The paper also records that the ambient Gowers--Maurey space is hereditarily indecomposable, hence its closed subspace \`X\` is indecomposable. |
| Form of idempotents | valid | For an idempotent \`P\`, \`X=ran(P) direct-sum ker(P)\`. Indecomposability forces one summand finite-dimensional. Thus either \`P\` or \`I-P\` is finite-rank, so \`P=epsilon I+F\` with \`epsilon\` in \`{0,1}\` and \`F\` finite-rank. |
| Scalar subsequence | valid | Each \`P_n+Q_n=k_n I+F_n\` with \`k_n\` in \`{0,1,2}\` and \`F_n\` finite-rank. An infinite subsequence has constant \`k_n=k\`. Since \`1/2-k\` is never zero, division is legitimate. |
| Uniform boundedness | valid | Strong convergence of \`F_n\` to \`(1/2-k)I\` makes each orbit \`{F_n x}\` bounded. The uniform boundedness principle gives \`sup ||F_n||<infinity\`. |
| Approximation implication | valid | The normalized finite-rank operators converge pointwise to \`I\` and are uniformly bounded. A finite-net argument upgrades convergence to uniform convergence on each compact subset, yielding BAP. Finite-rank maps are compact, so BAP implies CAP. |
| Contradiction and scope | valid | CAP contradicts the defining property of \`X\`. The source question is universal in \`X,T\`; one separable infinite-dimensional counterexample answers it negatively. |

## Counterexample Search

Small cases checked: no computation is relevant. The proof was attacked at the three possible failure points: unbounded individual idempotents, changing scalar classes \`k_n\`, and the distinction between pointwise and compact-uniform convergence. Individual idempotent norms are not used; a constant scalar class is obtained by a subsequence; and uniform boundedness supplies the equicontinuity needed on compact sets.

Result: no counterexample to the argument found.

## External Dependencies

- G. Allexandrov, D. Kutzarova, and A. Plichko, *A Separable Space with No Schauder Decomposition*, Proceedings of the AMS 127 (1999), 2805--2806. The precise existence proposition and HI observation were checked in the copied PDF.

## Gaps

- The supporting article is written in the standard Banach-space setting without emphasizing the scalar field in the proposition. A reviewer who reads Bourin's question as complex-only should confirm the complex Gowers--Maurey version (the construction and Szankowski criterion are standard over the complex field).
- The novelty search was bounded and did not include subscription databases.

## Confidence

Score: 94/100.

Reason: the internal proof is short and uses only exact decompositions, a pigeonhole subsequence, the uniform boundedness principle, and the definition of BAP/CAP. The only material external input is an explicit published existence proposition.

## Human Review Recommendation

\`send to human\`
