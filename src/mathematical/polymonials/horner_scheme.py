import math


def horner_scheme(n: int, a: float, x: float):
    sigma: float = 0
    for i in range(n - 1):
        sigma += a * math.pow(x, i)

    return sigma