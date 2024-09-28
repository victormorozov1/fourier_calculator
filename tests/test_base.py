import pytest

from base import System, SinCosBasis, PIClosedIntervalFunc
from math import isclose, pi, sin, cos


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
def test_fourier_series_expansion(func, expected):
    digits_num = 3
    epsilon = 10 ** (-digits_num)
    system = System(SinCosBasis())
    func = PIClosedIntervalFunc(func)
    res = [system.fourier_coefficient(func, i) for i in range(10)]
    err_str = f'Expected: {[round(e, digits_num) for e in expected]}, Actual: {[round(r, digits_num) for r in res]}'
    assert all(isclose(res[i], expected[i], abs_tol=epsilon) for i in range(10)), err_str
