from fur_lib.core.system import System
from fur_lib.core.typing import SystemObjectType


class RoundingSystem(System):
    def __init__(self, round_order: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.round_order = round_order

    def fourier_coefficient(self, obj: SystemObjectType, n: int) -> int | float:
        k = super().fourier_coefficient(obj, n)
        # left, right = k // 2 * 2, k // 2 * 2 + 2
        # if k - left < right - k:
        #     return left
        # return ri
        return round(k, self.round_order)
