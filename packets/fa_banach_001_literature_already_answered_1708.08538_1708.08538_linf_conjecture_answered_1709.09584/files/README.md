# Complex `ell_infinity(Gamma)` and `C(K)` have the Mazur--Ulam property

This is a literature-resolution packet for the conjecture on PDF page 15 of
arXiv:1708.08538.  Its two clauses are settled as follows:

- arXiv:1709.09584 explicitly cites the source conjecture and proves the
  `ell_infinity(Gamma)` clause in Theorem 1.1;
- Theorem 1 of arXiv:1804.10674 proves the Mazur--Ulam property for every
  unital complex C*-algebra, and therefore implies both clauses because
  `ell_infinity(Gamma)` and `C(K)` are unital commutative C*-algebras.

The supporting PDFs are retained in this directory for audit.  Build the
compact status report with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The reviewed artifact is `solution_packet.pdf`.
