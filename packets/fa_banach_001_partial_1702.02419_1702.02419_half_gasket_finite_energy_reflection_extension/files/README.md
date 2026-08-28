# Finite-energy extension from every level-l half gasket

Status: `candidate_partial_likely_valid`.

PDF page 6 of arXiv:1702.02419 asks how a finite-energy function on one of
the paper's domains can be extended to a finite-energy function on the whole
level-l Sierpinski gasket.  This packet completely answers the question for
the vertical half-domain family, for every `l >= 2` and for arbitrary
finite-energy functions (not only harmonic functions).

Reflection across the vertical symmetry axis gives a linear right inverse to
restriction.  At every graph level, non-fixed edges occur in reflected pairs,
while a setwise-fixed edge has its endpoints exchanged and therefore has zero
energy for the even reflection.  Consequently the extension satisfies the
exact identity

```text
E_SG_l(Eu) = 2 E_half(u).
```

The arbitrary upper- and lower-domain cases and the higher Sobolev spaces
remain open.  Novelty is plausible but deliberately rated provisional because
the reflection argument is elementary and may be implicit or folklore.

Build and check with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
python code/verify_reflection_energy.py
```

The human-review artifact is `solution_packet.pdf`.
