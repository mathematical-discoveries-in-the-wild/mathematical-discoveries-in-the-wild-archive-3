# Canonical-inner-product Toeplitz transfer for arXiv:1307.4829

Status: `candidate_full_solution_likely_valid`

Source: Hong Rae Cho, Joshua Isralowitz, and Jae-Cheon Joo, *Toeplitz operators on Fock-Sobolev type spaces*, arXiv:1307.4829, Section 5, page 31.

## Result

For the Toeplitz operator defined using the reproducing kernel of the natural/canonical inner product on `F^2_alpha`, the packet proves:

- boundedness on every `F^p_alpha`, `1 <= p < infinity`, exactly when the fixed-radius ball masses of the positive symbol are uniformly bounded;
- compactness on every such `F^p_alpha` exactly when those ball masses vanish at infinity;
- membership in every Schatten class `S_t`, `0 < t < infinity`, on the canonical Hilbert space exactly when the lattice ball-mass sequence belongs to `ell_t`;
- the expected bounded and vanishing canonical Berezin-transform criteria;
- the canonical Berezin `L^t` equivalence for every `0 < t < infinity`.

The mechanism is a direct answer to the source's requested operator-theoretic route. The positive diagonal operator changing the modified inner product to the canonical one is identity plus compact on every `F^p_alpha`, hence boundedly invertible. After applying it, the canonical Toeplitz operator equals a source Toeplitz operator with asymptotically unit symbol multiplier, modulo compactly supported super-smoothing pieces and finite Taylor blocks.

The final quasi-Banach clause is closed by an exact canonical-kernel localization lemma. The canonical weight is replaced only on a fixed ball by a smooth uniformly strictly plurisubharmonic weight. The generalized-Fock kernel then has exponential off-diagonal decay. The exact and smoothed inner products differ by `A=I+T_h`, with `h` compactly supported, so `K^c_z=A^{-1}L_z`. Support localization gives exponential decay of the correction in one variable, and self-adjointness gives it in the other. Consequently the exact canonical normalized kernel has a uniform exponential tail. For `0<t<1`, subadditivity turns the lattice `ell_t` condition into canonical Berezin `L^t` integrability.

This is therefore a candidate full solution of the Section 5 question: every clause of source Theorems A-C is recovered for the natural/canonical inner product.

## Verification and novelty

- The source open-problem crop is a real render of page 31 of the official arXiv PDF.
- The proof is symbolic and contains no numerical dependency.
- The origin singularity is isolated behind the high Taylor projection.
- The local form is finite-rank approximable at super-polynomial speed, so it lies in all Schatten classes.
- The radial smoothing is identical to the canonical weight off a fixed ball and has complex Hessian uniformly comparable with the Euclidean Kahler form.
- The decisive generalized-Fock kernel estimates are recorded in Isralowitz-Virtanen-Wolf, arXiv:1402.2567, Lemmas 2.1-2.2; its official PDF is included in the packet.
- Exact-id/title and core-keyword searches were run against the four lightweight run indexes and bounded arXiv/web scholarly searches on 2026-08-27.
- No matching canonical-inner-product transfer was found. A 2023 paper on Toeplitz operators between Fock-Sobolev-type spaces still uses the modified inner product and repeats the canonical-kernel difficulty.

Human review should first audit the compact local-form lemma, the alpha-positive block decomposition in the transfer identity, and the compactly supported smoothing argument that transfers exponential kernel decay back to the exact canonical inner product.

Ledger: `runs/fa_banach_001/ledger/results/1307.4829_canonical_toeplitz_inner_product_transfer.json`
