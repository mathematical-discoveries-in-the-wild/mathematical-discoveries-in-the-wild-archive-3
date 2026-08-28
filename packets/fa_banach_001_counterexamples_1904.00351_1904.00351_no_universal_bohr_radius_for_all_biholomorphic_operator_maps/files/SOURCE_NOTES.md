# Source notes for arXiv:1904.00351

## Exact question

The final Remark (ii), source lines 905--913 and PDF page 13, asks whether

```text
sum_{k>=1} ||B_k|| r^k
    <= liminf_{|z|->1-} ||f(z)-f(0)||
```

holds for every biholomorphic `f:D->B(H)` and every `g in S(f)` at all
`r <= r0`, for some universal `r0>0`. It says the answer might be negative,
even for convex `f`.

The displayed inequality is equation (2.26) in the compiled PDF and is at
source lines 731--736.

## Printed definition versus operative convention

At source lines 314--323, the paper says that `f:D subset X -> Y` is
biholomorphic when `f(D)` is a domain in `Y` and the inverse is holomorphic.
For `D` equal to the scalar disk and `Y=B(H)` of dimension greater than one,
an ambient-open image is impossible for a biholomorphism.

The rest of the paper uses a different, curve-level convention. In particular:

- the final question varies `H` and treats the coefficient `A_1=f'(0)` as an
  invertible operator in `B(H)` (source lines 905--912);
- the downloadable arXiv TeX contains a commented-out paragraph at lines
  690--715 that calls

  ```text
  f(z) = diag(z,t(z))
  ```

  biholomorphic for an arbitrary holomorphic scalar function `t` with
  `t(0)=0` and `t'(0)=1`, precisely to note that higher Taylor coefficients
  can be arbitrarily large.

The counterexample packet follows this operative convention: holomorphic and
injective, with a holomorphic inverse on the one-dimensional image. It does
not claim to satisfy the incompatible ambient-open clause.

## Local source files

- Original PDF: `source_paper.pdf` in this packet.
- Downloaded arXiv source archive:
  `data/raw/arxiv/1904.00351/source_download`.
- Question crop: `figures/open_problem_crop.png`.
