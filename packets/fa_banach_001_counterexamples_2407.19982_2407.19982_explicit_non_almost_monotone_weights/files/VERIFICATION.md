# Verification report

## Verdict

Likely valid candidate full answer by explicit counterexample. The
construction supplies weights on both `N` and `N^2` that fail both branches
of the source's definition of almost monotonicity.

## Mathematical checks

1. If `r = sum d_i 4^i`, the digit cost `c(r) = sum d_i 2^i` is
   subadditive. Adding two base-4 strings starts with cost `c(r)+c(s)`;
   each carry replaces cost `4*2^i` by `2^(i+1)`, decreasing it.
2. If `4^J <= r < 4^(J+1)`, then `c(r) <= 3(2^(J+1)-1)`, so
   `c(r)/r -> 0`.
3. Therefore `phi(r)=r+c(r)` is subadditive and
   `omega(n)=2^(phi(v_2(n)))` is a weight.
4. `omega(2^r)^(1/r) -> 2`, so the weight is not admissible.
5. The exact base-4 expansions give
   `c(4^j-1)=3(2^j-1)` and `c(4^j)=2^j`. Consequently
   `omega(2^(4^j-1))/omega(2^(4^j)) = 2^(2^(j+1)-4) -> infinity`, while
   the first argument divides the second. No uniform comparison constant
   exists.
6. `Omega(m,n)=omega(m)` is submultiplicative on `N^2`, nonadmissible along
   `(2^r,1)`, and has the same unbounded ratios on `(2^(4^j-1),1)` and
   `(2^(4^j),1)`.

No external theorem is needed.

## Computational sanity check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2407.19982_explicit_non_almost_monotone_weights/code/verify_digit_weight.py
```

The script checks all 1,002,001 pairs `0 <= r,s <= 1000` for digit-cost
subadditivity and checks the exact jump identity for `1 <= j <= 12`. This does
not replace the proof.

## Source and question check

- Source PDF: arXiv:2407.19982, 15 letter-sized pages.
- Exact location: concluding remark (4), source PDF page 15.
- The source crop also includes the immediately preceding multidimensional
  definition.
- The formal `N^2` definition with a comparison factor `K` appears on source
  PDF page 2.

## Definition ambiguity check

The page-15 restatement says "there is K > 0" but omits the factor `K` from
the displayed comparison. The formal page-2 definition includes `K`. The
constructed ratio is unbounded, so the example violates both versions. It is
also nonadmissible, so it cannot enter the automatic admissible branch.

## Novelty check

Bounded through 2026-08-26:

- searched the run registry, solution, attempt, and proof-gap indexes for the
  arXiv id and the core phrase;
- searched the exact phrase "not an almost monotone weight";
- searched the title, author, arXiv id, and combinations of "almost
  monotone", "weight", and "Dirichlet";
- inspected the source preprint and the official 2026 journal landing page.

Only the source work was found as a relevant exact hit. No later or independent
answer to item (4) was found. Historical novelty remains moderate because an
elementary construction can exist outside the bounded search.

## Artifact check

- `source_paper.pdf` is the official arXiv PDF downloaded on 2026-08-26.
- Page 15 is rendered at 180 dpi.
- `figures/open_problem_crop.png` keeps the full source-page width and contains
  the complete multidimensional definition and item (4).
- The final packet is rendered page-by-page and visually inspected before
  delivery.

## Human-review recommendation

Review the base-4 carry lemma and confirm the source's intended one-variable
definition. The unbounded-ratio argument is deliberately stronger than either
plausible reading of the page-15 comparison.
