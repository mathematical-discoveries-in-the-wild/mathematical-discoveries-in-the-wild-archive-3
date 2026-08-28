# Verification report

Candidate: arXiv:1012.4820, Section 7, Question 2

Claim checked: for every `n >= 10`, some complex symmetric `n x n` matrix
has simple spectrum and pairwise Hermitian-nonorthogonal eigenvectors but is
not unitarily equivalent to a truncated Toeplitz operator.

Verdict: `likely valid`; send to human review.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source match | valid | The crop and source PDF show the exact Question 2 on PDF page 13. |
| Semialgebraicity of the good locus | valid | Simple spectrum is a discriminant inequality. The bad-pair relation is a real polynomial system with normalized eigenvectors, distinct eigenvalues, and zero Hermitian inner product; Tarski-Seidenberg handles its projection. |
| Openness | valid | On the simple-spectrum locus the finitely many eigenlines vary locally continuously; nonzero cross-inner-products persist. |
| Nonemptiness | valid | For real skew `K`, `Q(t)=exp(itK)` has `Q(t)^T Q(t)=I`; because `itK` is Hermitian, its Hermitian Gram matrix is `exp(2itK)`, whose off-diagonal derivatives at zero are nonzero. Distinct diagonal eigenvalues then give a symmetric matrix in the locus. |
| Full dimension | valid | A nonempty open semialgebraic subset of the real vector space of symmetric complex matrices has dimension `n(n+1)`. |
| TTO-locus bound | external, verified in source | arXiv:2607.14019 proves semialgebraicity and the bound `7n-6+n(n-1)/2`; it is strict against `n(n+1)` for `n>=10`. |
| TTO model implies membership in `U(C)` | valid from external statements | The supporting paper's Theorem 4.1 gives a symmetric representative, and Lemma 4.2 gives its rank-two commutator certificate. |
| Final dimension exclusion | valid | A semialgebraic set of dimension below `n(n+1)` cannot contain the full-dimensional good locus. |

## Counterexample search and computation

The included script checks the elementary construction at `n=10`, `t=0.01`.
All assertions pass. This numerical matrix is not claimed to have been
certified outside the TTO locus; the actual counterexample is existential via
dimension.

## Remaining reviewer focus

- Confirm that O'Loughlin's `U(C)` contains every *symmetric matrix* that is
  unitarily equivalent to a finite-dimensional TTO, not only a preferred
  matrix representation. This follows from the definition of `U(C)` and
  transitivity of unitary equivalence.
- Confirm the intended quantifier in the source. The packet gives failure for
  every `n>=10`, which is enough to negate the universal question; it does not
  settle dimensions `4` through `9`.

Confidence: 92/100. No logical gap or computational contradiction found;
novelty remains provisional.
