# Paired-zero subcase of the Branden--Chasse Fourier conjecture

Status: `candidate_partial_likely_valid`.

Source: Petter Branden and Matthew Chasse, *Classification theorems for
operators preserving zeros in a strip*, arXiv:1402.2795, published in
*Journal d'Analyse Mathematique* 132 (2017), 177--215.  The target is
Conjecture 6.1 on source page 29 (PDF page 29).

## Candidate partial result

Let

```text
H(z) = c z^(2m+1) exp(-alpha z^2)
       product_j (1-z/a_j)(1+z/b_j),
```

where `alpha>=0`, `a_j,b_j>0`, the reciprocal zero magnitudes are summable,
`c(-1)^m>0`, and

```text
sum_j atan(|a_j-b_j|/(2 sqrt(a_j b_j))) < pi/2.
```

If `G'=H` and `G(0)` is real, then

```text
F(z) = integral_R exp(G(it)) exp(izt) dt
```

is in the Laguerre--Polya class.  Thus Conjecture 6.1 holds for this
infinite-dimensional paired genus-zero class.

## Idea of the proof

Truncate the paired zero product and approximate the Gaussian factor by
`(1-alpha z^2/N)^N`.  Every resulting derivative is a real-rooted polynomial,
so the polynomial Fourier theorem from the source applies to its primitive.
The angular-defect sum keeps every derivative truncation in the same open
half-plane on the positive imaginary axis.  This yields one uniform
Gaussian-or-better tail bound for all primitive truncations.  Dominated
convergence then passes their Laguerre--Polya Fourier transforms to the desired
transcendental transform.

## Scope and limitations

The unrestricted conjecture remains open in this packet.  For general
Laguerre--Polya canonical products, compact convergence of real-rooted
derivative approximants does not control the imaginary-axis tails of their
primitives.  The added pairing/sector condition is precisely what supplies
that missing uniform domination.

The source statement writes `G(it) -> -infinity`.  The packet treats the
nontrivial intended reading `Re G(it) -> -infinity`, consistent with the
polynomial and coefficient-sign results immediately preceding the conjecture.

The bounded novelty check found no exact later solution or occurrence of this
paired-zero criterion, but definitive novelty is not claimed.  Some members of
the class may also satisfy the source's earlier eventual coefficient-sign
criterion; strict separation from that class has not been proved.

## Verification

The formal step-by-step adversarial check is in `verification.md`.  No
computational assertion is used.  The packet PDF includes the source crop,
the theorem, proof, limitations, and verifier focus.

Human review recommendation: verify the interpretation of Conjecture 6.1 and
the applicability of source Corollary 5.5 to every polynomial primitive;
mathematically, the remaining steps are elementary phase and dominated-
convergence estimates.
