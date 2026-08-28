# Verification audit

## Exact proof dependencies

1. `D_s` is a continuous doubly stochastic field and exactly sends the
   diagonal vector of `B` to that of `A`.
2. For a unitary `U`, the diagonal of `U^* diag(b) U` is `E b`, where
   `E_{ik}=|U_{ki}|^2`; `E` is unistochastic and doubly stochastic.
3. The map `b(z1,z2)=(z1,z2,-z1-z2)` maps `R^2` onto the trace-zero plane.
   Taking radial limits at `z=0` therefore identifies a doubly stochastic
   matrix on that plane, and its action on `(1,1,1)` identifies the remaining
   direction.
4. Positivity of all convex weights and matrix entries transfers every zero
   of `D_s` to every unistochastic summand.
5. A unitary supported in the pattern of `I+P` realizes only `I` or `P` at
   the modulus-square level. This follows from one orthogonality product and
   propagation of row/column norm constraints.
6. A continuous map from connected `[0,1]` to `{I,P}` is constant.

## Automated checks

`code/verify_construction.py` deterministically verifies:

- row and column sums and nonnegativity of sampled `D_s`;
- the equality defining `A` from `D_s b(z)`;
- recovery of every sampled `D_s` from its action on the two columns of the
  trace-zero basis together with its action on `(1,1,1)`;
- the support-zero pattern for all `s`;
- enumeration of the permutation matrices whose supports lie in `I+P`,
  yielding exactly `I` and `P`.

The script does not replace the compactness/continuity limit or the
unistochastic support proof. Those are audited symbolically in `main.tex`.

