import random
import matplotlib.pyplot as plt
from pygments.lexers import q


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
        self.__set_x_limit(value)

    @y_arr.setter
    def y_arr(self, value):
        self._y_arr = value
        self.__set_y_limit(value)

    def __init__(self):
        self._y_arr = None
        self._x_arr = None
        self._colors = ["brown", "teal", "red", "blue", "green", "cyan", "magenta", "orange", "pink", "purple"]
        self._ax = plt.gca()

    def __set_x_limit(self, x_arr):
        len_x = len(x_arr)
        maxx = x_arr[len_x - 1]
        interval_x = maxx / (len_x - 1)
        xlim = maxx + interval_x
        self._ax.set_xlim([0, xlim])

    def __set_y_limit(self, y_arr):
        len_y = len(y_arr)
        maxy = y_arr[len_y - 1]
        interval_y = maxy / (len_y - 1)
        ylim = maxy + interval_y
        self._ax.set_ylim([0, ylim])

    def make_scatter_plot(self, title, marker: str, size, values=True):
        color = self.get_random_color()

        plt.scatter(self._x_arr, self._y_arr, label="dots", color=color, marker=marker, s=size)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title(title)
        plt.legend()

        if values:
            for x, y in zip(self._x_arr, self._y_arr):
                plt.text(x, y, " " + str(y).ljust(3, " "), color="black", fontsize=size / 1.75)

        return plt

    def get_random_color(self):
        num = random.randrange(0, len(self._colors) - 1, 1)
        return self._colors[num]

    def make_line_plot(self, title, size, values=False):
        color = self.get_random_color()

        plt.plot(self._x_arr, self._y_arr, label="line", color=color)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title(title)
        plt.legend()

        if values:
            for x, y in zip(self._x_arr, self._y_arr):
                plt.text(x, y, " " + str(y).ljust(3, " "), color="black", fontsize=size / 1.75)

        return plt

    def _define_averages(self):
        pass

