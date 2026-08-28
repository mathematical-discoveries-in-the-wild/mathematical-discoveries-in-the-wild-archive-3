# Verification Report

Candidate: arXiv:1112.4878, final `ax+b` example (PDF page 37)

## Claim Checked

For the positive irreducible representation

```text
(pi_+(a,b)f)(s) = a^(1/2) exp(ibs) f(as)
```

of the real affine group, the Gelfand spectrum of its Fourier--Stieltjes-norm
coefficient algebra is exactly the semigroup of operators

```text
tilde-pi_+(a,z),  a>0, Im z>=0.
```

## Verdict

`likely valid`

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Sum--ratio unitary | valid | The Jacobian of `(r,u) -> (ru,r(1-u))` is `r`; the factor `r^(1/2)` makes the map unitary. Direct substitution gives `pi_+ tensor pi_+ = pi_+ tensor I`. |
| Identification of the coproduct | valid | Both normal star homomorphisms send every `pi_+(g)` to `pi_+(g) tensor pi_+(g)`. Irreducibility gives `VN_pi=B(H)`, so they agree everywhere. |
| Angular commutation | valid | Radial amplification commutes with all multipliers in the ratio variable `u=s/(s+t)`; hence every group-like tensor square does too. |
| Positive interval-block lemma | valid | Positivity guarantees a nonzero diagonal compression in any countable narrow multiplicative partition. Tensoring a hypothetical separated off-diagonal block with that compression crosses disjoint angular spectral sets, contradicting commutation. |
| Multiplication conclusion | valid | Vanishing between all separated bounded intervals passes by strong limits to the two sides of every cut `(0,t) | (t,infinity)`. These spectral projections generate the multiplication masa. |
| Positive Cauchy equation | valid | For a multiplier, the coproduct equation is exactly `f(s+t)=f(s)f(t)` almost everywhere. Measurability, positivity, nonzeroness, and norm one give `f(s)=exp(-cs)`, `c>=0`. |
| Unitary ratio identity | valid | Conjugating the bounded ratio operator by `V tensor V` replaces `Q` by `A=V*QV`. The group-like angular commutation fixes this ratio. |
| Imaginary-power step | valid | Applying `(r/(1-r))^(it)` is bounded Borel functional calculus, so there is no illicit subtraction of unbounded logarithms. It gives `A^(it) tensor A^(-it)=Q^(it) tensor Q^(-it)`. |
| Scalar tensor factors | valid | From `C tensor D=I`, a vector slice nonzero on `D` makes `C` scalar; then `D` is the reciprocal scalar. Strong continuity makes the scalar a character of `R`. |
| Unitary normal form | valid | `V*QV=alpha Q` implies `V D_a*` commutes with `Q` for `a=alpha^(-1)`, hence is a unimodular multiplier. Its group-like equation is the circle-valued Cauchy equation, giving `exp(ibs)`. |
| Polar completion | valid | Absolute values are preserved by the coproduct. Support projections of the polar partial isometry are nonzero group-like projections and hence identities by the positive classification. |
| Parameter match | valid | `pi_+(a,b) M_exp(-cs)` equals `tilde-pi_+(a,b+iac)`, exactly matching the source's polar factor `c=a^(-1) Im z`. |
| Topology | valid | Escaping parameters have weak-operator limit zero on compactly supported test vectors; the solution set plus zero is weak-operator compact and the parameter map extends to a continuous bijection of one-point compactifications. |
| Match to source question | valid | The source conjectures precisely that no extra coefficient-norm characters occur beyond this complexified semigroup. The theorem proves equality, while explicitly not claiming the full general Conjecture 3.9(ii). |

## Adversarial Failure Search

- **Hidden kernel representation:** none is used. The positive rigidity argument
  is stated entirely with projections and operator blocks.
- **Need for invertibility of a positive character:** none is assumed. Support
  projections are classified after the positive operator itself.
- **Nontrivial group-like projections:** the positive classification makes a
  projection `M_exp(-cs)`, which is idempotent only for `c=0`.
- **Unbounded-log domain error:** avoided by applying bounded imaginary powers
  to the bounded ratio operator.
- **Tensor-scalar loophole:** both tensor factors are unitaries, so a nonzero
  vector slice always exists and scalarity follows.
- **Almost-everywhere Cauchy equations:** both functions are measurable and
  bounded; the standard measurable exponential classification applies after a
  null-set modification, which does not change the operators.
- **Topology overclaim:** the proof treats nets through compactification, not
  only sequences. Escape in the oscillatory coordinate is uniform over compact
  sets of the other parameters by compactness in `L1` plus Riemann--Lebesgue.

No counterexample or unresolved logical gap was found.

## Novelty Check

The four cheap run indexes and the local source corpus contained no result for
arXiv:1112.4878 or the exact spectral-naturalness question. Bounded web/arXiv
searches for the exact conjecture phrase, `spectrally natural`, `Wiener-Pitt
representation`, `ax+b coefficient algebra spectrum`, the title, and close
variants found the source article and unrelated citations, but no later
resolution. Subscription databases were not searched.

## External Dependencies

The proof uses the Walter character criterion and polar-decomposition closure
proved in the source article. The tensor decomposition needed to invoke it is
rederived in the packet. All remaining ingredients are elementary spectral
calculus, maximal abelianness of the multiplication algebra, and the measurable
Cauchy equation.

## Confidence

Score: 94/100.

Reason: the classification reduces to two self-contained operator lemmas, and
each delicate step has a bounded-operator formulation. The remaining review
risk is concentrated in the projection-block exhaustion and in checking all
functional-calculus identifications at the endpoints of the ratio spectrum.

## Human Review Recommendation

`send to human`
