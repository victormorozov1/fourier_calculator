from base import ClosedIntervalFunc
from math import isclose, sin, cos, pi
from non_ortogonal_system import NonOrthogonalBasis


DIGITS_NUM = 3
EPSILON = 10 ** (-DIGITS_NUM)


class SomeNonOrthogonalBasis(NonOrthogonalBasis):
    ELEMENTS = [lambda x: cos(x), lambda x: sin(x) + cos(x)]

    def stupid_get_item(self, n: int):
        return ClosedIntervalFunc(self.ELEMENTS[n], interval_start=-pi, interval_end=pi)


def check_func_equal(f1, f2):
    for i in [0, -5, 10, 15, 100]:
        assert isclose(f1(i), f2(i), abs_tol=EPSILON)


def test_fourier_series_expansion():
    basis = SomeNonOrthogonalBasis()
    check_func_equal(cos, basis[0])
    check_func_equal(sin, basis[1])
