from math import ceil, floor
import matplotlib.pyplot as plt
import numpy as np

from fur_lib.core.non_ortogonal_system import NonOrthogonalBasis
from fur_lib.core.sin_cos_basis import SinCosBasis
from fur_lib.core.system import System
from fur_lib.experimental_additions.simple_closed_interval_func import SimpleClosedIntervalFunc
from fur_lib.core.closed_interval_func import ClosedIntervalFunc


class OrtSinCosBasis(NonOrthogonalBasis, SinCosBasis):
    def stupid_get_item(self, n: int):
        return SinCosBasis.__getitem__(self, n)


def floor_ceil(x: float) -> tuple[int, int]:
    for l in range(floor(int(x) - 1), int(x) + 2):
        if l <= x <= l + 1:
            return l, l + 1


if __name__ == '__main__':
    start, end = 0, 4
    basis = OrtSinCosBasis(interval_start=start, interval_end=end, )
    basis2 = OrtSinCosBasis(interval_start=start, interval_end=end , sys_obj_type=SimpleClosedIntervalFunc)
    system = System(basis)
    system2 = System(basis2)
    lst = [1, 5, 3, 0, 9]

    def f(_x, eps=10**-5):
        l, r = floor_ceil(_x)
        if _x - l < eps:
            return lst[l]
        if r - _x < eps:
            return lst[r]
        return lst[l] * (r - _x) + lst[r] * (_x - l)


    func = ClosedIntervalFunc(f, interval_start=start, interval_end=end)
    func2 = SimpleClosedIntervalFunc(f, interval_start=start, interval_end=end)
    fs = system.fourier_sum(func, 4)
    fs2 = system2.fourier_sum(func2, 4)

    x = [float(i) for i in np.arange(start, end + 0.005, 0.01)]
    plt.plot(x, [f(xi) for xi in x], label=f'неповторимый оригинал')
    y = [fs(xi) for xi in x]
    plt.plot(x, y, label=f'жалкая пародия')
    y2 = [fs2(xi) for xi in x]
    plt.plot(x, y2, label=f'жалкая пародия')

    plt.legend()
    plt.show()
