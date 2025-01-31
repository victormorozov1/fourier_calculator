from math import sin, cos

from fur_lib.core.dot_product import integral_product
from fur_lib.core.func import Func
from fur_lib.core.non_ortogonal_system import NonOrthogonalBasis
from fur_lib.tests.core.utils import check_func_equal

DIGITS_NUM = 3
EPSILON = 10 ** (-DIGITS_NUM)


class SomeNonOrthogonalBasis(NonOrthogonalBasis):
    ELEMENTS = [lambda x: cos(x), lambda x: sin(x) + cos(x)]

    def stupid_get_item(self, n: int):
        return Func(self.ELEMENTS[n])


def test_fourier_series_expansion():
    basis = SomeNonOrthogonalBasis(dot_product=integral_product)
    check_func_equal(cos, basis[0])
    check_func_equal(sin, basis[1])
