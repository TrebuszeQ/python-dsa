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
        self._degree = SinglePolynomialDict.__find_degree(poly_dct) if len(poly_dct) > 0 else 0
        poly_dct: dict[float, float] = self.sort_and_fill(poly_dct)
        self._constant_term = constant_term
        self._poly = poly_dct
        self._poly_str = self.__poly_to_string()
        self._y = None

    @staticmethod
    def __find_degree(dct):
        maxx = 0
        for key in dct.keys():
            if key > maxx:
                maxx = key

        return maxx

    def sort_and_fill(self, poly_dct: dict[float, float]):
        n = round(self._degree)
        result: dict[float: float] = dict()

        for i in range(n, 0, -1):
            j = i * 1.0
            result[j] = poly_dct[j] if j in poly_dct else 0.0

        return result

    def horner_method(self, x):
        a = self.sort_and_fill(self._poly)

        p = 0
        for value in a.values():
            p = p * x + value

        return p + self._constant_term

    def __poly_to_string(self):
        poly = self.poly
        poly_str = ""
        for key in poly.keys():
            num = "+" + str(key) if key >= 0 else "-" + str(key)
            coefficient = "+" + str(poly[key]) if poly[key] >= 0 else "-" + str(poly[key])

            poly_str += num + "^" + coefficient

        return poly_str + str(self._constant_term) if self._constant_term >= 0 else "-" + str(self._constant_term)

