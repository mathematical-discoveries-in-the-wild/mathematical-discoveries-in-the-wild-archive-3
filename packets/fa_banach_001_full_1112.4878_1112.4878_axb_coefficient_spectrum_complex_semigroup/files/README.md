# Full candidate: spectrum of the positive `ax+b` coefficient algebra

Status: `full_solution_likely_valid` (awaiting human review).

Spronk--Stokke conjectured in the final example of arXiv:1112.4878 that the
Gelfand spectrum of the Fourier--Stieltjes-norm coefficient algebra generated
by the positive irreducible representation of the real affine group is exactly

```text
{(a,z): a>0, Im z>=0},  (a,z)(a',z')=(aa',az'+z).
```

This packet proves that conjecture.  In sum--ratio coordinates, the tensor
coproduct is radial amplification.  Angular commutation forces positive
group-like operators to be the exponential multipliers `M_exp(-cs)`.  A
bounded imaginary-power argument forces unitary group-like operators to be
the actual representation operators `pi_+(a,b)`.  Polar decomposition then
classifies every character as

```text
pi_+(a,b) M_exp(-cs) = tilde-pi_+(a,b+iac).
```

The proof also identifies the weak-operator topology with the usual topology
of the complexified semigroup, so this is a topological-semigroup
classification and proves spectral naturality of `pi_+`.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:1112.4878.
- `figures/open_problem_crop.png`: source PDF page 37, including the operator
  equation and the exact conjecture.
- `verification_report.md`: adversarial proof audit.

Scope: this settles the paper's concrete `ax+b` conjecture and one substantial
case of its general Conjecture 3.9(ii).  It does not settle that general
quasi-containment conjecture.

Primary verifier focus: the interval-block proof of positive angular rigidity,
and the bounded imaginary-power step in the unitary classification.
