# Counterexample packet: no universal Bohr radius for arbitrary operator-valued biholomorphic curves

Status: `counterexample_likely_valid_scoped`

Source: Bappaditya Bhowmik and Nilanjan Das, *Bohr phenomenon for operator
valued functions*, arXiv:1904.00351, final Remark (ii), PDF page 13.

## Result

Under the operative convention used by the source paper---an injective
holomorphic operator-valued map with a holomorphic inverse on its image---the
answer to the unrestricted question is negative, already in
`B(C^2)`. For any proposed `r0 > 0`, take

```text
r = min(r0/2, 1/2),
M > (1-r)/(r^2(1+r)),
f_M(z) = diag(z, z + M z^2 - M z^3),
g = f_M.
```

The first diagonal coordinate makes `f_M` injective and supplies its inverse
on the image. Moreover `g` is subordinate to `f_M` through the identity map.
Its coefficient sum is

```text
r + M r^2 + M r^3 > 1,
```

whereas

```text
liminf_{|z| -> 1-} ||f_M(z)-f_M(0)|| = 1.
```

Thus the displayed Bohr inequality fails at a radius `r <= r0`, for every
positive `r0`.

## Important source-convention caveat

The paper's printed definition also says that `f(D)` must be a domain in the
ambient codomain. Read literally with “domain” meaning ambient open set, this
excludes every map from the one-dimensional disk into `B(H)` when
`dim B(H) > 1`; the operator-valued part of the question is then empty. The
paper nevertheless treats `f'(0)` as an invertible member of `B(H)`, and its
downloadable arXiv TeX explicitly labels `diag(z,t(z))` biholomorphic for
arbitrary holomorphic `t`. The packet therefore answers the intended/operative
curve convention and states the literal-reading defect separately.

The example is not convex. It settles the unrestricted question but does not
settle the authors' stronger suggestion that failure might occur even for a
convex biholomorphic map.

## Files

- `main.tex` and `solution_packet.pdf`: self-contained proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source PDF page 13, final Remark (ii).
- `SOURCE_NOTES.md`: exact source locations and the convention mismatch.
- `code/verify_counterexample.py`: exact rational sanity checks.
- `VERIFICATION.md`: proof, source, novelty, and render audit.

## Verification

Run the exact sanity checker with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1904.00351_no_universal_bohr_radius_for_all_biholomorphic_operator_maps/code/verify_counterexample.py
```

Human review should focus on whether the paper's intended notion of
“biholomorphic” is accepted as the operative one. Once that convention is
fixed, the counterexample calculation is elementary and exact.

## Novelty status

A bounded search on 2026-08-27 covered the run's four lightweight indexes,
the exact arXiv id and title, exact phrases from the final question, the
publisher page and citation trail, and later operator-valued Bohr papers found
by those searches. No explicit answer to this unrestricted question was
found. This supports, but does not certify, novelty.

Ledger:
`runs/fa_banach_001/ledger/results/1904.00351_no_universal_bohr_radius_for_all_biholomorphic_operator_maps.json`
