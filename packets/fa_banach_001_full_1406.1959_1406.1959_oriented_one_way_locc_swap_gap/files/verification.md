# Verification audit

## Proof dependencies

1. The source defines `LOCC^{A->B}` by Alice measuring first and Bob using a
   conditional POVM.
2. For a classical-quantum Hermitian operator, every reverse-direction
   one-way outcome has scalar coefficients
   `m_{j,k,i}=<i|M_{j,k}|i> >= 0` with `sum_k m_{j,k,i}=1`.
3. The triangle inequality bounds every reverse one-way protocol by the local
   protocol that reads the classical label and uses the same first POVM on
   the quantum register.
4. Tensor swap reverses the one-way orientation and preserves unrestricted
   finite-round LOCC.
5. The source's Theorem 3 supplies the `2` versus `C/sqrt(d)` pair and its
   classical-quantum block structure.

## Automated checks

`code/verify_collapse.py` generates random Hermitian blocks, a random POVM on
the quantum side, and random conditional POVMs on the classical side. It
checks the outcome-level identity and the triangle-inequality domination for
hundreds of trials in dimensions 2 through 6.

The randomized checks are diagnostic only. The proof is the exact scalar
inequality in Lemma 1 of `main.tex`.

## Convention boundary

The packet does not claim a result for a class defined as the union of
`LOCC^{A->B}` and `LOCC^{B->A}`. Human review should confirm that the result is
matched to the oriented displayed definition in the source.

