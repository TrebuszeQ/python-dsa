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
        for pair in self._poly:
            p += math.pow(pair[0] * x, pair[1])

        self._y = p

    @property
    def poly_str(self):
        return self._poly_str

    def __init__(self, poly_arr: [[float]]):
        self._poly = poly_arr
        self._poly = self.sort_poly()
        self._n = SinglePolynomial.__find_max_coefficient(self)
        self._poly_str = SinglePolynomial.__poly_to_string(self)
        self._y = None

    def sort_poly(self):
        sorted_poly: [[float]] = None * self.n

        i = self._n
        while i != 0:
            for pair in self._poly:
                if pair[1] == i and sorted_poly[i] is None:
                    sorted_poly[i] = pair

                elif pair[1] == 1 and sorted_poly[i] is not None:
                    sorted_poly[i] += pair[0]

            if sorted_poly[i] is None:
                sorted_poly[i] = [0, 0]

        return sorted_poly

    def horner_method(self, x):
        poly = self._poly
        n = self._n
        p = None
        while n != 1:
            p = x * poly[n][0] + poly[n - 1][0]

        return p

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

