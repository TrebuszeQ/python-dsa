import random
import matplotlib.pyplot as plt


class PlotMaker:
    _colors = ["brown", "teal", "red", "blue", "green", "cyan", "magenta", "orange", "pink", "purple"]

    @property
    def colors(self):
        return self._colors

    @property
    def x_arr(self):
        return self._x_arr

    @property
    def y_arr(self):
        return self._y_arr

    @colors.setter
    def colors(self, value):
        self._colors = value

    @x_arr.setter
    def x_arr(self, value):
        self._x_arr = value

    @y_arr.setter
    def y_arr(self, value):
        self._y_arr = value

    def __init__(self):
        self._y_arr = None
        self._x_arr = None
        self._colors = ["brown", "teal", "red", "blue", "green", "cyan", "magenta", "orange", "pink", "purple"]

    def __compute_x_limit(self, x_arr):
        len_x = len(x_arr)
        maxx = x_arr[len_x - 1]
        interval_x = maxx / (len_x - 1)
        xlim = maxx + interval_x
        return xlim

    def __compute_y_limit(self, y_arr):
        len_y = len(y_arr)
        maxy = y_arr[len_y - 1]
        interval_y = maxy / (len_y - 1)
        ylim = maxy + interval_y
        return ylim

    def make_single_scatter_plot(self, title, marker: str, size, values=True):
        color = self.get_random_color()

        plt.scatter(self._x_arr, self._y_arr, label="dots", color=color, marker=marker, s=size)

        self._finish_single_plot(title, size, values)

        return plt

    def _finish_single_plot(self, title, size, values):
        plt.grid()
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title(title)
        plt.legend()

        if values:
            for x, y in zip(self._x_arr, self._y_arr):
                plt.text(x, y, " " + str(y).ljust(3, " "), color="black", fontsize=size / 1.75)

        xlim = self.__compute_x_limit(self._x_arr)
        ylim = self.__compute_y_limit(self._y_arr)
        # fig = plt.figure()
        # ax = fig.add_subplot()
        # ax.plot()
        # ax.set_xlim(xlim)
        plt.xlim(xmin=0, xmax=xlim)
        plt.ylim(xmin=0, xmax=ylim)

    def get_random_color(self):
        num = random.randrange(0, len(self._colors) - 1, 1)
        return self._colors[num]

    def make_single_line_plot(self, title, size, values=False):
        color = self.get_random_color()

        plt.plot(self._x_arr, self._y_arr, label="line", color=color)
        self._finish_single_plot(title, size, values)

        return plt
