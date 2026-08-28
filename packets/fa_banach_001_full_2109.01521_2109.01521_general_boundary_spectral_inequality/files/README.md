# General-boundary spectral inequality for the bi-Laplacian

Status: `candidate_full_solution_likely_valid`

Model: GPT5.6

## Source question

J. Le Rousseau and E. Wend-Benedo Zongo, *Stabilization of the damped
plate equation under general boundary conditions*, arXiv:2109.01521v2,
Section 1.6.2, page 8.

For a nonnegative self-adjoint realization `P` of the bi-Laplacian under
general boundary operators satisfying the Lopatinskii-Shapiro condition, the
paper asks whether every finite spectral sum obeys

```text
||u||_{L2(Omega)} <= C exp(C mu^(1/4)) ||u||_{L2(omega)}.
```

## Result

The answer is affirmative under exactly the source hypotheses. The missing
observation is that self-adjoint nonnegativity automatically supplies the
parameter Lopatinskii-Shapiro condition for the augmented operator
`D_s^4 + Delta^2`. Failure at a nonzero parameter would yield a decaying
negative-energy frozen boundary mode. A localized boundary-layer construction,
followed by a lower-order trace correction, would then give exact-domain
quasimodes with negative Rayleigh quotient, contradicting nonnegativity.

Once this automatic parameter condition is established, Theorem 1.3 of
E. Wend-Benedo Zongo and L. Robbiano, *Null-controllability for a fourth order
parabolic equation under general boundary conditions*, arXiv:2309.02181v1,
applies and gives the claimed exponent `mu^(1/4)`.

## Packet contents

- `solution_packet.pdf`: theorem, proof, source matching, and review notes.
- `source_paper.pdf`: arXiv:2109.01521v2.
- `supporting_paper_2309.02181.pdf`: arXiv:2309.02181v1.
- `figures/open_problem_crop.png`: full-width rendering of source page 8.
- `main.tex`: packet source; temporary build files are kept under `tmp/`.

## Review focus

The main point for expert verification is Lemma 1 in the packet: the standard
semiclassical trace correction for a boundary layer whose principal boundary
traces vanish, including the pure normal parameter ray. The scaling is
recorded explicitly and linked to the Agranovich-Vishik parameter boundary
calculus. A reviewer should also
confirm that the principal parameter convention in Theorem 1.3 of
arXiv:2309.02181 is the same `P + sigma^4` negative-resolvent convention used
in the boundary-layer contradiction.

The other two open directions in Section 1.6 of the source paper (boundary
damping and a boundary quantitative unique-continuation interpolation
inequality) are not claimed.
