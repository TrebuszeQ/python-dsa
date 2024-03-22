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

    @y.setter
    def y(self, x):
        p = 0
        print(self._poly)
        for key in self._poly:
            p += x * math.pow(key, self._poly[key])

        self._y = p

    @property
    def poly(self):
        return self._poly

    @poly.setter
    def poly(self, poly):
        self._poly = poly

    # here
    @property
    def poly_str(self):
        return self.poly.__str__(self.poly)

    def __init__(self, polynomial: {float: float}):
        self._poly = polynomial
        self._n = self._set_max_coefficient()
        self._y = None

    def _set_max_coefficient(self):
        maxx = 0

        for coefficient in self._poly.values():
            if coefficient > maxx:
                maxx = coefficient

        return maxx

    # P = a0
    # P = Px + ai, i = 1 ... n
    # here2
    def _horner_method(self, x0, i):
        if i != self.n:
            print(self._poly[i])
            self._poly = self._poly * x0 + self._poly[i]

        return self._horner_method(x0, i + 1)


