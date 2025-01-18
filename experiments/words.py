from typing import Callable

from fur_lib.core.closed_interval_func import ClosedIntervalFunc
from fur_lib.core.non_ortogonal_system import NonOrthogonalBasis
from fur_lib.core.rounding_system import RoundingSystem
from fur_lib.core.system import System
from fur_lib.utils.interpolator import LinearInterpolator, Point


def letter_to_num(c: str) -> int:
    return ord(c) - ord('а')


def num_to_letter(n: int | float) -> str:
    return chr(round(n) + ord('а'))


def word_to_array(word: str) -> list[int]:
    return [letter_to_num(c) for c in word]


words_basis = [
    'актер',
    'вафля',
    'лодка',
    'трава',
    'медик',
    'ветер',
    'книга',
    'лампа',
    'озеро',
    'спина',
]

words_num_basis = [word_to_array(word) for word in words_basis]


def get_func(arr: list[int]) -> Callable:
    points = [Point(x, y) for x, y in enumerate(arr)]
    return LinearInterpolator(points)


funcs = []
for y_values in words_num_basis:
    funcs.append(get_func(y_values))


class Func(ClosedIntervalFunc):
    def __init__(self, func: Callable, **kwargs):
        super().__init__(func, interval_start=0, interval_end=4)

    def __sub__(self, other):
        def _wrapper(*args):
            return self.func(*args) - other.func(*args)

        return Func(_wrapper)


class Basis(NonOrthogonalBasis):
    def stupid_get_item(self, n: int):
        return Func(funcs[n])


system = RoundingSystem(2, Basis())
func = Func(get_func(word_to_array('йцуке')))
fs = system.fourier_sum(func, 5)

for i in range(5):
    k = fs(i)
    print(num_to_letter(k), k, system.fourier_coefficient(func, i))
