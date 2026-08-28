# Complete low-exponent anisotropic Grothendieck classification

Status: `partial_result_likely_valid`

Source: Nacib Albuquerque, Gustavo Araujo, Lisiane Rezende, and Joedson
Santos, *A summability principle and applications*, arXiv:1904.04549v2
(2025), PDF page 9.

## Result

Let `H` be Hilbert, let `p=(p1,...,pm)` belong to `[1,2]^m`, and let
`q=(q1,...,qm)` have finite coordinates at least one. Then

```text
Pi_ms_(q;p)(ell_1,...,ell_1;H) = L(ell_1,...,ell_1;H)
```

if and only if `q_k >= p_k` for every coordinate `k`.

This is a complete classification throughout the full low-input-exponent
cube. The source asks for the unrestricted anisotropic classification and
provides several sufficient families, but does not state this iff theorem.

The upgraded packet also proves the ordered high-exponent obstruction

```text
1/q_k <= 1/p_l + max(1/p_k - 1/2, 0)    for every k < l.
```

It follows from normalized Hadamard rows in coordinate `k` and the unit
basis in coordinate `l`. In particular, coordinatewise conditions do not
classify the unrestricted range.

## Proof mechanism

1. At every vertex `p_k in {1,2}`, mixed Minkowski reorders all exponent-1
   coordinates outside all exponent-2 coordinates.
2. The inner exponent-2 block is controlled by the multilinear `(2;2)`
   Grothendieck theorem into a Hilbert space.
3. The resulting target is Hilbert, so the outer exponent-1 block is
   controlled by the `(1;1)` theorem.
4. Coordinatewise complex interpolation of weak sequence spaces over
   `ell_1` and vector-valued mixed sequence spaces fills `[1,2]^m`.
5. Mixed-norm monotonicity gives every `q_k >= p_k`; rank-one maps prove
   these inequalities are necessary.

## Scope

The result does not classify all tuples having some `p_k>2`. Freezing other
variables forces only `q_k>=p_k`; the new Hadamard proposition supplies
additional ordered cross-coordinate restrictions. The packet does not claim
that these necessary conditions are sufficient.

## Review files

- `solution_packet.pdf`: theorem and proof.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source PDF page 9.
- `verification.md`: adversarial proof audit.
- `code/verify_mixed_norm_reductions.py`: numerical mixed-norm regression
  checks.

The local indexes and bounded arXiv/web searches were checked on 26 August
2026 using the source id/title and anisotropic Grothendieck/multiple-summing
keywords. No prior statement of this complete low-exponent classification
was found. Human review recommendation: **send to human**.
