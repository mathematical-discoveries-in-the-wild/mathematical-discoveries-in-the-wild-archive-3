# arXiv:0804.0028 - maximal tensor quotients with a nonselfadjoint factor

Status: candidate full solution, likely valid; human review pending.

Blecher--Duncan ask immediately before Lemma 2.7 whether their maximal-tensor
quotient formula remains true when the second factor is nonselfadjoint.  This
packet proves that it does: if `A` is an approximately unital ideal in an
operator algebra `B` and `D` is any approximately unital operator algebra,
then

```text
(B tensor_max D)/(A tensor_max D)  ~=  (B/A) tensor_max D
```

completely isometrically.

The key point is representation-theoretic.  Given a representation of the
left quotient, the universal property of the maximal tensor product writes it
as a product of commuting representations of `B` and `D`.  On the essential
subspace of the `D`-representation, the `A`-action vanishes; hence the
`B`-representation factors completely contractively through `B/A`.  This
produces the missing matrix-contractive inverse.

- `source_paper.pdf`: arXiv:0804.0028
- `figures/open_problem_crop.png`: direct crop of source PDF page 4
- `solution_packet.pdf`: compiled proof packet
- `verification.md`: mathematical, novelty, and visual checks

No computational verification is relevant; the proof is structural.
