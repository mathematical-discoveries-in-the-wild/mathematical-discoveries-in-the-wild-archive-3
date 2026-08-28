# Verification report

Verdict: `candidate_full_negative_solution_likely_valid`

## Claim audited

For `d=qn+r`, `0<=r<n`, the least possible local multiplicity at each of
`[0:1:+/-i]` among degree-`d` `C_n`-invariant forms is `ceil(r/2)`, and this
value is generic. For every `q>=1`, `r>=3`, it occurs for normalized strictly
hyperbolic real forms. Therefore the conjectured value `binomial(r,2)` in
Section 8.1 of arXiv:2102.01726 is false.

## Proof audit

1. **Local coordinates.** At `P_+=[0:1:i]`, use `x=1`, `y=i+z` and set
   `u=x+iy`, `v=x-iy`. Then `u=iz` and `v=2-iz` is a unit. Hence the invariant
   monomial `t^(d-j-k)u^jv^k` has local order `d-k`. At `P_-`, the same
   calculation swaps `j` and `k`.

2. **Support maximum.** Write `k=an+b`, `0<=b<n`. Since `j congruent k mod n`
   and `j>=0`, one has `j>=b`, so `d>=an+2b`. Necessarily `a<=q`. If `a<q`,
   then `k<=qn-1`; if `a=q`, then `b<=floor(r/2)`. Thus
   `k<=qn+floor(r/2)`, with equality at the unique pair
   `(j,k)=(floor(r/2), qn+floor(r/2))`. This gives the sharp lower bound
   `ceil(r/2)` and prevents cancellation of the lowest term when the unique
   extremal coefficient is nonzero.

3. **Reality and symmetry.** The perturbation
   `G=t^delta(u^s v^(qn+s)+u^(qn+s)v^s)`, where
   `s=floor(r/2)` and `delta=r-2s`, is fixed by complex conjugation and hence
   has real coefficients. Its two exponent differences are `+/-qn`, so it is
   `C_n`-invariant; swapping `u` and `v` also fixes it, giving the dihedral
   symmetry.

4. **Exact multiplicity.** The radial base form has local order `ceil(d/2)`
   at both points. Since `q>=1` and `r<n`, this is strictly larger than
   `ceil(r/2)`. The perturbation has a nonzero term of exact order
   `s+delta=ceil(r/2)` at each point. Therefore every nonzero perturbation
   parameter gives exactly that multiplicity, with no possible cancellation.

5. **Strict hyperbolicity.** On the unit circle `x^2+y^2=1`, the radial base
   form is a fixed monic polynomial in `t` with `d` distinct real roots. Take
   pairwise disjoint small intervals around those roots on whose endpoints
   the base polynomial has opposite signs. The perturbation is uniformly
   bounded on the finite endpoint set times the unit circle. For sufficiently
   small parameter, all endpoint signs persist, so the IVT gives one root in
   each of the `d` intervals. Degree `d` forces these to be all the roots and
   all distinct. Homogeneity reduces every nonzero `(x,y)` to the unit circle.

6. **Violation.** For every integer `r>=3`,
   `ceil(r/2) < r(r-1)/2`. Thus the constructed curves violate the exact
   claimed multiplicity for every residue covered by the conjecture.

## Exact mechanical checks

`code/verify_local_orders.py` uses SymPy to:

- expand the `n=4,d=7` example at both forced points;
- verify local orders `ord(H)=4` and `ord(G)=2` and print the degree-2 terms;
- verify real coefficients and invariance under a quarter turn and reflection;
- brute-force the invariant support for 495 `(n,d)` pairs and compare its
  minimum local order against `ceil((d mod n)/2)`.

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2102.01726_forced_singularity_multiplicity_counterexample/code/verify_local_orders.py
```

The script is a consistency check, not the proof; the support optimization and
hyperbolicity argument are proved symbolically in the packet.

The exact output was:

```text
P_plus: ord(H)=4, initial(H)=288*I*t*z**3
P_plus: ord(G)=2, initial(G)=32*I*t*z
P_minus: ord(H)=4, initial(H)=-288*I*t*z**3
P_minus: ord(G)=2, initial(G)=-32*I*t*z
support formula verified for 495 (n,d) pairs
all exact checks passed
```

## Bounded novelty check

On 27 August 2026, the run registry, solution index, attempt index, and
proof-gap index were searched using arXiv id `2102.01726`, the exact
multiplicity language, and the terms `invariant hyperbolic`, `singularity`,
and `[0:1:i]`. Live web/arXiv searches used the exact sentence `We conjecture
they each have multiplicity`, the paper title, arXiv id, the authors' names,
and combinations of `d mod n`, `multiplicity`, `correction`, and
`counterexample`. The searches found the source paper and mirrors, but no
later paper, correction, or preprint claiming this support formula or
resolving the conjecture. This is a bounded search, not an exhaustive novelty
guarantee.

## Main review focus

Verify that the source conjecture intends ordinary plane-curve multiplicity at
the two named projective points. Under that standard meaning, the local Taylor
order calculation is decisive. No unproved external lemma remains.

## Mechanical and visual checks

The packet was compiled with `latexmk`; the final log contains no warnings,
undefined references, or overfull/underfull box reports. All five final pages
and the source crop were rendered and visually inspected. Ghostscript text
extraction contains the theorem, the strict-hyperbolicity argument, the
counterexample conclusion, and the references. SHA-256 hashes:

- `solution_packet.pdf`: `33cf87ab8a11fb041ab5d9738361e70671845a73eef1bd4babc50784a9bf36a7`
- `source_paper.pdf`: `4d984439091c0bbdcd99e43210d95ef43b114bb10bab1f0d31b56cfded817587`
- `figures/open_problem_crop.png`: `a726957565ccab222b6a819e3e33a8748c1c46ade3e9e316b8a016b83effad96`
