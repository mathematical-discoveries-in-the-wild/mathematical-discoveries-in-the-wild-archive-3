# Continuous-forcing pantograph resolvent

Status: `full_solution_likely_valid`  
Model: `GPT5.6`  
Source: Cheng-shi Liu, arXiv:1605.06734v4  
Target: Section 4, pp. 12--13, where the paper says it does not know how to
solve `y'(x)=beta y(alpha x)+q(x)` for a general smooth forcing and therefore
assumes `q` analytic in Theorem 4.1.

## Result

For a real or complex Banach space `X`, `0<alpha<1`, a bounded operator
`B in L(X)`, continuous `q:R->X`, and `a in X`, the unique global `C^1`
solution of

`y'(x)=B y(alpha x)+q(x),  y(0)=a`

is

`y(x)=E_alpha(Bx)a + sum_{n>=0} alpha^{n(n+1)/2} B^n/n!
integral_0^x (x-t)^n q(alpha^n t) dt`,

where

`E_alpha(Bx)=sum_{n>=0} alpha^{n(n-1)/2} x^n B^n/n!`.

The series converges absolutely and uniformly on every compact real interval.
Thus the source's analyticity restriction is unnecessary, and the result also
extends from scalar coefficients to bounded operators on arbitrary Banach
spaces.

## Proof mechanism

Integrate once and set `(Tf)(x)=integral_0^x f(alpha s) ds`.  Direct induction
gives

`T^n f(x)=alpha^{n(n-1)/2}/(n-1)! integral_0^x
(x-t)^{n-1} f(alpha^n t) dt`.

Consequently `T` is quasinilpotent on every compact interval, so the integral
equation is inverted by an everywhere-convergent Neumann series.  Applying the
iterated-kernel identity separately to the initial constant and to the
primitive of `q` yields the displayed formula.  Iteration of the homogeneous
integral equation proves uniqueness.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1605.06734_continuous_forcing_pantograph_resolvent/code/verify_formula.py
```

The checker passed:

- 961 exact exponent identities;
- 25 exact scalar Taylor coefficients;
- 38 exact components of a rational `2 x 2` matrix-coefficient test;
- 41 high-precision residual points on `[-2,2]`, with maximum truncated
  residual `2.3336307e-61` and zero initial-value error.

These checks guard against indexing errors; the proof in the PDF is the
mathematical justification.

## Novelty bounds

The four lightweight run indexes had no matching result.  The bounded search
used exact equation/phrase searches, `pantograph + Duhamel/variation of
constants/resolvent/continuous forcing`, the three OpenAlex citations to
arXiv:1605.06734, the source of arXiv:2303.09543 on successive approximation,
and metadata/abstracts for the classical generalized-pantograph literature.
No prior occurrence of this explicit continuous-forcing series was identified.
Because the argument is elementary, novelty confidence is moderate rather than
high; literature prior-art review is the main human-review task.

## Packet contents

- `solution_packet.pdf`: theorem, proof, source evidence, checks, and novelty
  statement;
- `source_paper.pdf`: exact arXiv:1605.06734v4 PDF;
- `figures/open_problem_crop_page12.png` and
  `figures/open_problem_crop_page13.png`: the two-page source passage;
- `code/verify_formula.py`: exact and numerical guard checks.

Human review recommendation: `send_to_human`.  Mathematical focus: confirm
the oriented-integral identities for `x<0`.  Literature focus: look for the
same explicit resolvent in older pantograph or Volterra-equation sources.
