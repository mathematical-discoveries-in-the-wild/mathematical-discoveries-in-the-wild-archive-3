# Bounded novelty and duplicate search

Search date: 2026-08-26

Status: no prior proof or counterexample located in the bounded search;
novelty remains candidate, not certified.

## Local run indexes

The run's registry, solution, attempt, and proof-gap indexes were searched for

- `1109.3652`,
- the exact paper title,
- `Conjecture 10`,
- `real 2-interpolation`,
- `Rochberg Semmes interpolation`,
- `2-homogeneous Brascamp Lieb`, and
- combinations of `convexity`, `alpha`, `norm square`, and `counterexample`.

No existing packet or attempt for this target was found before reservation.
The other extraction signal in the source concerned a question that is
immediately answered in the same paper and was discarded as a false positive.

## Source-paper audit

The whole real-interpolation section around Conjecture 10 was inspected.
Fact 11 immediately after the conjecture establishes only a special midpoint
inequality when the endpoints are Legendre dual.  It neither proves nor
disproves Conjecture 10.  The source explicitly says the general answer may be
negative but supplies no homogeneous counterexample.

## External bounded search

Web and arXiv-facing searches used the exact arXiv id and title, author names,
the conjecture label, and close query variants including

- `real 2-interpolation convexity alpha`,
- `Rochberg Semmes 2-interpolation convex body`,
- `2-homogeneous strengthened Brascamp Lieb counterexample`,
- `centro-affine Poincare constant 2n`, and
- `Cordero-Erausquin Klartag Conjecture 10`.

The search found the original paper and later work on related
centro-affine/Poincare inequalities, but no paper stating a proof or
counterexample to this exact conjecture.  In particular, Hu--Ivaki,
arXiv:2607.20223, proves a centro-affine Poincare inequality with constant
`n` for unconditional bodies.  Conjecture 10 would require the stronger
constant `2n`; the explicit planar computation in this packet shows that the
stronger constant fails.

## Bounds and confidence

This was not a comprehensive MathSciNet, zbMATH, or citation-network review.
Terminology varies between real interpolation, Rochberg--Semmes geodesics,
centro-affine spectral inequalities, and homogeneous Brascamp--Lieb
inequalities.  An independently known but differently phrased counterexample
could therefore have been missed.

Current confidence:

- duplicate confidence: high,
- proof confidence: high pending human review of analytic local existence,
- novelty confidence: moderate.
