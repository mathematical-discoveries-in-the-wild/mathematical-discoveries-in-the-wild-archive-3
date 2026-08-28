# Full affirmative answer to the Grushin-plane filling question

Status: `candidate_full_likely_valid_grushin_extension`.

Source: Noel DeJarnette, Piotr Hajlasz, Anton Lukyanenko, and Jeremy T.
Tyson, *On the lack of density of Lipschitz mappings in Sobolev spaces with
Heisenberg target*, arXiv:1109.4641v3, Question 8.7 on PDF page 34.

## Result

Let `G` be the first Grushin plane and `Y={(0,y)}` its singular axis. If
`phi:S^1 -> G` is Lipschitz and no nondegenerate segment of `Y` is contained
in a bounded component of `R^2 \ phi(S^1)`, then `phi` has a Lipschitz
extension to the disk. This gives a full affirmative answer to Question 8.7.

For a unit circle carrying its Euclidean chord metric, an `L`-Lipschitz loop
admits a `(pi/2)L`-Lipschitz filling.

## Mechanism

The image of the loop is a finite-length Peano continuum. Whyburn's cyclic
element theory decomposes it into cyclic blocks connected in a tree-like way
at cut points. Every cyclic block is contained in one closed Grushin
half-plane: otherwise it contains a Jordan curve crossing the singular axis,
and that curve forces the full image to enclose an axis segment.

Each closed Grushin half-plane is CAT(0). Replace every cyclic block by a
fresh copy of the half-plane containing it and keep the intervening dendritic
pieces as real trees. The result is a tree gluing of CAT(0) spaces along
points, hence its completion is CAT(0). The original loop lifts to this
unfolding with no increase of length on any subarc, and the unfolding has a
1-Lipschitz coordinate projection back to `G`. Lang--Schroeder extends the
lifted loop in the CAT(0) target; projecting gives the required filling.

## Review focus

The packet isolates the two nonstandard ingredients as explicit lemmas.
Reviewers should check:

1. the monotone CAT(0) limit proving that each closed Grushin half-plane is
   CAT(0);
2. the finite-length cyclic-element unfolding lemma, especially its
   countable completion and path-length estimate; and
3. the argument converting a cross-axis Jordan subcurve into a segment of
   the axis lying in a bounded complementary component of the full image.

The earlier partial packet is preserved in the run attempts area as the
superseded route that first established the half-plane and one-contact cases.

Packet PDF: `solution_packet.pdf`.
