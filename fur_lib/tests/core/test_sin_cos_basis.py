from math import isclose

from fur_lib.core.sin_cos_basis import SinCosBasis


def test_sin_cos_basis():
    basis = SinCosBasis(10, 20)
    assert basis[0].name == 'cos(0x)'
    assert basis[0](13.6) == 1  # cos(0) == const 1 == 1
    assert basis[1].name == 'sin(1x)'
    assert isclose(basis[1](10), 0, abs_tol=0.0001)     # sin(-pi) == 0
    assert isclose(basis[1](15), 0, abs_tol=0.0001)     # sin(0) == 0
    assert isclose(basis[1](20), 0, abs_tol=0.0001)     # sin(pi) == 0
    assert isclose(basis[1](12.5), -1, abs_tol=0.0001)  # sin(-pi/2) == -1
    assert basis[3].name == 'sin(2x)'
    assert isclose(basis[3](12.5), 0, abs_tol=0.0001)   # sin(-pi) == 0
    assert basis[4].name == 'cos(2x)'
    assert isclose(basis[4](12.5), -1, abs_tol=0.0001)   # cos(-pi) == -1
