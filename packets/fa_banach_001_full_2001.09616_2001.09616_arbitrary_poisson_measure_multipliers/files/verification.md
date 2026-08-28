# Verification report

Status: candidate full proof, likely valid.  
Model: GPT5.6.

## Formal checks

- Centered-polar geometry: `1-|z|^2 = rho(2a-rho)` and the real
  `2d`-dimensional polar Jacobian exactly cancel the singular power in the
  Euclidean Poisson kernel.
- Tip trace: on compact angular subsets the radial energy gives `L2` ray
  limits; a sequence with vanishing angular energy plus angular Poincare
  forces the limit to be constant.
- Anchored Hardy coefficient: after scaling `t=s/L`, the kernel ratio is
  `(1-t)(2t+1)/6`, whose maximum on `[0,1]` is exactly `3/16` at `t=1/4`.
- Stabilizer projection: invariance and Jensen contract both the Hardy norm
  and atomic gradient energy.
- Marginal scaling: on a dyadic box, `A ~ delta`, `b ~ delta^2`; integrating
  only over `u in [b,2b]` gives `W_d >= c_d/delta`.
- Final integration: Tonelli applies to nonnegative integrands and avoids any
  polynomial-density or dilation step.

## Computational guard

Run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/verify_atomic_geometry.py
```

The final run passed:

```text
PASS
centered-polar identities: 800
Hardy-kernel samples: 10001
Hardy-kernel maximum: 0.1875 (exact 3/16)
dyadic marginal samples: 567
d=2..8: min(delta * W_d) ranged from 1.57270428773 to 0.102438990939
```

These are algebraic/scaling guards only; the analytic proof is in the PDF.

## Human verifier focus

1. Confirm that the finite-energy trace argument on the expanding angular
   hemisphere is adequately explicit.
2. Confirm that the dyadic submean boxes can be chosen with bounded overlap
   and the stated `A,b` comparabilities.
3. Confirm the trace of the stabilizer average agrees with the original tip
   trace.
4. Check later citations to the JFA paper for priority/novelty.

## Artifact QA

- `solution_packet.pdf` has six pages.
- The final LaTeX log has no warnings, overfull boxes, or unresolved
  references.
- All six final rendered pages were inspected at 150 dpi; no clipping,
  overlap, broken glyphs, or unreadable content was found.
- PDF SHA-256:
  `c04b4aeab14d07509dc4833635940f27f5785f1704a3e95d1763cf2d9dc8d0a8`.
