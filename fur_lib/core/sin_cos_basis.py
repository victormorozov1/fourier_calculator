from math import pi, sin, cos

from fur_lib.core.basis import Basis, SystemObjectType
from fur_lib.core.func import Func
from fur_lib.utils.utils import x_translator


class SinCosBasis(Basis):
    def __init__(self, interval_start: int | float = -pi, interval_end: int | float = pi):
        self.interval_start = interval_start
        self.interval_end = interval_end

    def __getitem__(self, n: int) -> SystemObjectType:
        # 0: cos(0x) = 1
        # 1: sin(x)
        # 2: cos(x)
        # 3: sin(2x)
        k = (n + 1) // 2
        translator = x_translator(-pi, pi, self.interval_start, self.interval_end)
        if n % 2 == 0:
            return Func(lambda x: cos(k * translator(x)), name=f'cos({k}x)')
        return Func(lambda x: sin(k * translator(x)), name=f'sin({k}x)')
