from dataclasses import dataclass
from app.mathematical.statistics.arithmetic_average import ArithmeticAverage


@dataclass(repr=True)
class StandardDeviation:
    @property
    def degree(self):
        return self._degree

    @property
    def value(self):
        return self._estimator

    @property
    def arithmetic_average(self):
        return self._arithmetic_average

    def __init__(self, collection: [float]):
        self._degree = len(collection)
        self._arithmetic_average = ArithmeticAverage(collection)
        self._estimator = self.__sigma_task(collection)

    def __gamma(self, collection: [float]) -> float:
        n = self._degree
        g = 0

        for pair in collection:
            # arithmetic average of quads of probe
            x1 = ArithmeticAverage(collection)
            # quad of arithmetic average
            x2 = ArithmeticAverage(collection).value ** 2

            g = ((n * ()) / (n - 1)) ** (1 / 2)

    def __sigma_task(self, collection: [float]) -> float:
        n = self._degree
        ex = self._arithmetic_average.value
        s = 0

        for num in collection:
            s += ((num - ex) ** 2)

        return ((1 / (n - 1)) * s) ** 1/2
