"""Exact five-node check for the gradient-energy counterexample."""

from fractions import Fraction as F


def phi(s: F) -> F:
    if s <= 0:
        return 4 * s
    if s <= 2:
        return s * (2 - s) ** 2
    return F(0)


def dphi(s: F) -> F:
    if s <= 0:
        return F(4)
    if s <= 2:
        return (2 - s) * (2 - 3 * s)
    return F(0)


def neumann_laplacian(v: list[F]) -> list[F]:
    """Unit-mesh path Laplacian with reflecting endpoint flux."""
    out = []
    for index, value in enumerate(v):
        left = v[index - 1] if index else value
        right = v[index + 1] if index + 1 < len(v) else value
        out.append(left - 2 * value + right)
    return out


u = [F(2), F(2), F(3, 2), F(2), F(2)]
v = [phi(value) for value in u]
lap_v = neumann_laplacian(v)
u_t = lap_v
v_t = [dphi(value) * velocity for value, velocity in zip(u, u_t)]

# Forward differences, with the zero extension at the right endpoint.
d_v = [v[index + 1] - v[index] for index in range(len(v) - 1)] + [-v[-1]]
d_v_t = [v_t[index + 1] - v_t[index] for index in range(len(v_t) - 1)] + [-v_t[-1]]

energy = sum(value * value for value in d_v) / 2
energy_derivative_direct = sum(a * b for a, b in zip(d_v, d_v_t))
energy_derivative_identity = -sum(
    dphi(value) * lap * lap for value, lap in zip(u, lap_v)
)

assert v == [F(0), F(0), F(3, 8), F(0), F(0)]
assert energy == F(9, 64)
assert energy_derivative_direct == F(45, 64)
assert energy_derivative_identity == energy_derivative_direct

print(f"v={v}")
print(f"Delta v={lap_v}")
print(f"E(0)={energy}")
print(f"E'(0)={energy_derivative_direct} > 0")
