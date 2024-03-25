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
    def solve(self):
        return self._poly

    @solve.setter
    def solve(self, poly):
        self._poly = poly

    # here
    @property
    def poly_str(self):
        return self.solve.__str__(self.solve)

    def __init__(self, polynomial):
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
    def _horner_method(self, px, n, a):
        for i in range(self.n):
            px = self._poly.solve(a)
            p = px + a


        return self._horner_method(x0, i + 1)


