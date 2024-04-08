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
    def corrected(self):
        return self._corrected

    @property
    def unbiased(self):
        return self._gamma

    def __init__(self, array: [float]):
        self._array = array
        self._degree = len(array)
        self._c4: dict[int: float] = c4_map()
        self._arithmetic_average = ArithmeticAverage(array)
        self._corrected = self.__sigma(array)
        self._gamma = self.__gamma()

    def __sigma(self, collection: [float]) -> float:
        n = self._degree
        sigma = 0
        aa = self._arithmetic_average.value

        for num in collection:
            sigma += (num - aa) * (num - aa)

        return math.sqrt(sigma/(n - 1.0))

    def __gamma(self) -> float:
        n = self._degree
        aa = self._arithmetic_average.value
        c4 = self._c4[n]

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

    def single_loop(self) -> float:
        n = self._degree
        s = 0
        sq_sum = 0

        for num in self._array:
            s += num
            sq_sum += num * num

        return sq_sum / (s * n)

    def bessel_correction_unbiased(self) -> float:
        n = self._degree
        s = 0
        sum_sq = 0

        for num in self._array:
            s += num
            sum_sq += num * num

        variance = (sum_sq - (s * s) / n) / (n - 1)
        return math.sqrt(variance)


