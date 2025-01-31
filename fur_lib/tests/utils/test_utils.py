from fur_lib.utils.utils import x_translator


def test_x_translator():
    translator = x_translator(-2, 2, 10, 22)
    assert translator(10) == -2
    assert translator(16) == 0
    assert translator(19) == 1
    assert translator(22) == 2
