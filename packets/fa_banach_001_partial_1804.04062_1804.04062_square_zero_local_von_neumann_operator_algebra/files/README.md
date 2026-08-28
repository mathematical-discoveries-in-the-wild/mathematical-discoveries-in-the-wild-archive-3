# Square-zero local von Neumann algebras are operator algebras

Status: `candidate_partial_likely_valid`.

The open question on PDF page 4 of arXiv:1804.04062 asks whether every
normalized unital Banach algebra satisfying von Neumann's inequality is
isometrically an operator algebra.  This packet proves an affirmative answer
for every local square-zero extension

```text
A = C 1 + X,   X^2 = 0,
```

with no dimension or reflexivity assumption on the closed ideal `X`.
Disk automorphisms force the exact unit ball

```text
|lambda|^2 + ||x|| <= 1,
```

and this is exactly the contraction ball of an explicit upper-triangular
Hilbert-space representation.

Build and verify with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
python code/verify_block_contraction.py
```

The review artifact is `solution_packet.pdf`.  The general source question
remains open.
