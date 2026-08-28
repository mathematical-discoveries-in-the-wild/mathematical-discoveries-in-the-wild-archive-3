# arXiv:2105.04635 — SOT-star density of contractions with compact-free commutant

This packet proves a substantial partial answer to Question 6.4 of Grivaux
and Matheron.  For every complex `ell_p`, `1<p<infinity`, the contractions
which commute with no nonzero compact operator are dense for the Strong-star
Operator Topology.

The construction attaches a unilateral-shift tail to an arbitrary strict
finite compression.  Its adjoint has a total family of one-dimensional
eigenspaces over the unit disk.  A compact operator in the commutant would
act on that family through a bounded holomorphic scalar function.  Normalized
eigenvectors become weakly null at every boundary point, so compactness forces
all radial boundary values of the scalar function to vanish; hence the
function, and then the compact operator, is zero.

This does **not** yet prove the source's word `typical`: density alone does not
imply comeagerness.  The Hilbert-space proof obtains a dense class on which
every commutant element has norm equal to essential norm, using von Neumann's
inequality.  No corresponding estimate is established here for arbitrary
`ell_p` contractions when `p!=2`.  The stronger Lomonosov-hypothesis clause
also remains open.

- `source_paper.pdf`: arXiv:2105.04635
- `figures/open_problem_crop.png`: direct crop of PDF page 18, Question 6.4
- `solution_packet.pdf`: compiled proof packet
- `verification.md`: mathematical, novelty, source-integrity, and visual checks

Status: candidate substantial partial result, likely valid, pending human
expert review.
