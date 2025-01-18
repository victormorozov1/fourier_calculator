from __future__ import annotations

from abc import ABC
from typing import Any, Callable, overload

from scipy.integrate import quad

from fur_lib.core.system_object import SystemObject
from fur_lib.utils.callable_math_operations import callable_mul, callable_sum, callable_number_mul


class ClosedIntervalFunc(SystemObject, ABC):
    def __init__(
            self,
            func: Callable,
            *,
            interval_start: int | float,
            interval_end: int | float,
            name: str | None = None,
            skip_small_numbers_in_names: bool = True,
    ):
        self.func = func
        self.interval_start = interval_start
        self.interval_end = interval_end
        self.name = name
        self.skip_small_numbers_in_names = skip_small_numbers_in_names

    @staticmethod
    def _get_new_name(name_1: Any, name_2: Any, op: str) -> str | None:
        if name_1 is not None and name_2 is not None:
            return f'({name_1} {op} {name_2})'

    @overload
    def __mul__(self, other: int | float) -> ClosedIntervalFunc:
        pass

    @overload
    def __mul__(self, other: ClosedIntervalFunc) -> int | float:
        pass

    def __mul__(self, other, eps=10**-10):
        if isinstance(other, (int, float)):
            return self.__class__(
                callable_number_mul(self.func, other),
                interval_start=self.interval_start,
                interval_end=self.interval_end,
                name=self._get_new_name(self.name, other, '*') if (other > eps or not self.skip_small_numbers_in_names) else self.name,
            )
        return quad(callable_mul(self.func, other.func), self.interval_start, self.interval_end)[0]

    def __add__(self, other: ClosedIntervalFunc) -> ClosedIntervalFunc:
        f = callable_sum(self.func, other.func)
        return self.__class__(
            f,
            interval_start=self.interval_start,
            interval_end=self.interval_end,
            name=self._get_new_name(self.name, other.name, '+'),
        )

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __str__(self) -> str:
        if self.name:
            return f'ClosedIntervalFunc[{self.name}]'
        return super().__str__()

    def __repr__(self) -> str:
        if self.name:
            return f'<ClosedIntervalFunc[{self.name}]>'
        return super().__repr__()