# A cubic with no critical element over `C(S^1)`

Status: candidate full counterexample, likely valid, human review required.

Source: K. Mahesh Krishna, “C*-algebraic Smale Mean Value Conjecture and
Dubinin-Sugawa Dual Mean Value Conjecture,” arXiv:2206.08154 (2022).

The source's C*-algebraic Smale and Dubinin-Sugawa conjectures are false in
degree 3. Let `A=C(S^1)`, let `u(zeta)=zeta`, put

```text
rho = exp(i*pi/3),   epsilon = 1/4,   c = rho + epsilon*u,
P(x) = x(x-1)(x-c).
```

At the source point `z=0`, `P'(0)=c` is invertible, so `z` is not critical.
Nevertheless, `P` has no critical element anywhere in `A`. Indeed, a critical
element `w` would make `h=3w-(1+c)` a continuous square root of

```text
q = c^2-c+1 = epsilon*u*(i*sqrt(3)+epsilon*u).
```

The loop `q` never vanishes and has winding number 1. A square has even
winding number, a contradiction. Thus the existential conclusion common to
Conjectures 2.1, 2.2, 3.1, and 3.2 already fails before any proposed norm
inequality can be evaluated.

Files:

- `solution_packet.pdf` — review-ready proof packet
- `main.tex` — packet source
- `source_paper.pdf` — original arXiv paper
- `figures/open_problem_crop.png` — source-page evidence containing both conjectures
- `code/verify_construction.py` — numerical/symbolic sanity checks, not part of the proof
- `VERIFICATION.md` — verifier checklist and bounded novelty record

Human review should focus on the derivative identity and the winding-number
obstruction. The result concerns the proposed C*-algebraic extensions, not the
classical scalar Smale or Dubinin-Sugawa conjectures.
