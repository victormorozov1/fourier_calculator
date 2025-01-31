from __future__ import annotations

from typing import Generic

from fur_lib.core.basis import Basis
from fur_lib.core.typing import DotProduct, SystemObjectType


class System(Generic[SystemObjectType]):
    """
    Под системой понимаю множество элементов,
    где один из элементов этого множества раскладывается через элементы базиса
    """

    def __init__(self, basis: Basis[SystemObjectType], dot_product: DotProduct):
        self.basis = basis
        self.dot_product = dot_product

    def fourier_coefficient(self, obj: SystemObjectType, n: int, eps: float = 0.0001) -> int | float:
        base_obj = self.basis[n]
        a = self.dot_product(obj, base_obj)
        b = self.dot_product(base_obj, base_obj)

        # хз зчем я это добавлял. Может и правда нужно. Но один раз эта хуета испортила мне все, так что пока комменчу
        # if a < eps:
        #     logging.warning('Обнаружен МАЛЕНЬКИЙ ЧЛЕН ряда. Во избежание погрешностей он будет занулен')
        #     return 0

        return a / b

    def fourier_sum(self, obj: SystemObjectType, n: int) -> SystemObjectType:
        k = self.fourier_coefficient(obj, 0)
        summ = self.basis[0] * k
        for i in range(1, n):
            k = self.fourier_coefficient(obj, i)
            summ = summ + self.basis[i] * k
        return summ
