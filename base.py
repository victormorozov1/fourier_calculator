from abc import ABC, abstractmethod
from math import sqrt, pi, sin, cos
from scipy.integrate import quad
from typing import Generic, TypeVar

""" 
Под системой считаю множество элементов, 
где один из элементов этого множества буду пытаться разложить через базовые элементы
"""

"""
Под базовой системой считаю множество элементов,
по которым буду раскладывать элементы системы
"""


class SystemObject(ABC):
    """ Класс элемента системы"""

    @abstractmethod
    def __mul__(self, other) -> int | float:
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    def norm(self):
        # По умолчанию норма будет выводится из произведения, но при желании ее можно определить как угодно
        return sqrt(self * self)


SystemObjectType = TypeVar('SystemObjectType', bound=SystemObject)


class BaseSystem(Generic[SystemObjectType], ABC):
    @abstractmethod
    def __getitem__(self, n: int) -> SystemObjectType:
        pass


class System(Generic[SystemObjectType]):
    def __init__(self, base_system: BaseSystem[SystemObjectType] | list):
        self.base_system = base_system

    def fourier_coefficient(self, obj: SystemObjectType, n: int) -> int | float:
        base_obj = self.base_system[n]
        return (obj * base_obj) / (base_obj * base_obj)

    def fourier_sum(self, obj: SystemObjectType, n: int) -> SystemObjectType:
        summ = self.base_system[0] * self.fourier_coefficient(obj, 0)
        for i in range(1, n):
            summ = summ + self.base_system[i] * self.fourier_coefficient(obj, i)
        return summ


class ClosedIntervalFunc(SystemObject, ABC):
    @property
    @abstractmethod
    def interval_start(self) -> int | float:
        pass

    @property
    @abstractmethod
    def interval_end(self) -> int | float:
        pass

    @staticmethod
    def multed_func(f1, f2):
        def _wrapper(*args):
            return f1(*args) * f2(*args)
        return _wrapper

    def __init__(self, func):
        self.func = func

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            def _wrapper(*args):
                return self.func(*args) * other
            return self.__class__(_wrapper)
        return quad(self.multed_func(self.func, other.func), self.interval_start, self.interval_end)[0]

    def __add__(self, other):
        def _wrapper(*args):
            return self.func + other.func
        return self.__class__(_wrapper)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class PIClosedIntervalFunc(ClosedIntervalFunc):
    @property
    def interval_start(self) -> int | float:
        return -pi

    @property
    def interval_end(self) -> int | float:
        return pi


class SinCosBaseSystem(BaseSystem[PIClosedIntervalFunc]):
    def __getitem__(self, n: int) -> SystemObjectType:
        # 0: cos(0x) = 1
        # 1: sin(x)
        # 2: cos(x)
        # 3: sin(2x)
        k = (n + 1) // 2
        if n % 2 == 0:
            return PIClosedIntervalFunc(lambda x: cos(k * x))
        return PIClosedIntervalFunc(lambda x: sin(k * x))


if __name__ == '__main__':
    system = System(SinCosBaseSystem())
    func = PIClosedIntervalFunc(lambda x: x ** 2 - x ** 4 / 9 + 3 + x)
    for i in range(10):
        print(system.fourier_coefficient(func, i))
