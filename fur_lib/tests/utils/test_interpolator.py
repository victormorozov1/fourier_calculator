import pytest

from fur_lib.utils.interpolator import LinearInterpolator, Point


@pytest.mark.parametrize(
    ('x', 'expected_y'),
    (
            (-100, 4),
            (1, 4),
            (2, 4),
            (3, 4),
            (4, 7),
            (6, 9),
            (7, 8),
            (8, 7),
            (9, 7),
    )
)
def test_linear_interpolator(x, expected_y):
    lin_int = LinearInterpolator([Point(1, 4), Point(3, 4), Point(5, 10), Point(8, 7)])
    assert lin_int(x) == expected_y
