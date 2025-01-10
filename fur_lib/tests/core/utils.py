from math import isclose
from typing import Callable

EPSILON = 10 ** -3


def check_func_equal(
        f1: Callable,
        f2: Callable,
        check_start: int | float = -100,
        check_end: int | float = 100,
        checks: int = 10,
        epsilon: int | float = EPSILON,
):
    for i in range(checks):
        x = check_start + i * (check_end - check_start) / (checks - 1)
        assert isclose(f1(x), f2(x), abs_tol=epsilon)
