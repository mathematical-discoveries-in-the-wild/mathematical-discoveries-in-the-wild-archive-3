# Property A localization: the complete p-phase diagram

Status: `candidate_full_solution_likely_valid`

Source: Ján Špakula and Jiawen Zhang, *Quasi-Locality and Property A*,
arXiv:1809.00532, Question 6.6.

## Full answer

For every bounded-geometry metric space and every fixed exponent
\(1<p<\infty\), all five clauses in Proposition 6.3 remain equivalent after
replacing \(\ell^2(X)\) by \(\ell^p(X)\). At \(p=1\), the three localization
clauses are automatic on every metric space and therefore cannot characterize
Property A.

The new reverse implication is

\[
  p\text{-ONL}\quad\Longrightarrow\quad \mathrm{ULA}
  \quad\Longrightarrow\quad \text{Property A},
  \qquad 1<p<\infty.
\]

If ULA fails, a finite set carries uniform local vertex expansion at one
scale. The lazy random walk on its bounded-degree proximity graph has norm one
on \(\ell^p\), while a local Cheeger inequality and uniform convexity force a
fixed norm loss on every vector of bounded support. This contradicts
\(p\)-operator norm localization. The endpoint fails because
\(\|b\|_{\mathcal B(\ell^1(X))}=\sup_x\|b\delta_x\|_1\).

## Novelty and review

Chung–Nowak, arXiv:1811.10457, explicitly state that they do not know whether
\(p\)-operator norm localization implies the Hilbert-space version and suggest
ULA as a possible route. Bounded exact-phrase, title, keyword, citation, and
run-index searches through 27 August 2026 found no later resolution. This
supports, but does not certify, novelty.

Human review should focus on the conversion of failure of ULA into the finite
proximity graphs and on the weighted lazy-walk estimate in Lemma 2 of the
packet. The remaining implication chain is direct or already in the cited
sources.

## Packet contents

- `main.tex`, `solution_packet.pdf`: full statement and proof.
- `source_paper.pdf`: arXiv:1809.00532.
- `supporting_paper_1912.00806.pdf`: Elek's ULA-to-Property-A theorem.
- `supporting_paper_1811.10457.pdf`: the later explicit p-ONL open question.
- `figures/open_problem_crop.png`: source PDF page containing Question 6.6.
- `verification.md`: proof, literature, and rendering audit.

