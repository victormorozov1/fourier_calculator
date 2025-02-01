from functools import partial
from sys import argv

import matplotlib.pyplot as plt
from numpy import arange

from fur_lib.core.dot_product import integral_product
from fur_lib.core.sin_cos_basis import SinCosBasis
from fur_lib.core.system import System


if __name__ == '__main__':
    start, end, expression = int(argv[1]), int(argv[2]), argv[3]
    if len(argv) > 4:
        harmonics_num = int(argv[4])
    else:
        harmonics_num = 4
    basis = SinCosBasis(interval_start=start, interval_end=end)
    system = System(basis, partial(integral_product, interval_start=start, interval_end=end))
    func = eval(f'lambda x: {expression}')
    fs_sum = system.fourier_sum(func, harmonics_num)

    x = [float(i) for i in arange(start, end + 0.05, 0.01)]
    plt.plot(x, [func(i) for i in x], label=f'неповторимый оригинал')
    y = [fs_sum(xi) for xi in x]
    plt.plot(x, y, label=f'жалкая пародия')
    plt.show()
