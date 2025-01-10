from math import sin, cos, pi

from fur_lib.core.closed_interval_func import ClosedIntervalFunc
from fur_lib.core.non_ortogonal_system import NonOrthogonalBasis
from fur_lib.tests.core.utils import check_func_equal

DIGITS_NUM = 3
EPSILON = 10 ** (-DIGITS_NUM)


class SomeNonOrthogonalBasis(NonOrthogonalBasis):
    ELEMENTS = [lambda x: cos(x), lambda x: sin(x) + cos(x)]

    def stupid_get_item(self, n: int):
        return ClosedIntervalFunc(self.ELEMENTS[n], interval_start=-pi, interval_end=pi)


def test_fourier_series_expansion():
    basis = SomeNonOrthogonalBasis()
    check_func_equal(cos, basis[0])
    check_func_equal(sin, basis[1])
