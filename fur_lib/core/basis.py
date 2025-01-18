from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from fur_lib.core.system_object import SystemObject
from fur_lib.core.typing import SupportsGetItem

SystemObjectType = TypeVar('SystemObjectType', bound=SystemObject)


class Basis(Generic[SystemObjectType], ABC):
    """
    Под базисом понимаю множество элементов, по которым буду раскладывать элементы системы
    """
    @abstractmethod
    def __getitem__(self, item: int) -> SystemObjectType:
        pass
