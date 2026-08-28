# Stable trace asymptotics conjecture of arXiv:1006.4711

Status: `literature_already_answered (full conjecture)`

Original source:

- David Applebaum, *Infinitely divisible central probability measures on
  compact Lie groups---regularity, semigroups and transition kernels*,
  arXiv:1006.4711; *Annals of Probability* 39 (2011), 2474--2496.
- Exact location: Section 6, arXiv PDF page 21 (journal page 2494).

Answering source:

- Rodrigo Banuelos and Fabrice Baudoin, *Trace asymptotics for subordinate
  semigroups*, arXiv:1308.4944 (2013).
- Exact locations: the explicit identification of Applebaum's conjecture is on
  arXiv PDF page 1; the stable specialization is on pages 2--3; the general
  regularly-varying result is the unnumbered theorem and equation (9) on page
  3, followed immediately by the compact-Lie-group on-diagonal conclusion.

Applebaum conjectures that for a compact semisimple Lie group of dimension
`d`, the central alpha-stable transition density satisfies
`k_t(e) ~ C t^(-d/alpha)` for `0 < alpha <= 2`. Banuelos--Baudoin explicitly
state that their note addresses this conjecture and that it is true.  With
`psi(lambda)=lambda^(alpha/2)`, Weyl's law gives the counting asymptotic for
`psi(-Delta)`, and the Tauberian step gives the stated heat-trace asymptotic.
On a compact Lie group, invariance identifies the normalized on-diagonal
kernel with the trace, yielding Applebaum's formula.  Their proof covers
`0 < alpha < 2`; the endpoint `alpha=2` is the classical heat-kernel case
already known and explicitly acknowledged in the source paper.  Thus no part
of the stated conjecture remains open.

The answering paper cites Applebaum as reference [1], names the pages of the
conjecture, and says its purpose is to show that the conjectured asymptotics
hold.  This is therefore an exact later-literature answer, not an inference or
a new mathematical result of this run.

Search evidence: the four run indexes were checked for arXiv:1006.4711 and the
stable/Casimir/Weyl keywords; exact-title and DOI searches were run over the
local parsed arXiv corpus; current exact-phrase and citation searches were run
on 26 August 2026; and the 16 works in OpenAlex then indexed as citing the
source were reviewed by title.  arXiv:1308.4944 was the direct explicit answer.
The later papers of Fahrenwaldt (2016) and Applebaum--Le Ngan (2017) also cite
or use the Banuelos--Baudoin result, but are not needed for the classification.

- Compact status note: `solution_packet.pdf`
- Original source PDF: `source_paper.pdf`
- Answering source PDF: `supporting_paper_1308.4944.pdf`
- Ledger:
  `runs/fa_banach_001/ledger/results/1006.4711_stable_trace_asymptotics_answered_by_1308.4944.json`
