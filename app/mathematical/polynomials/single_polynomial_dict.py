import math
from dataclasses import dataclass
from operator import itemgetter


@dataclass(repr=True)
class SinglePolynomialDict:
    @property
    def poly(self):
        return self._poly

    @property
    def degree(self):
        return self._degree

    @property
    def y(self):
        return self._y

    @property
    def poly_str(self):
        return self._poly_str

    @y.setter
    def y(self, x):
        p = 0
        print(self._poly)

        for key in self._poly.keys():
            p += math.pow(self._poly.get(key), key) * x

        self._y = p + self._constant_term

    @poly.setter
    def poly(self, arr: [[float]]):
        self._poly = arr

    def __init__(self, poly_dct: dict[float, float], constant_term: float):
        poly_dct: dict[float, float] = self.sort_and_fill(poly_dct)
        self._degree = self.__find_degree() if len(poly_dct) > 0 else 0
        self._constant_term = constant_term
        self._poly = poly_dct
        self._poly_str = SinglePolynomial.__poly_to_string(self)
        self._y = None

    def __find_degree(self):
        maxx = 0
        for key in self._poly.keys():
            if key > maxx:
                maxx = key

        return maxx

    def sort_and_fill(self, poly_dct: dict[float, float]):
        n = round(self._degree)
        result: dict[float: float] = dict()
        n -= 1

        for i in range(n):
            result[i] = poly_dct[i] if i in poly_dct else 0

        return result

    def horner_method(self, x):
        poly = self.poly
        n = round(self._degree) - 1
        p = None

        for i in range(n, 0, -1):
            if len(poly) < n or poly[i] is None:
                poly[n] = 0

            elif poly[n - 1] <= 0:
                poly[n - 1] = 0

            p = x * poly[i] + poly[i - 1]

        return p + self._constant_term

    def __poly_to_string(self):
        poly = self.poly
        poly_str = ""
        for key in poly.keys():
            num = "+" + str(key) if key >= 0 else "-" + str(key)
            coefficient = "+" + str(poly[key]) if poly[key] >= 0 else "-" + str(poly[key])

            poly_str += num + "^" + coefficient

        return poly_str + str(self._constant_term) if self._constant_term >= 0 else "-" + str(self._constant_term)

