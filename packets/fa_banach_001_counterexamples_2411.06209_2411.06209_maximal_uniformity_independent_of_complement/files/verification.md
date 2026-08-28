# Verification report

Verdict: `candidate_full_negative_solution_likely_valid`

## Claim audited

For a one-sided bounded invertible difference system and a fixed stable space
`L1`, every dichotomy uniformity-dimension pair `(j1,j2)` transfers from one
complement of `L1` to every other complement, with the same exponent. Hence
the maximal unstable uniformity dimension is complement-independent and the
existential conjecture in Remark 39(b) of arXiv:2411.06209 is false.

## Proof audit

1. **Common rate.** By the source definition, one exponent `alpha > 0` works
   for all uniformity subspaces. Refinement to one-dimensional stable lines
   preserves this same exponent.

2. **Uniform absolute stable bound.** Choosing an orthonormal basis of `L1`
   uses only finitely many line constants. Cauchy--Schwarz then gives
   `||Phi(n)s|| <= K exp(-alpha n)||s||` for every `s in L1`. No uniform
   estimate on all of `L1` between arbitrary starting times is asserted or
   needed.

3. **Graph representation.** Projection onto the original complement along
   `L1` restricts to an isomorphism from any `j2`-plane in a new complement
   onto a `j2`-plane in the original complement. The new plane is therefore
   the graph of a bounded linear map `T` into `L1`.

4. **Rate separation.** The stable graph correction has size at most
   `K||T|| exp(-alpha r)||v||`; the original unstable component has size at
   least `c exp(alpha r)||v||`. Their ratio is at most
   `(K||T||/c) exp(-2 alpha r)`. This yields a uniform lower dichotomy
   estimate on each new `j2`-plane after a plane-dependent finite time. The
   definition permits the multiplicative constant to depend on the plane.

5. **Finite-time patch.** All fundamental matrices are invertible. On the
   unit sphere of the fixed finite-dimensional plane, every ratio involving
   one of the finitely many early times has a positive minimum. This extends
   the later-time estimate to all `n >= m >= 0`, equivalently the role of
   Lemma 36 in the source paper.

6. **Maximality.** Transferring the source maximal pair gives `u2 <= u2'`.
   Applying the same theorem in the reverse direction to the target maximal
   pair gives `u2' <= u2`. Thus equality holds. Degenerate splittings have a
   unique complement and are immediate.

## Comparison with the source theorem

Theorem 37 of the source assumes that the stable projection of every target
`u2`-plane has dimension at most `u1`, so that a full moving-time stable
estimate is available on that projection. The new proof bypasses that
hypothesis: only an absolute time-zero estimate on the stable projection is
needed, and finitely many stable basis-line estimates supply it regardless of
the projection's dimension.

## Bounded novelty check

On 27 August 2026, the run registry, solution index, attempt index, and
proof-gap index were searched using arXiv id `2411.06209` and the phrases
`maximal uniformity dimension`, `dependence on splitting`, and `choice of L2`.
Live web/arXiv searches used the exact conjecture language, the paper title,
the arXiv id, and the authors' names with the complement-dependence keywords.
They found the source paper and a repository mirror, but no later paper or
preprint claiming this transfer theorem or resolving Remark 39(b). This is a
bounded search, not an exhaustive novelty guarantee.

## Mechanical and visual checks

There is no numerical or symbolic computation in the proof. The packet is
compiled with `latexmk`; the final log is checked for warnings and overfull
boxes; all final pages are rendered and visually inspected. The exact source
crop is rendered from page 20 of the source PDF. The final build has four
pages and no LaTeX warnings, undefined references, or overfull/underfull box
reports. SHA-256 hashes:

- `solution_packet.pdf`: `caad83dee553653ba2a7158a341da47154a121535bb3de44cda897ff7705b38b`
- `source_paper.pdf`: `6a161dded5fb6c30c57c0ffc77e52c348fe0c36e60aebc8e6b6b6e7d21b2a464`
- `figures/open_problem_crop.png`: `8fbc7e66ea9baf9144d4d32688f6e48749664734d79faebc52f97ea4601a8664`

## Main review focus

Verify that the source convention indeed supplies the same exponent on all
refined one-dimensional stable subspaces (Definitions 4 and 15 and the
refinement theorem do), and check that the later-time estimate is uniform in
all vectors of each fixed graph plane. No unproved external lemma remains.
