# Verification report

Status: `counterexample_likely_valid_scoped`

## Mathematical audit

For each proposed `r0>0`, set `r=min(r0/2,1/2)` and choose

```text
M > (1-r)/(r^2(1+r)).
```

For `f_M(z)=diag(z,z+Mz^2-Mz^3)` and `g=f_M`:

1. the first diagonal entry proves injectivity;
2. the `(1,1)` coordinate projection is the inverse on the image;
3. `g=f_M o id`, so `g in S(f_M)`;
4. `B_1=I_2`, `B_2=diag(0,M)`, and `B_3=diag(0,-M)`;
5. the coefficient sum is `r+Mr^2+Mr^3>1`;
6. the boundary liminf is at least one because the norm dominates `|z|`;
7. along positive real `rho -> 1`, both diagonal entries tend to one, so the
   same liminf is at most one.

Every inequality is strict or exact as claimed. No numerical approximation or
external theorem enters the proof.

## Automated sanity check

`code/verify_counterexample.py` checks the coefficient identities and the
strict failure with exact rational arithmetic for several representative
positive values of `r0`. This is a regression check, not a substitute for the
quantified algebraic proof.

## Source audit

- The exact question is visible in `figures/open_problem_crop.png` from PDF
  page 13.
- Equation (2.26) is transcribed from source lines 731--736.
- The printed-definition/operative-convention mismatch is documented in
  `SOURCE_NOTES.md` with exact source line locations.

## Novelty audit

The bounded 2026-08-27 search checked:

- `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
  `proof_gaps/index.tsv` for the arXiv id, title, and core Bohr/biholomorphic
  terms;
- exact-title and exact-question-phrase web searches;
- the arXiv abstract/source, the Cambridge publisher page, and the later
  operator-valued Bohr papers surfaced by the publisher/citation searches.

No explicit proof or counterexample to the unrestricted question was found.
The search was bounded and does not certify novelty.

## Scope and recommended review

The result answers the unrestricted question under the source's operative
curve convention. It does not answer the convex-only strengthening. Under the
printed ambient-open definition, the non-scalar family is empty instead, so a
reviewer should explicitly decide which convention the result should be
reported against.

Recommended reviewer: an expert in holomorphic mappings in Banach spaces or
operator-valued Bohr phenomena. The only substantive audit issue is the source
convention; the counterexample calculation itself is elementary.

## Render audit

`main.tex` compiled with `latexmk` in two passes. The final log contains no
warnings, undefined references, or overfull/underfull box reports. The four
pages of `solution_packet.pdf` were rendered to PNG at 150 dpi and each page
was visually inspected: text, mathematics, source crop, margins, and links are
legible, with no clipping or overlap.

```text
Pages: 4
Page size: 612 x 792 points (US Letter)
File size: 390699 bytes
SHA-256: e7efc5c98c908cd6c07f49eda69a2d44e9d3ac9345e6303a9f0cb8b0b6251189
```

The copied source PDF has SHA-256
`5fc8e03e2a13d46cf1b18d6dc88a25d1f4a51cdfb2b6e03aad482baa2fdd0ad0`.
