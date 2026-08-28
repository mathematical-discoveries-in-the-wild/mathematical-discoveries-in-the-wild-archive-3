# Verification report

Status: candidate full solution, likely valid.

## Mathematical audit

1. **Singular support.** A trace-class operator on an arbitrary Hilbert space
   has at most countably many nonzero singular values.  Its right singular
   vectors therefore extend to an orthonormal basis indexed by an arbitrary
   set `J`.
2. **Coordinate weight.** For a selected `k in J`, the weight uses
   `sqrt(s_n(B))` on the singular support and, if needed, the value `1` at
   `k`.  Hence it lies in `ell_2(J)`, is nonzero at `k`, and gives the exact
   Hilbert--Schmidt factorization `B=B_1 B_2^(k)`.
3. **Kernel lemma.** Lemmas 5.2 and 5.4 of the source are stated for arbitrary
   Hilbert spaces and arbitrary square-summable weights.  They imply that both
   completely positive summands kill `vec(B_1)` under the selected weighted
   Choi operator.
4. **Coefficient identity.** Expanding the matrix coefficient at
   `g_k tensor g_j` gives exactly
   `lambda_k(<g_j,K g_k>tr(B)+delta_jk tr(BK*))=0`.  No division by a weight at
   any other coordinate occurs.
5. **Scalar conclusion.** Repeating step 4 for every `k` makes every basis
   column of `K` equal to the same scalar multiple of that basis vector.  The
   zero weighted trace forces the scalar to be purely imaginary.
6. **Uncountable Kraus family.** The source's arbitrary-index Kraus theorem
   and Lemma 4.7 give centering coefficients in `ell_2(J)`.  Cauchy--Schwarz
   makes the finite-subset net of cross operators Cauchy in operator norm.
   The centered Kraus family has a uniformly bounded square sum.
7. **Map identity.** Expanding the centered finite Kraus sums and passing to
   their trace-norm limits yields the displayed generator identity.  The final
   imaginary scalar shift enforces the gauge condition.
8. **Injectivity.** The strengthened proposition leaves only an imaginary
   scalar difference, and the gauge condition eliminates it because
   `Re(tr(B))` is nonzero.

No computation is used as proof.  The argument was checked in the scalar and
finite-dimensional special cases for sign consistency, but those checks are
not evidence for the infinite-dimensional theorem.

## Novelty bounds

On 27 August 2026 the run's registry, solution, attempt, and proof-gap indexes
were searched by arXiv id and the terms `nonseparable`, `weighted Choi`,
`CP_B`, and `unique decomposition`.  Bounded arXiv/web searches used the exact
question, `Proposition 5.6`, the paper title, the author, and close
nonseparable variants.  They returned the source paper, its published record,
and the finite-dimensional predecessor, but no later solution or equivalent
extension.  Novelty confidence is moderate rather than definitive because the
search was bounded and the central coordinatewise trick is elementary.

## Render audit

Compiled with `latexmk` under TeX Live 2026.  The final PDF has five letter-size
pages.  All five pages were rendered to PNG at 150 dpi and inspected at
original resolution.  The source-question crop is complete and readable;
displayed equations, theorem statements, references, page numbers, and section
transitions are unclipped.  The final log contains no overfull/underfull box,
undefined-reference, or warning lines.  Reopening with `pypdf` confirmed five
pages, extractable text, and no encryption.
