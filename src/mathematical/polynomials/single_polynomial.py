import math
from dataclasses import dataclass


@dataclass(repr=True)
class SinglePolynomial:

    @property
    def n(self):
        return self._n

    @property
    def y(self):
        return self._y

    @property
    def poly(self):
        return self._poly

    def __init__(self, polynomial: {float: float}):
        self._poly = polynomial
        self._n = self._set_max_coefficient()
        self._y = self._horner_method()

    def _set_max_coefficient(self):
        max = 0

        for coefficient in self._poly.values():
            if coefficient > max:
                max = coefficient

        return max

    # here
    def _horner_method(self):
        result = 0
        for poly in self._poly:
            print(self._poly[poly])
            result += math.pow(self._poly[poly], poly.coefficient)

        return result
