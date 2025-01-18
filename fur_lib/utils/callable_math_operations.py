import operator
from functools import partial
from typing import Callable


def _helper(op: Callable, f1: Callable, f2: Callable) -> Callable:
    return lambda *args, **kwargs: op(f1(*args, **kwargs), f2(*args, **kwargs))


callable_sum = partial(_helper, operator.add)
callable_diff = partial(_helper, operator.sub)
callable_mul = partial(_helper, operator.mul)
callable_truediv = partial(_helper, operator.truediv)


def callable_number_mul(f1: Callable, num: int | float) -> Callable:
    return lambda *args, **kwargs: f1(*args, **kwargs) * num
