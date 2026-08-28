# The affine group refutes the Modular Collapse Conjecture

Result type: `counterexample`

Status: candidate full negative answer, likely valid pending expert review.

Source:

- Takao Inoué, “Haar-Type Measures on Topological Quasigroups and Kunen's
  Theorem,” arXiv:2603.06174v2 (2026).
- Target: Conjecture 1 (Modular Collapse Conjecture), PDF page 16.
- Local source: `source_paper.pdf`.
- Source evidence: `figures/open_conjecture.png`.

## Claimed contribution

The conjecture is false even when the quasigroup is a connected
two-dimensional Lie group and the measure is two-sided quasi-invariant.
Take the orientation-preserving affine group

```text
G = {(a,b): a>0, b in R},
(a,b)(a',b') = (aa', b+a b').
```

Every group satisfies the identity `(N1)`.  Equip `G` with right Haar measure

```text
dnu(a,b) = da db / a.
```

For `g=(alpha,beta)`, direct changes of variables give

```text
(L_g)_*nu = alpha^(-1) nu,
(R_g)_*nu = nu.
```

Thus the paper's left modular cocycle is `j(g)=alpha^(-1)`, so, for example,
`j((2,0))=1/2`.  All hypotheses of the conjecture hold, but `j` is not
identically one.

## Scope caveat

This fully refutes Conjecture 1 as written.  It does not classify extra
hypotheses that force cocycle collapse.  Requiring the chosen measure itself
to be left invariant would force `j=1` tautologically; more substantive
rigidity assumptions remain open.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_conjecture.png`: source statement.
- `code/check_counterexample.py`: exact symbolic regression check.
- `verification_report.md`: mathematical, build, and novelty checks.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

A bounded local-index, arXiv, and web search on 27 August 2026 found the source
paper but no later response to the named conjecture.  The construction uses
standard Haar-measure facts, so the counterexample should be regarded as a new
application/observation rather than a new affine-group fact.  Novelty
confidence is moderate pending specialist review.

## Human review focus

Please check the source's push-forward convention, the two Jacobian factors,
and that the conjecture does not silently require the measure to be left Haar.
Under the displayed statement and Definition 4 of the source, the example is
literal.
