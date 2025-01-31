from abc import ABC, abstractmethod
from typing import Generic

from fur_lib.core.typing import SystemObjectType


class Basis(Generic[SystemObjectType], ABC):
    """
    Под базисом понимаю множество элементов, по которым буду раскладывать элементы системы
    """
    @abstractmethod
    def __getitem__(self, item: int) -> SystemObjectType:
        pass
