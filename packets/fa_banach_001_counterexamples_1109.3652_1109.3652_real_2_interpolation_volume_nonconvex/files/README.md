# Counterexample packet: real 2-interpolation volume convexity fails in dimension two

Status: `candidate_counterexample_likely_valid_full_negative_answer`

Model: `GPT5.6`

Source paper: Dario Cordero-Erausquin and Bo'az Klartag, *Interpolations, convexity and geometric inequalities*, arXiv:1109.3652.

Target: Conjecture 10 on source PDF page 11 asks whether
`alpha(t) = -log integral exp(-F_t)` is convex along every real
2-interpolation whose endpoints are even, convex, and 2-homogeneous norm
squares.

Answer claimed here: no, already in dimension two, under the intended
nontrivial smooth-norm interpretation.  Take the analytic unconditional body
whose support function is

`h(theta) = 1 - (1/100) cos(4 theta)`

and prescribe a 2-homogeneous initial speed with boundary value
`a(theta) = cos(2 theta)`.  Cone coordinates give the exact second-variation
formula

`alpha''(0) = (A - 4D) / M`,

where

- `M = integral h(h+h'')`,
- `A = integral h^2(a')^2`, and
- `D = integral a^2 h(h+h'')`.

For `h = 1 + epsilon cos(4 theta)`, exact Fourier integration yields

`A - 4D = 8 pi epsilon (3 + 4 epsilon)`.

At `epsilon = -1/100` this equals `-148 pi / 625`, while both `h` and
`h+h''` stay strictly positive.  Thus the logarithmic partition function has
negative second derivative at the central time.  The reduced homogeneous
interpolation equation is an analytic PDE in noncharacteristic normal form
for the second time derivative.  Cauchy--Kowalevski therefore realizes the
datum as an actual short analytic 2-interpolation; affine time rescaling puts
its two genuine endpoints at 0 and 1.

The source initially phrases interpolation for smooth functions on all of
Euclidean space, but a globally twice differentiable exactly 2-homogeneous
function is necessarily quadratic.  Since Conjecture 10 explicitly concerns
arbitrary norm squares, its nontrivial intended class is the standard one:
smooth and strongly convex away from the origin, continuous and convex at the
origin, with the PDE holding away from the origin (hence almost everywhere).
The counterexample lies in this class.  Under a literal globally smooth
reading, only ellipsoids remain and the question is trivial.

Packet files:

- `main.tex`: full proof packet, including the exact source statement,
  geometric calculation, local-existence argument, caveat, and references.
- `solution_packet.pdf`: rendered proof packet.
- `verification.md`: adversarial mathematical and computational audit.
- `novelty_search.md`: bounded duplicate and literature search.
- `code/verify_rayleigh.py`: exact SymPy verification of every Fourier
  integral and of the negative deficit.
- `source_paper.pdf`: local copy of arXiv:1109.3652.
- `figures/open_problem_crop.png`: source crop containing Conjecture 10.

Human review focus:

- Check the global periodic patching of the local analytic
  Cauchy--Kowalevski solution.
- Confirm that the source's intended regularity is smooth off the origin for
  norm squares, as its statement and surrounding discussion indicate.
- Recheck the cone-coordinate Hessian identity, although it has also been
  reduced to an exact symbolic calculation.

Ledger record:
`runs/fa_banach_001/ledger/results/1109.3652_real_2_interpolation_volume_nonconvex.json`.
