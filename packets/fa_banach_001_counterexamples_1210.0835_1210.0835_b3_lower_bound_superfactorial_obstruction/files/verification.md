# Verification report

Status: candidate counterexample/disproof, likely valid.

## Mathematical audit

1. For `n=2m+1` and three negative `-2` steps, the source equation
   `2q=2m+1+3` gives exactly `q=m+2` positive `+4` steps.
2. Thus every candidate sequence has `m+5` steps and `m+4` internal
   vertices.  Choosing the three negative-step locations gives at most
   `binom(m+5,3)` sequences; admissibility can only reduce this count.
3. With `j_t=-n+2r_t`, the denominator identity is exactly
   `n^2-j_t^2=4r_t(n-r_t)`.
4. The vertices following the first `m+1` positive steps are internal because
   one positive step remains.  They are distinct and all occur among the
   `m+4` factors in `h_1`.
5. If `d_p` negative steps have occurred, `r_p=2p-d_p` with
   `0<=d_p<=3`.  Admissibility handles the only small exceptional cases and
   gives the two product bounds `prod |r_p|>=m!` and
   `prod |n-r_p|>=m!`.
6. Every unselected internal factor is a product of two nonzero integers, so
   its absolute value is at least one.
7. Multiplying by the `4` from each of the `m+4` internal denominators and
   summing over the path count gives the theorem.
8. Taking `m`-th roots after multiplying by `m!` gives zero by Stirling's
   formula, contradicting every eventual lower estimate with fixed `C>0`.

No computation is used in the proof.

## Exact enumeration check

Run from the packet directory:

```text
conda run --no-capture-output -n sandbox python code/verify_b3.py --max-m 12
```

The script enumerates all choices of three negative-step locations using exact
rational arithmetic, rejects paths hitting either endpoint internally, and
checks both the signed and absolute sums against the theorem.  It checks 12
values (`m=1,...,12`).  The check is finite evidence only.

## Novelty bounds

On 27 August 2026 the run's registry, solution, attempt, and proof-gap indexes
were searched by arXiv id and the core formula.  Bounded arXiv/web searches
used the exact `B_3(2m+1)` language, `C^m/m!`, the title and authors, and the
associated two-exponential potential.  They found the source, its publication
record, and the authors' arXiv:1210.3907 follow-up, but no treatment of this
exact lower bound.  The follow-up's stated antiperiodic range excludes the
present `r=1,s=2` case.  Novelty confidence is moderate because the search was
bounded and the obstruction is elementary.

## Render audit

Compiled with `latexmk` under TeX Live 2026.  The final PDF has four
letter-size pages.  All four pages were rendered to PNG at 150 dpi and
inspected at original resolution.  The source-question crop includes the full
question, both inequalities (27)-(28), and the stated spectral implication;
all text and formulas are readable.  The final log contains no overfull or
underfull box, undefined-reference, or warning lines.  Reopening with `pypdf`
confirmed four pages, extractable text, and no encryption.
