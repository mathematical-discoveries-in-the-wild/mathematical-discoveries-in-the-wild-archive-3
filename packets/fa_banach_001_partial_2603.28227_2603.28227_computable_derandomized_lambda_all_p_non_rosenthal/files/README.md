# A computable derandomization of Neuwirth's thin-set construction

status: `substantial_partial_result (full effective derandomization; natural closed-form question remains)`

model: GPT5.6

source: Stefan Neuwirth, *Two random constructions inside lacunary sets*,
Annales de l'Institut Fourier 49 (1999), 1853–1867; arXiv:2603.28227.

packet: `runs/fa_banach_001/solutions/partial/2603.28227_computable_derandomized_lambda_all_p_non_rosenthal/`

ledger: `runs/fa_banach_001/ledger/results/2603.28227_computable_derandomized_lambda_all_p_non_rosenthal.json`

## Result

There is a parameter-free computable set `E` of positive integers which is
`Lambda(p)` for every finite `p`, is equidistributed in Weyl's sense, and
therefore is not a Rosenthal set.

The construction is deterministic. In the factorial block
`(2^((k-1)!), 2^(k!)]`, it chooses the lexicographically first subset passing
two finite tests:

1. additive independence up to a computably increasing order `h_k`; and
2. a centered exponential-sum discrepancy bound at every prefix and every
   point of a finite root-of-unity grid.

Neuwirth's counting estimate and Bernstein inequality show that a random
subset passes both tests with positive probability, so the finite search
always terminates. Littlewood–Paley block union then gives all `Lambda(p)`
properties. The discrepancy test, including all partial block prefixes,
gives equidistribution after Abel summation.

## Scope

This gives the explicit deterministic procedure that the source paper says
its random construction did not provide. It is classified as a substantial
partial result rather than a full solution because the source asks for a
“natural” set, an informal requirement not implied by computability, and the
lexicographic exhaustive search is not a closed formula or efficient
algorithm.

## Verification and novelty bounds

- The proof checks positive-probability existence, exact decidability of each
  finite search, `h_k -> infinity`, all within-block prefixes, and the final
  Rosenthal implication.
- The source PDF and exact TeX are stored locally; the crop identifies the
  question on source PDF page 3.
- A bounded search on 27 August 2026 covered the run indexes and arXiv/web
  queries for explicit, computable, deterministic, equidistributed,
  `Lambda(p)`-for-all-`p`, and non-Rosenthal constructions. It found
  Neuwirth's random construction and later random thin-set constructions by
  Li–Queffélec–Rodríguez-Piazza, but no matching computable derandomization.
  This is not an exhaustive citation-graph review, so novelty confidence is
  medium.

## Files

- `main.tex`: theorem, construction, complete proof, and review notes.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2603.28227 / published 1999 source.
- `figures/open_problem_crop.png`: source question and surrounding criterion.
- `source_tex/source_2603.28227.tex`: exact arXiv TeX used for verification.
