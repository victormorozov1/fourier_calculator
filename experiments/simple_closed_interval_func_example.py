import matplotlib.pyplot as plt
import numpy as np

from fur_lib.core.non_ortogonal_system import NonOrthogonalBasis
from fur_lib.core.sin_cos_basis import SinCosBasis
from fur_lib.core.system import System
from fur_lib.experimental_additions.simple_closed_interval_func import SimpleClosedIntervalFunc


class OrtSinCosBasis(NonOrthogonalBasis, SinCosBasis):
    def stupid_get_item(self, n: int):
        return SinCosBasis.__getitem__(self, n)


if __name__ == '__main__':
    start, end = -2, 2
    basis = OrtSinCosBasis(interval_start=start, interval_end=end, sys_obj_type=SimpleClosedIntervalFunc)
    system = System(basis)
    f = lambda _x: _x ** 3 + 1
    func = SimpleClosedIntervalFunc(f, interval_start=start, interval_end=end)
    fs = system.fourier_sum(func, 4)

    x = [float(i) for i in np.arange(start, end + 0.005, 0.01)]
    plt.plot(x, [f(xi) for xi in x], label=f'неповторимый оригинал')

    y2 = [fs(xi) for xi in x]
    plt.plot(x, y2, label=f'жалкая пародия')

    plt.legend()
    plt.show()
