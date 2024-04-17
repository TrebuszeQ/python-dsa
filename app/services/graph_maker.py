import math


class GraphMaker:
    @property
    def point_array(self):
        return self._points

    @property
    def max_y(self):
        return self._max_y

    @property
    def min_y(self):
        return self._min_y

    @property
    def max_x(self):
        return self._max_x

    def __init__(self, points: [[2]]):
        self._points = sorted(points)
        self._max_y = points[len(points) - 1][1]
        self._min_y = points[0][0]
        self._max_x = len(points) - 1

    def draw_y(self, degrees: int) -> None:
        ymax = round(self._max_y, -1)
        interval = ymax / (degrees - 1)
        print("y")

        ymax_int = int(ymax)
        indent = len(str(ymax_int)) + 2

        for i in range(degrees, 1, -1):
            ymax_int = int(ymax)
            print(f"{ymax_int}" + "|".rjust(indent))
            ymax -= interval

        print(f"  " + "0".rjust(indent))

    def draw_x(self, degrees: int) -> None:
        pass
    