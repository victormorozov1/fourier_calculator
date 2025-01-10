from __future__ import annotations

from math import pi, sin, cos

from fur_lib.core.closed_interval_func import ClosedIntervalFunc
from fur_lib.core.typing import Basis, SystemObjectType
from fur_lib.utils.utils import x_translator


class SinCosBasis(Basis[ClosedIntervalFunc]):
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
            return ClosedIntervalFunc(
                lambda x: cos(k * translator(x)), interval_start=self.interval_start, interval_end=self.interval_end,
            )
        return ClosedIntervalFunc(
            lambda x: sin(k * translator(x)), interval_start=self.interval_start, interval_end=self.interval_end,
        )
