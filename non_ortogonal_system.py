from base import BaseSystem, SystemObjectType
from typing import Generic
from abc import ABC, abstractmethod


class NonOrthogonalSystem(Generic[SystemObjectType], BaseSystem[SystemObjectType], ABC):
    @staticmethod
    def projection(obj1: SystemObjectType, obj2: SystemObjectType):
        return (obj1 * obj2) / (obj2 * obj2)

    @classmethod
    def exclude(cls, obj: SystemObjectType, obj_to_exclude: SystemObjectType) -> SystemObjectType:
        exclude_k = cls.projection(obj, obj_to_exclude)
        return obj - obj_to_exclude * exclude_k

    @abstractmethod
    def stupid_get_item(self, n: int) -> SystemObjectType:
        pass

    def __getitem__(self, n: int):
        el = self.stupid_get_item(n)
        for i in range(n):
            el = self.exclude(el, self[i])
        return el
