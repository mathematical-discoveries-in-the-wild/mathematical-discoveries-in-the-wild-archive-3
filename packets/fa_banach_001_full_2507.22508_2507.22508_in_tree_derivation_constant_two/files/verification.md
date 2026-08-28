# Verification audit

## Mathematical dependencies

1. Source Lemma 6.2: every derivation on the tensor algebra of a finite tree
   is inner with an implementer in the algebra.
2. The vertex projections are pairwise orthogonal and sum to the identity.
3. A tree has no positive-length path with equal source and range.
4. In an in-tree, every vertex has a directed path to the range root.

## Proof checks

- Averaging over all diagonal sign unitaries is a contractive expectation
  onto the vertex diagonal and expresses the off-diagonal part as an average
  of commutators evaluated by the derivation.
- Multiplying a positive-length path by another positive-length path either
  gives zero or increases length.  Hence the coefficient at a chosen path in
  the implementer commutator comes only from the vertex diagonal.
- The Fourier coefficient functional is the matrix coefficient
  $A\mapsto\langle A\xi_{s(p)},\xi_p\rangle$ and has norm at most one.
- The whole path from a vertex to the root is used directly, so no depth
  factor accumulates.

## Automated diagnostic

`code/verify_tree_averaging.py` builds the finite left-regular path matrices
for random rooted in-trees.  It checks the sign-average identity, the norm
bound for the positive-length part, and the exact path-coefficient formula.
This is diagnostic only; the formal proof is independent of computation.

## Human review recommendation

Check the multiplication convention for $L_pL_q$, the sign in the definition
of $\delta_T$, and the claim that no positive-length product contributes to
the coefficient at $L_p$.  These are the only convention-sensitive points.
