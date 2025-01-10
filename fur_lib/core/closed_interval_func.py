from __future__ import annotations

from abc import ABC
from typing import Callable, overload

from scipy.integrate import quad

from fur_lib.core.system_object import SystemObject
from fur_lib.utils.callable_math_operations import callable_mul, callable_sum, callable_number_mul


class ClosedIntervalFunc(SystemObject, ABC):
    def __init__(self, func: Callable, *, interval_start: int | float, interval_end: int | float):
        self.func = func
        self.interval_start = interval_start
        self.interval_end = interval_end

    @overload
    def __mul__(self, other: int | float) -> ClosedIntervalFunc:
        pass

    @overload
    def __mul__(self, other: ClosedIntervalFunc) -> int | float:
        pass

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                callable_number_mul(self.func, other),
                interval_start=self.interval_start,
                interval_end=self.interval_end,
            )
        return quad(callable_mul(self.func, other.func), self.interval_start, self.interval_end)[0]

    def __add__(self, other: ClosedIntervalFunc) -> ClosedIntervalFunc:
        f = callable_sum(self.func, other.func)
        return self.__class__(f, interval_start=self.interval_start, interval_end=self.interval_end)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
