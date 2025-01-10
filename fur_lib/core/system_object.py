from abc import ABC, abstractmethod
from math import sqrt


class SystemObject(ABC):
    """ Класс элемента системы"""

    @abstractmethod
    def __mul__(self, other) -> int | float:
        pass

    @abstractmethod
    def __add__(self, other):
        pass
