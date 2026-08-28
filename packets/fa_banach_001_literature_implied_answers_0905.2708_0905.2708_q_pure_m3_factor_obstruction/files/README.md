# The q-pure-map conjecture on `M_3(C)`

**Status:** `literature_implied_answer (full n=3 subcase)`  
**Verdict:** likely valid; agent-identified implication, not an explicit claim located in the supporting papers  
**Source question:** Christopher Jankowski, *On type II_0 E_0-semigroups induced by boundary weight doubles*, arXiv:0905.2708v2, concluding paragraph on PDF page 37  
**Supporting sources:** arXiv:1005.4404 (Theorem 3.9, Corollary 3.10, Proposition 4.5) and arXiv:1807.09824 (Theorem 5.7)

## Result

Every unital q-pure map

```text
phi : M_3(C) -> M_3(C)
```

is either invertible or has rank one. This proves the complete `n=3` case of the conjecture stated in arXiv:0905.2708. The cases `n >= 4` are not addressed.

## Identification

The proof is a short but non-explicit synthesis of three ingredients. The boundary-weight-double correspondence (Lemma 4.3 of the source paper) transfers q-purity of `phi` to q-purity of a finite-dimensional, index-zero q-weight `omega`. Directly from the defining formula, `ran(omega)=ran(phi)` and the Choi-Effros limit of `omega` is

```text
L_phi = lim_{s -> infinity} s phi (I + s phi)^(-1).
```

Theorem 5.7 of arXiv:1807.09824 therefore forces `(ran(phi), A star B = L_phi(AB))` to be a factor. The `M_3` classification in arXiv:1005.4404, together with Proposition 4.5 there, leaves only a faithful rank-one limit or the identity limit. Since `phi` and `L_phi` have the same range, these alternatives give rank one or invertibility.

## Scope and novelty status

The original conjecture is for every `n`; this packet settles only `n=3`. The supporting authors do not appear to state this matrix-map corollary explicitly. A bounded search of the run indexes, exact conjecture wording, `q-pure M_3`, the three cited arXiv records, and close title/keyword variants found the published `n=2` result and the q-weight classification, but no explicit `n=3` resolution. The appropriate provenance is therefore a literature-implied answer, not a claim of wholly independent novelty.

## Files

- `solution_packet.pdf`: detailed proof and review note
- `source_paper.pdf`: arXiv:0905.2708
- `supporting_paper_1005.4404.pdf`: limit-map classification and annihilation obstruction
- `supporting_paper_1807.09824.pdf`: Choi-Effros factor theorem
- `main.tex`: packet source
- `verification.md`: verification record

## Human-review recommendation

High-priority review. Check especially the transfer from q-purity of the matrix map to q-purity of the boundary q-weight and the direct computation identifying its range and Choi-Effros limit. Once those two bridge steps are accepted, the final `M_3` classification argument is immediate.
