from __future__ import annotations

from typing import Generic

from fur_lib.core.typing import Basis, SystemObjectType


class System(Generic[SystemObjectType]):
    """
    Под системой понимаю множество элементов,
    где один из элементов этого множества раскладывается через элементы базиса
    """

    def __init__(self, basis: Basis[SystemObjectType]):
        self.basis = basis

    def fourier_coefficient(self, obj: SystemObjectType, n: int) -> int | float:
        base_obj = self.basis[n]
        return (obj * base_obj) / (base_obj * base_obj)

    def fourier_sum(self, obj: SystemObjectType, n: int) -> SystemObjectType:
        summ = self.basis[0] * self.fourier_coefficient(obj, 0)
        for i in range(1, n):
            summ = summ + self.basis[i] * self.fourier_coefficient(obj, i)
        return summ






