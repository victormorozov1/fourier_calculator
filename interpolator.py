from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Point:
    x: int | float
    y: int | float


class BaseInterpolator(ABC):
    def __init__(self, data: list[Point]):
        self.data = data

    @abstractmethod
    def get_intermediate_value(self, left_point: Point, right_point: Point, x: int | float) -> int | float:
        pass

    def __call__(self, x: int | float):
        if x <= self.data[0].x:
            return self.data[0].y

        if x >= self.data[-1].x:
            return self.data[-1].y

        l, r = 0, len(self.data)
        while r - l > 1:
            m = (l + r) // 2
            if self.data[m].x > x:
                r = m
            else:
                l = m

        if self.data[l].x == x:
            return self.data[l].y
        return self.get_intermediate_value(self.data[l], self.data[r], x)


class LinearInterpolator(BaseInterpolator):
    def get_intermediate_value(self, left_point: Point, right_point: Point, x: int | float) -> int | float:
        return left_point.y + (right_point.y - left_point.y) * (x - left_point.x) / (right_point.x - left_point.x)
