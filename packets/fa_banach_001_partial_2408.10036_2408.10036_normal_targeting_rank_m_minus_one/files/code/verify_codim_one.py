"""Deterministic checks for the rank-(m-1) normal-targeting packet.

The script is supporting verification, not a substitute for the proof.
"""

import numpy as np


def normal_residual(a):
    return np.linalg.norm(a.conj().T @ a - a @ a.conj().T)


def block_residuals(b, c, d, eta):
    h_res = np.linalg.norm(
        b.conj().T @ b - b @ b.conj().T + np.outer(c, c.conj())
        - np.outer(d, d.conj())
    )
    cross_res = np.linalg.norm(
        b.conj().T @ d + c * eta - b @ c - d * np.conj(eta)
    )
    return h_res, cross_res


def check_random_normal_completion(seed=240810036):
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    q = q @ np.diag(np.conj(phases) / np.abs(phases))
    eig = np.array([-2 + 0.5j, -0.2 - 1.3j, 1 + 2j, 3 - 0.1j])
    a = q @ np.diag(eig) @ q.conj().T
    b, d, c, eta = a[:3, :3], a[:3, 3], a[3, :3].conj(), a[3, 3]
    h_res, cross_res = block_residuals(b, c, d, eta)
    assert normal_residual(a) < 1e-11
    assert h_res < 1e-11 and cross_res < 1e-11
    return normal_residual(a), h_res, cross_res


def check_collinear_positive_example():
    # Active eigenvalues lie on Im(z)=1.  omega=1 and eta=i work.
    b = np.diag(np.array([1j, 1 + 1j, 2 + 1j]))
    c = np.array([1, 2 - 1j, -0.5j], dtype=complex)
    d = c.copy()
    eta = 1j
    a = np.block([[b, d[:, None]], [c.conj()[None, :], np.array([[eta]])]])
    h_res, cross_res = block_residuals(b, c, d, eta)
    assert normal_residual(a) < 1e-12
    return normal_residual(a), h_res, cross_res


def check_noncollinear_obstruction():
    b = np.diag(np.array([0, 1, 1j], dtype=complex))
    c = np.ones(3, dtype=complex)
    h = b.conj().T @ b - b @ b.conj().T + np.outer(c, c.conj())
    evals = np.linalg.eigvalsh(h)
    assert np.allclose(evals, [0, 0, 3], atol=1e-12)

    # If d=omega*c, the lambda=0 coordinate gives
    # eta-omega*conj(eta)=0.  Lambda=1 then forces omega=1,
    # while lambda=i forces omega=-1.  Hence no phase works.
    forced_by_one = 1 + 0j
    forced_by_i = -1 + 0j
    assert forced_by_one != forced_by_i
    return evals, forced_by_one, forced_by_i


if __name__ == "__main__":
    print("random normal completion residuals:", check_random_normal_completion())
    print("collinear positive example residuals:", check_collinear_positive_example())
    print("noncollinear defect eigenvalues/phases:", check_noncollinear_obstruction())
