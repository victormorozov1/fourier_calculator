from fur_lib.utils.utils import x_translator


def test_x_translator():
    translator = x_translator(-2, 2, 0, 8)
    assert translator(0) == -2
    assert translator(4) == 0
    assert translator(6) == 1
    assert translator(8) == 2
