import math
from dataclasses import dataclass
from operator import itemgetter


@dataclass(repr=True)
class SinglePolynomial:
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
        for pair in self._poly:
            p += math.pow(pair[0] * x, pair[1])

        self._y = p + self._constant_term

    @poly.setter
    def poly(self, arr: [[float]]):
        self._poly = arr

    def __init__(self, poly_arr: [[float]], constant_term: float):
        poly_arr = sorted(poly_arr, key=itemgetter(1), reverse=True)
        self._degree = poly_arr[0][1] if len(poly_arr) > 0 else 0
        self._constant_term = constant_term
        self._poly = poly_arr
        self._poly_str = SinglePolynomial.__poly_to_string(self)
        self._y = None

    def sort_and_fill(self):
        n = round(self._degree)
        result = [[0.0, 0.0] * n]
        n -= 1

        for i in range(n):
            for pair in self._poly:
                if pair[1] == i:
                    result.append(pair)

    def __fill_gaps(self):
        n = round(self._degree)
        result: [[float]] = [[0.0, 0.0]] * n

        k = 0

        for i in range(n, 0, -1):
            j = i * 1.0

            for pair in self._poly:
                if pair[1] == j and result[k] == [0.0, 0.0]:
                    result[k] = pair

                elif pair[1] == j and result[k] != [0.0, 0.0]:
                    result[k][0] += pair[0]

                elif pair[1] != j and result[k] == [0.0, 0.0]:
                    result[k] = [0.0, j]

            k += 1

        return result

    def horner_method(self, x):
        poly = self.__fill_gaps()
        n = round(self._degree)
        p = 0

        for i in range(n):
            term = poly[i][0]
            p = p * x + term

        return p * x + self._constant_term

    def __poly_to_string(self):
        poly = ""
        for pair in self._poly:
            num = "+" + str(pair[0]) if pair[0] >= 0 else "-" + str(pair[0])
            coefficient = "+" + str(pair[1]) if pair[1] >= 0 else "-" + str(pair[1])

            poly += num + "^" + coefficient

        return poly + str(self._constant_term) if self._constant_term >= 0 else "-" + str(self._constant_term)

