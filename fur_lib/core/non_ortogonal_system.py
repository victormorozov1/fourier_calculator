import logging
from abc import ABC, abstractmethod
from typing import Callable

from fur_lib.core.basis import Basis, SystemObjectType
from fur_lib.core.typing import DotProduct


class NonOrthogonalBasis(Basis, ABC):
    """
    Для разложения в ряд Фурье есть необходимое условие - "ортогональный" (в смысле введенного произведения) базис
    Но не всегда удобно задавать ортогональную систему.

    С помощью этого класса можно собрать базис из неортогональных элементов,
    из которых будет собрана ортогональная система
    """

    def __init__(
            self,
            *args,
            eps: float = 10 ** -5,
            max_shift_len: int = 20 ** 2,
            dot_product: DotProduct,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._basis = []
        self._shift = 0
        self._eps = eps
        self._max_shift_len = max_shift_len
        self.dot_product = dot_product

    def projection(self, obj1: SystemObjectType, obj2: SystemObjectType):
        return self.dot_product(obj1, obj2) / self.dot_product(obj2, obj2)

    def exclude(self, obj: SystemObjectType, obj_to_exclude: SystemObjectType) -> SystemObjectType:
        exclude_k = self.projection(obj, obj_to_exclude)
        return obj + obj_to_exclude * -exclude_k

    @abstractmethod
    def stupid_get_item(self, n: int) -> SystemObjectType:
        pass

    def __getitem__(self, n: int):
        while_iterations = 0
        while len(self._basis) <= n:

            while_iterations += 1
            if while_iterations > 1000 and while_iterations % 1000 == 0:
                logging.warning(f'При получении {n}-ного элемента базиса уже {while_iterations} элементов занулилось')

            el = self.stupid_get_item(len(self._basis) + self._shift)
            for basis_el in self._basis:
                el = self.exclude(el, basis_el)

            # Околонулевые элементы могут создавать сильную погрешность при вычислениях, поэтому их не берем
            p = self.dot_product(el, el)
            if p > self._eps:
                self._basis.append(el)
            else:
                self._shift += 1
                logging.warning(f'element {el} excluded from basis, {p}')

        return self._basis[n]
