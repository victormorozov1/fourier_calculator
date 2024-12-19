def x_translator(original_start: int | float, original_end: int | float, new_start, new_end):
    """
    Иногда функцию нужно "натянуть" на другой отрезок.
    Например синусы и косинусы рассматриваются на отрезке от [-pi, pi], но что если мы захотим придставлять через
    сумму Фурье синусов и косинусов функцию на отрезке от [0, 10]?
    """
    def _wrapper(x: int) -> int:
        k = (x - new_start) / (new_end - new_start)
        return original_start + (original_end - original_start) * k

    return _wrapper
