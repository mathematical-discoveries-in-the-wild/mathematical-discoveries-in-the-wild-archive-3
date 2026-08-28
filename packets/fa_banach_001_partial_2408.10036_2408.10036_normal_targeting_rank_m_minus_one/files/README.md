# Rank-`m-1` normal targeting: a complete one-column criterion

Status: `partial_result` (likely valid; human review recommended).

Source question: Kyle Bierly, Stephan Ramon Garcia, and Roger A. Horn,
*The linear targeting problem*, arXiv:2408.10036. Section 10, p. 13 states
that the unrestricted normal targeting problem remains open.

## Result

The packet completely solves the subcase `rank(X)=m-1` over the complex
field. A compact SVD of `X` turns every targeting matrix into

```text
A = V [ B  d ; c*  eta ] V*.
```

The theorem gives necessary and sufficient conditions for choosing the sole
free column `(d,eta)` so that `A` is normal. The test consists of:

1. the data-consistency condition `ker(X) subset ker(Y)`;
2. a positive-semidefinite rank-at-most-one defect condition for
   `H=B*B-BB*+cc*`; and
3. one explicit vector compatibility equation involving only a phase and a
   scalar.

When `B` is normal, the compatibility condition has a closed geometric form:
the eigenvalues of `B` seen by `c` must lie on one affine line in the complex
plane.

## Sharp obstruction

For

```text
X = [I_3; 0],
Y = [diag(0,1,i); 1 1 1],
```

the source paper's positive-semidefinite defect condition holds with rank one,
but no normal `4 x 4` targeting matrix exists. The active eigenvalues
`0,1,i` are not collinear. This is the smallest obstruction in the normal
compression family.

## Files

- `solution_packet.pdf`: expert-facing statement, proof, construction,
  obstruction, verification, limitations, and novelty audit.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: source passage on p. 13.
- `code/verify_codim_one.py`: deterministic numerical checks of the block
  identities and examples.

## Scope

The general normal targeting problem for lower-rank sources remains open. The
packet does not claim an efficient closed-form elimination of the remaining
phase in the nonnormal-compression case. Prior normal-defect-one literature is
closely related, but it allows both border vectors to vary; here the lower
border is fixed by `(X,Y)`.

Human-review focus: check the SVD reduction when `n=m` and `X` has a
one-dimensional kernel, and check the conjugations in the upper-right block
normality equation.
