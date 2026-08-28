# Verification notes

Status: `candidate_full_counterexample_likely_valid`  
Confidence: 98/100  
Result type: full counterexample to Remark 4.15(iii)

## Target

Remark 4.15(iii), printed/PDF page 20 of arXiv:2412.15029, asks whether an
`Fell1(eta)`-base in a Banach algebra `A` implies that every bounded
eta-family in `LUC(A)` admits a common factorization

```text
S_lambda = Psi_lambda . T,
```

where `(Psi_lambda)` is bounded in `LUC(A)*` and `T` is one element of
`LUC(A)`.

## Adversarial checks

1. **The source hypothesis really holds.** Source Theorem 6.1 on printed/PDF
   page 28 states that `L1(G)` has an `Fell1(eta)`-base of type 2 whenever
   `G` is noncompact locally compact and `eta` is its compact covering.
   For `G=R`, `eta=aleph_0`.

2. **The family lies in the target space.** Under the standard group-algebra
   identification `LUC(L1(R))=LUC(R)`, every character
   `S_n(x)=exp(i n x)` is bounded and uniformly continuous. The family has
   constant norm one.

3. **A common bounded factor forces uniform essentiality.** If
   `S_n=Psi_n.T` and `C=sup_n||Psi_n||`, source associativity gives

   ```text
   (Psi_n.T).u = Psi_n.(T.u).
   ```

   Therefore

   ```text
   sup_n ||S_n.u_j-S_n|| <= C ||T.u_j-T||.
   ```

4. **Every individual T in LUC(A) is approximated.** By the source definition,
   `LUC(A)` is the norm-closed span of `A*.A`. On a generator `R.a`,
   `(R.a).u_j=R.(a*u_j)` tends to `R.a`; boundedness of `(u_j)` extends this
   to the closed span. Hence `||T.u_j-T||` tends to zero.

5. **Fourier multiplier computation.** With convolution on `L1(R)` and the
   usual dual pairing,

   ```text
   S_n.u_j = m_j(n) S_n,
   m_j(n) = integral_R u_j(t) exp(i n t) dt.
   ```

   Changing the pairing convention only changes `n` to `-n`.

6. **Contradiction is uniform.** For each fixed `j`, the Riemann-Lebesgue
   lemma gives `m_j(n)->0`. Thus

   ```text
   ||S_n.u_j-S_n|| = |m_j(n)-1| -> 1,
   ```

   so the supremum over `n` is at least one for every `j`. This contradicts
   item 3.

7. **No positivity issue.** The argument applies to any bounded approximate
   identity in `L1(R)`; positivity or a special kernel is not needed.

8. **The one-factor theorem is untouched.** Each single character may still
   factor as in source Theorem 4.16. The obstruction concerns a bounded
   countable family sharing one common target-space factor.

## Numerical illustration

For the Gaussian approximate identity

```text
u_j(t) = j/sqrt(pi) exp(-j^2 t^2),
```

the multiplier is `m_j(n)=exp(-n^2/(4j^2))`. The supplied script checks that
at `n=20j` the defect exceeds `1-10^-40` for several `j`. This illustrates,
but is not needed for, the proof.

## Novelty audit

- No matching run-index entry was found for arXiv:2412.15029 or the target.
- The official arXiv record still lists only v1, submitted 2024-12-19.
- Exact target-phrase, title/author, `Fell1`/`LUC(A)` factorization, and
  character/approximate-identity searches found no explicit answer.
- The bounded search does not establish absolute novelty.

## Recommended human focus

Check the module-action orientation against source equations (1) and (5), and
confirm the source's standard group-algebra identification of `LUC(A)` with
`LUC(R)`. The norm contradiction is then immediate.
