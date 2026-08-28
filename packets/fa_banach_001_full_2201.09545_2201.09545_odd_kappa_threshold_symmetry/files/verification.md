# Verification audit

## Mathematical checks

1. The source defines
   `g_{j kappa}(x)=sum_i (1-x_i^2) U_{j kappa-1}(x_i)`.
2. The standard Chebyshev parity identity is
   `U_n(-t)=(-1)^n U_n(t)`.
3. Therefore simultaneous negation gives
   `g_{j kappa}(-x)=(-1)^(j kappa-1) g_{j kappa}(x)`.
4. For each fixed `j`, this scalar is independent of the witness index `q`,
   so multiplying the source's defining witness relation by it preserves the
   same weights `omega_q <= 0`.
5. Negation maps the constant-energy surface `S_E` onto `S_{-E}`.
6. The `m=0` definition is preserved because zero remains zero.

No analytic convergence, spectral approximation, or numerical hypothesis is
used.

## Automated diagnostic

`code/verify_parity.py` constructs Chebyshev polynomials of the second kind by
their recurrence and symbolically verifies both the scalar parity identity
and its coordinate-sum version for a finite grid of dimensions, `kappa`, and
`j`.  This is a transcription check only; the proof is the parity calculation
in `main.tex`.

## Human review recommendation

Confirm that the source's definition imposes its linear relation separately
for every positive integer `j`, rather than requiring a sign independent of
`j`.  Once this is checked, the odd-`kappa` case follows immediately.

## Render audit

The final two-page PDF compiled without LaTeX warnings.  Both rendered pages
were inspected at full resolution; the source crop, equations, section
transitions, and bibliography are readable and free of clipping or overlap.
