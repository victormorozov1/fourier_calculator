from abc import ABC, abstractmethod
from typing import Generic

from fur_lib.core.typing import Basis, SystemObjectType


class NonOrthogonalBasis(Generic[SystemObjectType], Basis[SystemObjectType], ABC):
    """
    Для разложения в ряд Фурье есть необходимое условие - "ортогональный" (в смысле введенного произведения) базис
    Но не всегда удобно задавать ортогональную систему.

    С помощью этого класса можно собрать базис из неортогональных элементов,
    из которых будет собрана ортогональная система
    """

    @staticmethod
    def projection(obj1: SystemObjectType, obj2: SystemObjectType):
        return (obj1 * obj2) / (obj2 * obj2)

    @classmethod
    def exclude(cls, obj: SystemObjectType, obj_to_exclude: SystemObjectType) -> SystemObjectType:
        exclude_k = cls.projection(obj, obj_to_exclude)
        return obj + obj_to_exclude * -exclude_k

    @abstractmethod
    def stupid_get_item(self, n: int) -> SystemObjectType:
        pass

    def __getitem__(self, n: int):
        el = self.stupid_get_item(n)
        for i in range(n):
            el = self.exclude(el, self[i])
        return el
