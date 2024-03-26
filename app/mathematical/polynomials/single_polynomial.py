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
    def solve(self):
        return self._poly

    @y.setter
    def y(self, x):
        p = 0
        print(self._poly)
        for pair in self._poly:
            p += math.pow(pair[0] * x, pair[1])

        self._y = p

    @property
    def poly_str(self):
        return self._poly_str

    def __init__(self, poly_arr: [float]):
        self._poly = poly_arr
        self._y = None
        self._poly_str = self.__poly_to_string()
        self._n = self.__find_max_coefficient()

    # P = a0
    # P = Px + ai, i = 1 ... n
    # here2
    def horner_method(self, px, a, i, x):
        self._poly[i][0] * x + self._poly[i + 1][1]
        p = p * x +

        return self._horner_method(x0, i + 1)

    def __poly_to_string(self):
        poly = ""
        for pair in self._poly:
            num = "+" + str(pair[0]) if pair[0] >= 0 else "-" + str(pair[0])
            coefficient = "+" + str(pair[1]) if pair[1] >= 0 else "-" + str(pair[1])

            poly += num + "^" + coefficient

        return poly

    def __find_max_coefficient(self):
        maxx = 0
        for pair in self._poly:
            coefficient = pair[1]
            if coefficient > self.n:
                maxx = coefficient

        return maxx
