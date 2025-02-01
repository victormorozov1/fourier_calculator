from functools import partial
from math import *
from sys import argv

import matplotlib.pyplot as plt
from numpy import arange

from fur_lib.core.dot_product import integral_product
from fur_lib.core.func import Func
from fur_lib.core.non_ortogonal_system import NonOrthogonalBasis
from fur_lib.core.system import System


class MyBasis(NonOrthogonalBasis):
    ELEMENTS = [
        lambda x1: x1 ** 2,
        lambda x2: x2,
        lambda x3: -x3,
        lambda x4: x4 ** 3,
        lambda x5: 1 / max(x5, 1),
    ]

    def stupid_get_item(self, n: int) -> Func:
        return Func(self.ELEMENTS[n])


if __name__ == '__main__':
    start, end, expression = int(argv[1]), int(argv[2]), argv[3]
    if len(argv) > 4:
        harmonics_num = int(argv[4])
    else:
        harmonics_num = 4

    basis = MyBasis(dot_product=partial(integral_product, interval_start=start, interval_end=end))
    system = System(basis, partial(integral_product, interval_start=start, interval_end=end))
    func = eval(f'lambda x: {expression}')
    fs_sum = system.fourier_sum(func, harmonics_num)

    x = [float(i) for i in arange(start, end + 0.05, 0.01)]
    plt.plot(x, [func(i) for i in x], label=f'неповторимый оригинал')
    y = [fs_sum(xi) for xi in x]
    plt.plot(x, y, label=f'жалкая пародия')

    plt.legend()
    plt.show()
