# Verification report

Status: candidate counterexample, likely valid.

## Exact hypothesis and conclusion audit

- H=l2(N;C^2) is a complex Hilbert space.
- A=direct_sum(nJ) on D(A)={x: sum n^2||x_n||^2<infinity} is densely
  defined, closed, unbounded, and skew-adjoint; it generates the blockwise
  rotation group.
- P=direct_sum diag(1,0) is an orthogonal projection and Q=I-P.
- P and Q preserve D(A). On D(A) intersect QH, QAQ=0; this domain is dense
  in QH, so the compression closes to the zero generator and the natural
  predicted limit is Q.
- The nth block of A-kP is M_n,k=[[-k,-n],[n,0]]. Its energy derivative is
  d||v||^2/dt=-2k|v_1|^2, so all block semigroups and their direct sum are
  contractions.
- For fixed n, the exact overdamped exponential tends to diag(0,1) as k
  tends to infinity. Contractivity upgrades finite-support convergence to
  strong convergence on all of H.
- For n>k/2, the exact underdamped formula shows
  ||exp(tM_n,k)e_2|| -> exp(-kt/2) as n tends to infinity. The reverse
  triangle inequality therefore gives
  ||exp(t(A-kP))-Q|| >= 1-exp(-kt/2).
- Since the semigroups converge strongly to Q, any operator-norm limit would
  have to be Q; the lower bound proves that no norm limit exists.

## Computational regression

Command:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/1511.02329_unbounded_rotation_blocks_no_norm_absorption_limit/code/verify_rotation_blocks.py

The script checks the exact two regimes of the matrix exponential, fixed-mode
convergence, high-frequency damping, the norm lower bound, and contractivity
for multiple values of t, k, and n. These finite computations are not used as
proof.

## Bounded novelty check

Checked through 27 August 2026:

- all four cheap run indexes for arXiv:1511.02329, absorption semigroups,
  unbounded generators, projection damping, rotation blocks, and
  operator-norm convergence;
- exact-title, exact-phrase, author/id, formula, quantum-Zeno, and close-variant
  arXiv/web searches;
- OpenAlex and Semantic Scholar citation metadata for DOI
  10.1007/s00013-015-0861-3.

The searches found the source and generic later references to it, but no paper
claiming this block construction or an exact answer to its unbounded-generator
question. Novelty is plausible, not certified.

## Scope and human review

This is a complete counterexample to extending Theorem 1.2's unconditional
operator-norm assertion to arbitrary unbounded generators. It deliberately
retains strong convergence and a well-behaved compressed generator, so the
failure is purely nonuniform across high modes. The broader request to
classify sufficient conditions for unbounded generators remains open.

Human review should focus on the fixed-mode matrix limit, the passage from
finite support to strong convergence, and the high-frequency norm lower bound.
