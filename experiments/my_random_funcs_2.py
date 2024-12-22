from typing import Callable

from fur_lib.core.base import ClosedIntervalFunc, SinCosBasis, System
from fur_lib.core.non_ortogonal_system import NonOrthogonalBasis
from fur_lib.utils.interpolator import LinearInterpolator, Point

# Какие-то данные функции
a = [[1, 15, 0, 15, 15], [0, 1, 18, 5, 16], [2, 0, 20, 11, 31], [11, 14, 4, 10, 0], [18, 16, 0, 2, 0], [12, 5, 4, 8, 10], [2, 5, 18, 5, 16], [10, 13, 8, 3, 0], [11, 0, 12, 15, 0], [14, 7, 5, 16, 14], [17, 15, 8, 13, 0]]

funcs = []
for y_values in a:
    points = [Point(x, y) for x, y in enumerate(y_values)]
    funcs.append(LinearInterpolator(points))

study = funcs[1:]
check = funcs[:1]


class Func(ClosedIntervalFunc):
    def __init__(self, func: Callable, **kwargs):
        super().__init__(func, interval_start=0, interval_end=9.999)

    def __sub__(self, other):
        def _wrapper(*args):
            return self.func(*args) - other.func(*args)

        return Func(_wrapper)


class Basis(NonOrthogonalBasis):
    def stupid_get_item(self, n: int):
        return Func(study[n])


if __name__ == '__main__':
    system = System(Basis())
    func = Func(check[0])
    fs = system.fourier_sum(func, 5)

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, 4, 400)
    y = [func(xi) for xi in x]
    plt.plot(x, y, label=f'неповторимый оригинал')

    y2 = [fs(xi) for xi in x]
    plt.plot(x, y2, label=f'жалкая пародия')

    sincos_system = System(SinCosBasis(interval_start=0, interval_end=4))
    sincos_fs = sincos_system.fourier_sum(func, 1)

    # y3 = [sincos_fs(xi) for xi in x]
    # plt.plot(x, y3, label=f'вообще не то что нужно')

    # for i in range(5):
    #     basis_func = system.basis[i] * system.fourier_coefficient(func, i)
    #     basis_y = [basis_func(xi) for xi in x]
    #     plt.plot(x, basis_y, label=f'{i} - {system.fourier_coefficient(func, i)}')

    plt.legend()
    plt.show()


