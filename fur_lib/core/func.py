from __future__ import annotations

from typing import Any, Callable

from fur_lib.utils.callable_math_operations import callable_diff, callable_number_mul, callable_sum


class Func:
    def __init__(self, func: Callable, *, name: str | None = None, skip_small_numbers_in_names: bool = True):
        self.func = func
        self.name = name
        self.skip_small_numbers_in_names = skip_small_numbers_in_names

    @staticmethod
    def _get_new_name(name_1: Any, name_2: Any, op: str) -> str | None:
        if name_1 is not None and name_2 is not None:
            return f'({name_1} {op} {name_2})'

    def __mul__(self, other: int | float, eps=10**-10):
        if other > eps or not self.skip_small_numbers_in_names:
            new_name = self._get_new_name(self.name, other, '*')
        else:
            new_name = self.name
        return self.__class__(callable_number_mul(self.func, other), name=new_name)

    def __add__(self, other: Func) -> Func:
        f = callable_sum(self.func, other.func)
        return self.__class__(f, name=self._get_new_name(self.name, other.name, '+'))

    def __sub__(self, other: Func) -> Func:
        f = callable_diff(self.func, other.func)
        return self.__class__(f, name=self._get_new_name(self.name, other.name, '+'))

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __str__(self) -> str:
        if self.name:
            return f'Func[{self.name}]'
        return super().__str__()

    def __repr__(self) -> str:
        if self.name:
            return f'<Func[{self.name}]>'
        return super().__repr__()
