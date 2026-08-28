# Verification report

status: likely valid partial result

## Proof-critical checks

1. The compiled source question is on page 4 of arXiv:1701.00766. The other
   extracted “open problem” is after `\\end{document}` and was excluded.
2. The free pluriharmonic Poisson kernel is explicitly stated in the source to
   be a positive free `k`-pluriharmonic function. Therefore Harnack domination
   with constant `c` immediately implies Poisson domination with the same
   constant.
3. The one-nonscalar-row representation lemma is the previously verified
   result in packet `1511.08852_one_nonscalar_row_poisson_representation`; its
   proof is reproduced in the new packet.
4. In the direct system over `N^s`, all connecting maps are isometries and the
   extended scalar isometries are surjective because
   `U_i tilde J_(p+e_i) = J_p`.
5. The nonscalar row extends coordinatewise, remains a row isometry, and
   commutes with the scalar unitaries. Fuglede gives commutation with their
   adjoints, exactly the missing double-commutation relations.
6. The compressed representation of `C*(R)` is completely positive and has
   the original moment coefficients. The epsilon regularization covers
   singular `F(0)` with a uniformly bounded point-ultraweak limit.
7. Applying `mu tensor id` to the two Poisson-kernel inequalities preserves
   order and leaves `c` unchanged. Hence the admissible constant sets, not
   merely their infima, coincide.

## Literature and novelty check

A bounded web search on 2026-08-26 used the exact source sentence, title,
arXiv id, author, and combinations of “Harnack”, “Poisson”, “regular
polyball”, and “one nonscalar row”. Results included arXiv:1701.00766, the
published JMAA paper, later citations/applications, and a recent survey, but no
later resolution or this intermediate dimension theorem. Novelty is therefore
“apparently new within the bounded search”, not an exhaustive claim.

## Recommended human focus

Check the direct-limit convention in Lemma 2 and the tensor-factor orientation
in `(mu tensor id)[P(R,X)] = F(X)`. Once that identity is accepted, the metric
proof is a direct order-preservation argument.

## Packet QA

- The source PDF is copied as `source_paper.pdf`; the decisive supporting
  arXiv:1511.08852 PDF is copied as `supporting_paper_1511.08852.pdf`.
- `figures/open_problem_crop.png` is a real render of source page 4 and shows
  the complete open-question paragraph at full readable page width.
- LaTeX build and complete-page visual inspection are recorded after the final
  render.
- `latexmk` completed the final build in three passes. The final log contains
  no undefined-reference, overfull-box, underfull-box, LaTeX, or package
  warnings.
- All four final pages were rendered at 150 dpi and visually inspected. Text,
  displayed mathematics, the source-page evidence, and references are legible;
  no clipping, overlap, or missing glyphs was found.
- Final PDF SHA-256:
  `0d1f4674008d4b089f486c9e7d0aef47585f38287e89b057fa7ca3ce67bbc24f`.
