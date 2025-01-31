import pytest
from math import isclose, pi, sin, cos
from typing import Callable

from fur_lib.core.func import Func
from fur_lib.core.system import System
from fur_lib.core.sin_cos_basis import SinCosBasis
from fur_lib.tests.core.utils import check_func_equal
from fur_lib.utils.callable_math_operations import callable_number_mul, callable_sum
from fur_lib.core.dot_product import integral_product


@pytest.mark.parametrize(
    ('func', 'expected'),
    (
            (lambda x: x + 1, [1, 2 / 1, 0, -2 / 2, 0, 2 / 3, 0, -2 / 4, 0, 2 / 5]),
            (
                    lambda x: abs(x + 1),
                    [
                        (pi ** 2 + 1) / 2 / pi,
                        2 / pi * (sin(1) - 1 * (-1) ** 1) / 1 ** 2,
                        2 / pi * ((-1) ** 1 - cos(1)) / 1 ** 2,
                        2 / pi * (sin(2) - 2 * (-1) ** 2) / 2 ** 2,
                        2 / pi * ((-1) ** 2 - cos(2)) / 2 ** 2,
                        2 / pi * (sin(3) - 3 * (-1) ** 3) / 3 ** 2,
                        2 / pi * ((-1) ** 3 - cos(3)) / 3 ** 2,
                        2 / pi * (sin(4) - 4 * (-1) ** 4) / 4 ** 2,
                        2 / pi * ((-1) ** 4 - cos(4)) / 4 ** 2,
                        2 / pi * (sin(5) - 5 * (-1) ** 5) / 5 ** 2,
                    ],
            ),
    ),
)
def test_fourier_series_expansion(func: Callable, expected: list[int | float]):
    digits_num = 3
    epsilon = 10 ** (-digits_num)
    system = System(SinCosBasis(), integral_product)
    func = Func(func)
    res = [system.fourier_coefficient(func, i) for i in range(10)]
    err_str = f'Expected: {[round(e, digits_num) for e in expected]}, Actual: {[round(r, digits_num) for r in res]}'
    assert all(isclose(res[i], expected[i], abs_tol=epsilon) for i in range(10)), err_str

    sin_cos_basis = [
        lambda x: 1,
        sin,
        cos,
        lambda x: sin(2 * x),
        lambda x: cos(2 * x),
        lambda x: sin(3 * x),
        lambda x: cos(3 * x),
        lambda x: sin(4 * x),
        lambda x: cos(4 * x),
        lambda x: sin(5 * x),
    ]
    expected_func = callable_number_mul(sin_cos_basis[0], expected[0])
    for i in range(1, 10):
        f = callable_number_mul(sin_cos_basis[i], expected[i])
        expected_func = callable_sum(expected_func, f)
    actual_func = system.fourier_sum(func, 10)
    check_func_equal(expected_func, actual_func, check_start=-pi + 0.1, check_end=pi - 0.1, epsilon=0.6)
