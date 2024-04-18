from dataclasses import dataclass
from app.services.plot_maker_util import PlotMakerService


@dataclass(repr=True)
class Ota:

    @property
    def degree(self):
        return self._degree

    @property
    def binary_degree(self):
        return self._binary_degree

    @property
    def points_arr(self):
        return self._points_arr

    @property
    def y_arr(self):
        return self._y_arr

    @property
    def x_arr(self):
        return self._x_arr

    @property
    def c_array(self):
        return self._c_arr

    @property
    def binary_array(self):
        return self._bin_arr

    def __init__(self, arr: list[int]):
        self._points_arr = None
        self._degree = len(arr)
        self._binary_degree = len(bin(self._degree - 1)[2:])
        self._c_arr = []
        self._set_c_arr(arr)
        self._bin_arr = []
        self._set_bin_arr()
        self._points_arr = []
        self._x_arr = []
        self._y_arr = []
        self._set_points_arr()
        self._plot_maker_service = PlotMakerService(self._x_arr, self._y_arr)

    def _set_points_arr(self):
        c = self._c_arr

        for i in range(self._degree):
            sigma = 0
            a = self._bin_arr[i]
            sigma += c[0]
            sigma += c[1] * a[2]
            sigma += (c[1] + c[2]) * a[1]
            sigma += (c[3] - c[1]) * a[1] * a[2]
            sigma += (c[1] + c[2] + c[3] + c[4]) * a[0]
            sigma += (c[5] - c[1]) * a[0] * a[2]
            sigma += (c[6] + c[5] - c[2] - c[1]) * a[0] * a[1]
            sigma += (c[7] - c[5] - c[3] + c[1]) * a[0] * a[1] * a[2]

            result = [i, sigma]
            self._points_arr.append(result)
            self._y_arr.append(sigma)
            self._x_arr.append(i)

    def _set_c_arr(self, arr: list[int]):
        c_arr = self._c_arr = []

        for i in range(self.degree):
            val = arr[i] if i == 0 else (arr[i] - arr[i - 1])
            c_arr.append(val)

    def _set_bin_arr(self):
        for i in range(self._degree):
            bit = self.__to_bin(i)
            self._bin_arr.append([int(bit[i]) for i in range(self._binary_degree)])

    def __to_bin(self, num: int):
        return format(num, f"0{self._binary_degree}b")

    def show_plot(self):
        self._plot_maker_service.make_scatter_plot("Plot of Ota function", 'o', 20)
