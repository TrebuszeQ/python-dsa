import math
from dataclasses import dataclass
from app.mathematical.statistics.arithmetic_average import ArithmeticAverage
from app.mathematical.statistics.c4_map import c4_map


@dataclass(repr=True)
class StandardDeviation:
    @property
    def degree(self):
        return self._degree

    @property
    def value(self):
        return self._gamma

    @property
    def arithmetic_average(self):
        return self._arithmetic_average

    @property
    def c4(self) -> dict[int: float]:
        return self._c4

    @property
    def sigma(self):
        return self._sigma

    @property
    def gamma(self):
        return self._gamma

    def __init__(self, collection: [float]):
        self._degree = len(collection)
        self._c4: dict[int: float] = c4_map()
        self._arithmetic_average = ArithmeticAverage(collection)
        self._gamma = self.__gamma()

    def __sigma(self, collection: [float]) -> float:
        n = self._degree
        sigma = 0
        aa = self._arithmetic_average.value

        for num in collection:
            sigma += (num - aa) ** 2

        return sigma/(n - 1.0)

    def __gamma(self) -> float:
        n = self._degree
        aa = self._arithmetic_average.value
        c4 = self._c4[n]
        gamma = 0

        if 1 < n <= 75:
            gamma = aa / c4

        elif n < 200:
            gamma = aa / c4

        elif n <= 1000:
            gamma = aa / c4

        elif n <= 10000:
            gamma = aa / c4

        else:
            gamma = aa

        return gamma

    def single_algorithm(self, collection: [float]) -> float:
        n = self._degree
        s = 0
        sq_sum = 0

        for num in collection:
            s += num
            sq_sum += num * num

        return (sq_sum - (n - 1)) / (s * n)

