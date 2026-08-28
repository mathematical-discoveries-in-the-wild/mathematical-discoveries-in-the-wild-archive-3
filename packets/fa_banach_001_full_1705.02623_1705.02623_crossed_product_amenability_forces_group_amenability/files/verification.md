# Verification report

## Claim and scope

- Exact source target: source PDF page 16 asks whether amenability of
  `ell^1(G,A;alpha)` for nontrivial `A` implies amenability of the discrete
  group `G`.
- Packet answer: yes.  The proof only uses that `A` is a nonzero Banach
  algebra and the action is isometric.
- No unit, character, invariant state, positivity, separability, or
  countability assumption is used.

## Multiplier lemma audit

Let `B` be amenable and `M` a virtual diagonal.  A bounded approximate
identity `(e_lambda)` exists.  For a double centralizer `T=(L,R)`, a weak-star
cluster point `x_T` of `L(e_lambda)` in `B**` implements the multiplier:

- `x_T b = L(b)`, since `L(e_lambda)b=L(e_lambda b)`;
- `b x_T = R(b)`, since `bL(e_lambda)=R(b)e_lambda`.

The canonical Arens-extended module actions therefore give
`x_T M=M x_T` from centrality of `M` under `B`.  For finite multiplier and
algebra sets, Goldstine followed by Hahn--Banach convexification produces a
uniformly bounded tensor whose multiplier commutators and approximate
identity errors are small.  Directing these finite tests yields the stated
net.

Verifier focus: confirm that the two module actions are extended in the
weak-star continuous multiplier variable.  Equivalently, check the scalar
pairings against `X*`; both are bounded linear functionals of the multiplier
representative in `B**`.

## Coefficient audit

Under
`B tensor_pi B = ell^1(GxG,A tensor_pi A)`, set
`z_i(p)=D_i(p,p^{-1})`.  The canonical multiplier has

- `(u_g f)(r)=alpha_g(f(g^{-1}r))`;
- `(f u_g)(r)=f(rg^{-1})`.

At output coordinate `(gp,p^{-1})`, the first action contributes
`(alpha_g tensor id)z_i(p)` and the second contributes `z_i(gp)`.  Selecting
these coordinates is contractive, so their summed difference tends to zero.

If `c_i` is the identity coefficient of `pi(D_i)`, then for norm-one
`a in A`, approximate-identity convergence gives `c_i a -> a`.  Also
`c_i=sum_p m(id tensor alpha_p)z_i(p)`, hence
`||c_i|| <= sum_p ||z_i(p)||`.  The normalising mass is therefore bounded
away from zero.

The probability functions
`mu_i(p)=||z_i(p)|| / sum_q||z_i(q)||` satisfy
`||lambda_g mu_i-mu_i||_1 -> 0`, which is Reiter `P_1`.

## Literature and provenance audit

Searches performed through 2026-08-27:

- exact arXiv id and exact paper title;
- exact source-question phrases;
- `ell^1(G,A;alpha)` with amenability/converse/group-amenability terms;
- author-name and citation searches;
- related Fell-bundle and convolution-dominated-algebra searches;
- Ross Stokke's 2004 approximate-diagonal/Folner paper;
- recent work on Banach star algebras associated with group actions.

No explicit later solution of this converse was located.  Stokke gives a
related diagonal-to-invariance argument for scalar group algebras, not the
coefficient-valued theorem proved here.  Novelty is plausible, not certified.

## Rendering audit

- Final packet: 4 US-Letter pages.
- `solution_packet.pdf` SHA-256:
  `9a9d0ba82454229b5533f9d3f8daa9ff3d4f4aba6c5f35f565aa5553727870bf`.
- `source_paper.pdf` SHA-256:
  `0191d6f402c9416c593415378266266f26fd145b4d48eae634a409a8819e65ea`.
- `main.tex` SHA-256:
  `41aa01c110358143a691bf9acf8c8f773b6366dcbfae1aa66a91f5f49839e86c`.
- Source crop SHA-256:
  `97392ad23369a357929e5e29abec354bf541ff3c95ee0a30bc0b4b89d032d367`.
- LaTeX log: no warnings, undefined references, overfull boxes, or
  underfull boxes.
- Every final packet page was rendered to PNG and visually inspected.
  The source page and final question crop were also visually inspected.
