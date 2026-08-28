# Adversarial verifier report

Verdict: `candidate_full_result_likely_valid`

Model: `GPT5.6`  
Date: 2026-08-26

## Scope and source match

- The source Problem 2.16 assumes `T` is bounded and adjointable and asks for
  invariance of every closed submodule.
- The theorem retains adjointability and exactly that closed-submodule
  quantifier. It does not silently replace all submodules by complemented
  submodules.
- The source's nonzero coefficient cannot cover `T=0`; the packet states this
  boundary explicitly. It also separates coefficients in `A` from natural
  coefficients in `M(A)`.
- Frank's arXiv:2507.11206 proves the bijective bounded-module case. The packet
  does not claim to settle the broader non-adjointable case.

## Lemma-by-lemma audit

### 1. Coefficient ideal reduction

`I_E=closure(span <E,E>)` is a closed two-sided ideal and `E I_E` is dense in
`E`, so `E` is full over `I_E`. If `M` is a closed `I_E`-submodule and
`u_lambda` is an approximate identity of `I_E`, then

```text
x a = lim (x u_lambda) a = lim x (u_lambda a) in M
```

for `a in A`; hence closed `A`- and `I_E`-submodules coincide. This step does
not require `I_E` to be essential in `A`.

### 2. Closed submodules versus closed right ideals

For a closed right ideal `J` of `B=K(E)`, set `M=closure(JE)`. The two
inclusions in

```text
J = closure(span{theta_(m,y): m in M, y in E})
```

are justified separately:

- `theta_(Sx,y)=S theta_(x,y)` lies in `J` because `J` is a right ideal;
- a finite-rank approximate identity `e_lambda` of `K(E)` gives
  `S e_lambda -> S`, with every term having first vector in `JE`.

If `T(M) subset M`, then `TS` is compact (adjointability is used here) and
has range in `M`, so the same approximation puts `TS` in `J`.

### 3. Right-ideal preserving multipliers are central

For positive `a in B`, the closed right ideal `closure(aB)` has weak-star
closure `p B**`, where `p=s(a)`. Invariance and normality of multiplication
give `(1-p) b p=0`.

If an irreducible image `pi(b)` is nonscalar, choose `xi` so `pi(b)xi` has a
nonzero component `zeta` orthogonal to `xi`. Kadison transitivity produces a
self-adjoint `c in B` acting on `span{xi,zeta}` as the projection onto `xi`.
For `a=c^2`, its support projection fixes `xi` and kills `zeta`. The relation
`(1-p)bp=0` then says `pi(b)xi` lies in the support range, contradicting the
`zeta` component. Thus every irreducible image is scalar, and irreducible
representations separate each commutator `[b,x] in B`.

This proof was specifically checked for the projectionless case: it constructs
an open projection in `B**`, not a projection in `B`.

### 4. Transfer of the center

For `U` commuting with `K(E)`, the map

```text
L_U(sum <x_k,y_k>) = sum <x_k,U y_k>
```

is well-defined because multiplying its value by any module vector gives
`U(w a)`. Fullness makes the coefficient action faithful. Its norm is bounded
by `||U||`, and `L_U(ab)=L_U(a)b`.

The map `R_U(a)=L_(U*)(a*)*` satisfies

```text
a L_U(b) = R_U(a) b
```

first for inner-product generators and then by density. Hence it is a double
centralizer `z in M(I_E)`. Approximate identities give `Uw=wz`; module
linearity then gives `w(az-za)=0`, and fullness forces `z` central. The same
faithfulness proves uniqueness.

### 5. Converse

If `z in Z(M(I_E))`, the image of `A` in `M(I_E)` commutes with `z`, so
`R_z` is `A`-linear. It is adjointable with adjoint `R_(z*)`. For a closed
submodule `M`,

```text
x z = lim x (z u_lambda) in M,
```

because `z u_lambda in I_E subset A`. Thus every closed submodule is
invariant.

## Boundary and falsification checks

- `A=C`, `E=H`: the theorem reduces to the classical scalar-operator result.
- `A=M_d(C)`, `E=A^n`: it gives scalar matrices with scalar coefficient, in
  agreement with the exact checker.
- `A=C_0(0,1)`, `E=A`, `z(t)=t`: multiplication is injective and not
  surjective, showing why injectivity cannot imply invertibility.
- `A` nonunital, `T=I_E`: the coefficient is `1 in M(A)`, confirming that the
  source's demand `a in A` cannot hold universally.
- No step uses an orthonormal module vector, closed range of `T`, injectivity,
  surjectivity, or complementability of submodules.

## Literature and novelty bound

The four cheap run indexes, local parsed arXiv sources, current arXiv pages for
2506.01161 and 2507.11206, and bounded exact-phrase searches were checked.
The search found Frank's bijective result, the standard closed-submodule/right-
ideal correspondence, and Blecher-Effros-Zarikian's one-sided M-ideal
framework. It did not find the theorem proved here. This is not an exhaustive
publication-novelty certification.

## Final verifier focus

The two highest-value human checks are:

1. verify the use of weak-star density of `pB** cap B` in `pB**` and the
   support-projection image under an irreducible representation;
2. verify the double-centralizer compatibility identity and the norm estimate
   extending `L_U` from `span <E,E>`.
