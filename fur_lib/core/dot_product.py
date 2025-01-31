from math import pi
from typing import Callable

from numpy import arange
from scipy.integrate import quad

from fur_lib.utils.callable_math_operations import callable_mul


def integral_product(
        f1: Callable,
        f2: Callable,
        interval_start: int | float = -pi,
        interval_end: int | float = pi,
) -> int | float:
    """
    standard dot product used in almost all the literature related to Fourier series.
    """
    return quad(callable_mul(f1, f2), interval_start, interval_end)[0]


def vector_product(
        f1: Callable,
        f2: Callable,
        step: int | float,
        interval_start: int | float = pi,
        interval_end: int | float = pi,
) -> int | float:
    """
    The given scalar product is similar to the standard one,
    but instead of an integral that sums an infinite number of points,
    here the product of points is taken with a specific step size.
    """
    x = list(arange(interval_start, interval_end, step))
    vec_1 = [f1(i) for i in x]
    vec_2 = [f2(i) for i in x]
    return sum(a * b for a, b in zip(vec_1, vec_2))
