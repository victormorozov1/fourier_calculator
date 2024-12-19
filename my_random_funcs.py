from math import floor

from base import ClosedIntervalFunc, System
from interpolator import LinearInterpolator, Point
from non_ortogonal_system import NonOrthogonalBasis

# Какие-то данные функции
a = [
    [981, 758, 5, 56, 6, 420, 957, 98, 5, 175],
    [589, 173, 7, 98, 4, 173, 458, 34, 8, 398],
    [198, 435, 3, 18, 7, 957, 431, 57, 4, 591],
    [918, 237, 2, 58, 9, 985, 771, 75, 8, 454],
    [319, 823, 8, 45, 4, 328, 497, 19, 8, 283],
    [919, 835, 9, 93, 2, 189, 657, 19, 8, 390],
    [894, 372, 8, 20, 7, 378, 947, 91, 4, 740],
    [943, 280, 8, 23, 4, 349, 872, 98, 7, 940],
    [983, 740, 7, 20, 3, 810, 270, 82, 7, 732],
    [473, 829, 1, 84, 8, 374, 809, 37, 1, 743],
    [748, 329, 8, 70, 9, 315, 980, 37, 9, 123],
    [473, 218, 3, 27, 1, 723, 198, 12, 3, 392],
    [758, 923, 7, 45, 1, 328, 917, 22, 7, 713],
    [557, 231, 8, 17, 1, 537, 215, 73, 2, 712],
    [875, 389, 9, 21, 8, 924, 789, 35, 9, 984],
    [913, 280, 3, 98, 7, 701, 589, 32, 9, 124],
    [901, 735, 2, 73, 7, 723, 849, 89, 4, 754],
    [714, 358, 8, 48, 1, 978, 945, 81, 4, 147],
    [897, 439, 9, 59, 8, 495, 143, 94, 5, 145],
    [489, 137, 8, 54, 5, 897, 549, 10, 7, 980],
]

funcs = []
for y_values in a:
    points = [Point(x, y) for x, y in enumerate(y_values)]
    funcs.append(LinearInterpolator(points))

study = funcs[::2]
check = funcs[1::2]


class Func(ClosedIntervalFunc):
    @property
    def interval_start(self) -> int | float:
        return 0

    @property
    def interval_end(self) -> int | float:
        return 9.999

    def __sub__(self, other):
        def _wrapper(*args):
            return self.func(*args) - other.func(*args)

        return Func(_wrapper)


class Basis(NonOrthogonalBasis):
    def stupid_get_item(self, n: int):
        return Func(study[n])


if __name__ == '__main__':
    system = System(Basis())
    for i, c in enumerate(check[:3]):
        func = Func(c)
        fs = system.fourier_sum(func, 6)

        import matplotlib.pyplot as plt
        import numpy as np

        x = np.linspace(0, 10, 400)
        y = [func(xi) for xi in x]
        plt.plot(x, y, label=f'неповторимый оригинал {i}')

        y2 = [fs(xi) for xi in x]
        plt.plot(x, y2, label=f'жалкая пародия {i}')

    plt.legend()
    plt.show()


