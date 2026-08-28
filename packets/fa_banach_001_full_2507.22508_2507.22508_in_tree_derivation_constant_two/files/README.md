# In-tree derivations: a universal constant two

Status: candidate full solution, likely valid, pending human review.

This packet answers Conjecture 6.27 of Huang--Ma, arXiv:2507.22508.  For every
finite in-tree $G$ and every derivation $\delta$ on the tensor algebra
$\mathcal A_G$, it produces $S\in\mathcal A_G$ such that

```text
delta = delta_S,       ||S|| <= 2 ||delta||.
```

The proof has two independent norm estimates.  Diagonal sign averaging shows
that the positive-length path part of an arbitrary implementer has norm at
most $\|\delta\|$.  A single path from each vertex to the range root shows
that the vertex-diagonal part, modulo the root scalar, also has norm at most
$\|\delta\|$.

Files:

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: Conjecture 6.27 on source PDF page 33.
- `code/verify_tree_averaging.py`: finite matrix-model diagnostic.
- `verification.md`: proof and render audit.
- `novelty.md`: bounded literature-search record.

The result establishes the conjectured dimension-free bound but does not
determine the optimal universal constant.
