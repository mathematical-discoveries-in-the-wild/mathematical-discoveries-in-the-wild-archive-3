# Unbounded rotation blocks destroy the operator-norm absorption limit

Status: candidate counterexample, likely valid, human review required.

Source: Jochen Glück, “A note on approximation of operator semigroups,”
arXiv:1511.02329, *Archiv der Mathematik* 106 (2016), 265–273.

The unconditional operator-norm extension of the source's Theorem 1.2 to
unbounded generators is false, even on a Hilbert space with an orthogonal
projection.

Let H = l2(N;C^2), let

    J = [[0,-1],[1,0]],        (Ax)_n = n J x_n,
    P(a,b) = (a,0),            Q = I-P.

With its natural weighted domain, A is an unbounded skew-adjoint generator.
The compression QAQ is zero on a dense domain and closes to the zero
generator on QH, so the predicted absorption limit is Q.

For every k>0, A-kP generates a contraction semigroup. For each fixed mode
its 2-by-2 block converges to Q, and contractivity plus finite-support density
gives

    exp(t(A-kP)) x -> Qx

strongly for every x and every t>0. Nevertheless, high-frequency blocks give,
for every fixed t>0,

    ||exp(t(A-kP))-Q|| >= 1-exp(-kt/2),

and hence the operator-norm distance has liminf at least 1. There is no
operator-norm limit as k tends to infinity.

Files:

- solution_packet.pdf — review-ready proof packet
- main.tex — packet source
- source_paper.pdf — original arXiv paper
- figures/open_problem_crop_page2.png and open_problem_crop_page3.png — the complete two-page source question
- code/verify_rotation_blocks.py — finite-block regression checks, not part of the proof
- VERIFICATION.md — exact audit and bounded novelty record

This answers the natural unconditional operator-norm extension negatively. It
does not classify additional hypotheses under which unbounded generators have
an absorption limit.
