import math


def horner_method(n: int, a: float, x: float):
    result: float = 0
    for i in range(n):
        result += a * math.pow(x, i)

    return result


