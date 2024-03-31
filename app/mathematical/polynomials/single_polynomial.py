import math
from dataclasses import dataclass


@dataclass(repr=True)
class SinglePolynomial:
    def degree(self):
        return self._degree


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
    def poly(self):
        return self._poly

    @poly.setter
    def poly(self, arr: [[float]]):
        self._poly = SinglePolynomial.__sort_poly(self._degree, arr)

    @property
    def poly_str(self):
        return self._poly_str

    def __init__(self, poly_arr: [[float]]):
        self._degree = SinglePolynomial.__find_max_coefficient(poly_arr)
        self._poly = SinglePolynomial.__sort_poly(self._degree, poly_arr)
        self._poly_str = SinglePolynomial.__poly_to_string(self)
        self._y = None

    @staticmethod
    def __sort_poly(degree: float, arr: [[float]]):

        return sorted(arr)

    def horner_method(self, x):
        poly = self._poly
        n = self._degree
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

    @staticmethod
    def __find_max_coefficient(arr: [[float]]):
        maxx = 0
        for pair in arr:
            coefficient = pair[1]
            if coefficient > maxx:
                maxx = coefficient

        return maxx

