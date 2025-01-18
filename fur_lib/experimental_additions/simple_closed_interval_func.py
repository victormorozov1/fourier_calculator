import numpy as np
from fur_lib.core.closed_interval_func import ClosedIntervalFunc
from fur_lib.utils.callable_math_operations import callable_number_mul


# TODO: придумать нормальное название
class SimpleClosedIntervalFunc(ClosedIntervalFunc):
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return super().__mul__(other)

        x = list(np.arange(self.interval_start, self.interval_end, 1))
        vec_1 = [self(i) for i in x]
        vec_2 = [other(i) for i in x]
        return sum(a * b for a, b in zip(vec_1, vec_2))
