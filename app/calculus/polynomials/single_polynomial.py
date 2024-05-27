import math
from dataclasses import dataclass
from operator import itemgetter

from app.services.plot_maker_service import PlotMaker


@dataclass(repr=True)
class SinglePolynomial:
    @property
    def poly(self):
        return self._poly

    @property
    def degree(self):
        return self._degree

    @property
    def value(self):
        return self._value

    @property
    def poly_str(self):
        return self.__poly_to_string

    @value.setter
    def value(self, x):
        p = 0
        print(self._poly)
        for pair in self._poly:
            p += math.pow(pair[0] * x, pair[1])

        self._value = p

    @poly.setter
    def poly(self, arr: [[float]]):
        self._poly = arr

    def __init__(self, x_points: [float], y_points: [float]):
        poly_arr = [[y, x] for y, x in zip(y_points, x_points)]
        poly_arr = sorted(poly_arr, key=itemgetter(1), reverse=True)
        self._degree = poly_arr[0][1] if len(poly_arr) > 0 else 0
        self._poly = poly_arr
        self._value = None
        self._plot_maker = PlotMaker()
        self._plot_maker.x_arr = x_points
        self._plot_maker.y_arr = y_points

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

        return p * x

    # wrong
    def __poly_to_string(self):
        poly_str = ""
        for pair in self._poly:
            num = str(pair[0]) if pair[0] >= 0 else "-" + str(pair[0])
            coefficient = str(pair[1]) if pair[1] >= 0 else "-" + str(pair[1])

            poly_str += num + "^" + coefficient

        return poly_str

    def scatter_plot(self, marker, size, points_on_plot: bool):
        return self._plot_maker.make_scatter_plot("Single Polynomial Scatter Plot", marker, size, values=points_on_plot).plot

    def line_plot(self, size, points_on_plot: bool):
        return self._plot_maker.make_line_plot("Single Polynomial Line Plot", size, values=points_on_plot).plot
