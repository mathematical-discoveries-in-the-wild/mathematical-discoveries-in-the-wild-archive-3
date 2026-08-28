# Verification report

Verdict: **likely valid candidate partial result**.

## Logical audit

1. **Reduction to eigenvalue vectors.** Continuous diagonalizability gives
   `A=V^*D_aV` and `B=W^*D_bW`. Continuous doubly stochastic majorization
   implies `a(x)` lies in the permutahedron `P(b(x))` pointwise.
2. **No-crossing partition.** If `B(x)` has simple spectrum everywhere, each
   ordering condition on the labeled eigenvalues is clopen. There are at most
   `n!` such pieces, and a fixed permutation sorts `b` on each piece.
3. **Toric slice.** The closure of a generic diagonal-torus orbit in `Fl(n)` is
   the permutohedral toric variety. Its nonnegative part maps homeomorphically
   to the weighted permutahedron under the weighted moment map. The moment map
   on the Hermitian orbit is the diagonal map.
4. **Unitary lift.** The nonnegative toric part is homeomorphic to a polytope,
   hence contractible. The restricted principal torus bundle
   `U(n) -> Fl(n)` is therefore trivial and has a continuous section.
5. **Joint continuity.** Over the compact eigenvalue image `K` inside the open
   Weyl chamber, `(b,t) -> (b,theta_b(t))` is a continuous bijection from a
   compact space to a Hausdorff space. Its inverse is continuous.
6. **Exact dephasing.** Averaging conjugations by the `n` cyclic diagonal phase
   matrices kills all off-diagonal entries exactly. Substitution of the two
   source diagonalizers gives the displayed continuous unitaries `U_k`.

The proof does not cross a Weyl-chamber wall. At an eigenvalue collision the
moment map collapses faces, so the joint inverse used above need not persist.

## Numerical algebra check

Run from the repository root:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2210.13309_no_crossing_exact_unitary_convexity/code/verify_dephasing.py
```

Captured output is in `code/verification_output.txt`. The checker generates
random unitary data for sizes 2 through 8 and verifies:

- the cyclic phase average equals the diagonal projection;
- the proposed `U_k=W^*Q^*Omega^kV` are unitary;
- their equal-weight conjugation average equals `A`.

The maximum reported Frobenius residual is below `1e-13` in every size.

## Code/proof boundary

The numerical checker validates only the finite Fourier and conjugation
algebra. The existence and continuity of the toric slice are mathematical
inputs audited from the supporting papers; they are not established by the
script.
