# Elementary polygonal proof of the outer-anticircle Bonnesen inequality

Status: `candidate_full_solution_likely_valid`

Agent: `agent_lane_03`  
Model: `GPT5.6`  
Date: 2026-08-26

## Source request

Martini and Swanepoel, *Antinorms and Radon curves*,
arXiv:math/0409200, prove that if `sigma I` is a smallest anticircle
containing a planar convex body `C`, then

```text
area(C) + area(sigma I) <= sigma perimeter(C).                 (13)
```

Their proof invokes Blaschke's mixed-area inequality. Immediately after
Theorem 15, on arXiv PDF page 19 (source lines 962--978), they say that they
do not know an elementary proof of (13) involving polygons, analogous to
their polygonal proof of the inner-radius inequality (12).

This packet supplies such a proof. It uses only supporting lines, the
shoelace/support-number area formula for polygons, an algebraic discrete
Dirichlet inequality, and simultaneous circumscribed-polygon approximation.
It does not invoke Blaschke's inequality or the Minkowski inequality.

## Proof map

Translate and scale so that the minimum containing anticircle is the unit
anticircle `I`. Let `h_C` and `h_I` be support functions and set
`d = h_I-h_C >= 0`.

1. Minimality of `I` implies that the outward normals at common supporting
   lines of `C` and `I` are not contained in an open semicircle. Hence one
   may select two or three contact normals whose consecutive angular gaps
   are at most `pi`.
2. First suppose `C` and `I` are polygons, and refine to a common normal
   fan with directions `theta_i`, gaps `alpha_i`, and support vectors `c`
   and `k`. The polygon area is the quadratic form

   ```text
   Q(h) = sum_i h_i h_{i+1}/sin(alpha_i)
          - (1/2) sum_i h_i^2(cot(alpha_{i-1})+cot(alpha_i)).
   ```

   If `B` is its polarization, the norm perimeter is `2B(c,k)`. Thus

   ```text
   area(C)+area(I)-perimeter(C) = Q(c-k) = Q(d).
   ```

3. The selected contact normals have `d_i=0`, so `Q(d)` splits into paths
   whose total angles are at most `pi`. On a path, `-2Q` is

   ```text
   sum_i e_{alpha_i}(d_i,d_{i+1}),
   e_a(x,y) = (cos(a)(x^2+y^2)-2xy)/sin(a).
   ```

   The exact merge identity

   ```text
   e_a(x,z)+e_b(z,y)-e_{a+b}(x,y)
     = sin(a+b)/(sin(a)sin(b))
       * (z-(x sin(b)+y sin(a))/sin(a+b))^2
   ```

   shows by induction that every zero-endpoint path of total angle below
   `pi` has nonnegative energy. The endpoint `pi` follows by continuity.
   Therefore `Q(d)<=0`, which is (13) in the normalized polygonal case.
4. Approximate `C` and `I` by circumscribed polygons using the same
   increasingly dense symmetric normal sets, always retaining the selected
   contact normals. The contact balance makes each approximating `I_n` a
   minimum containing homothet for `C_n`. Areas and polarized polygon areas
   converge, yielding the inequality for arbitrary convex bodies. Scaling
   back gives the stated factor `sigma`.

The complete proof, including the contact-normal lemma and the approximation
argument, is in `solution_packet.pdf` and `main.tex`.

## Verification

`code/verify_discrete_energy.py` checks the two-angle merge identity, thousands of
random zero-endpoint paths of total angle at most `pi`, the support-number
area formula against shoelace area, and the identity `Q=-E/2`.

Representative command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/0409200_elementary_polygonal_outer_bonnesen/code/verify_discrete_energy.py \
  --trials 20000 --seed 20260826
```

These computations are consistency checks, not substitutes for the proof.

## Novelty search and scope

The four run indexes contained no entry for arXiv:0409200 or this proof
request. Exact-title citations in the local parsed arXiv corpus were checked;
the substantive hits use the paper for antinorm/Radon background and do not
discuss the missing polygonal proof. Current web searches used the exact
sentence, `smallest anticircle`, the displayed inequality, and polygonal
Bonnesen variants. They recovered the source and general mixed-area proofs,
but no later elementary polygonal proof. This is bounded novelty evidence,
not a guarantee of publication novelty.

The theorem itself is classical and already proved in the source through
Blaschke's inequality. The claimed new contribution is only the requested
elementary polygonal proof.

## Files

- `solution_packet.pdf`: review packet
- `main.tex`: packet source
- `source_paper.pdf`: arXiv:math/0409200
- `figures/open_problem_crop.png`: source-paper request on PDF page 19
- `code/verify_discrete_energy.py`: exact/numerical consistency checks
- Ledger:
  `runs/fa_banach_001/ledger/results/0409200_elementary_polygonal_outer_bonnesen.json`
