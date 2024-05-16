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
        self.__set_x_axis_limit()

    @y_arr.setter
    def y_arr(self, value):
        self._y_arr = value
        self.__set_y_axis_limit()

    def __init__(self):
        self._y_arr = None
        self._x_arr = None
        self._colors = ["brown", "teal", "red", "blue", "green", "cyan", "magenta", "orange", "pink", "purple"]
        self._ax = plt.gca()

    def __set_x_axis_limit(self):
        interval = max(self._x_arr) / (len(self._x_arr) - 1)
        self._ax.set_xlim([0, max(self._x_arr) + interval])

    def __set_y_axis_limit(self):
        max_len = len(str(max(self._y_arr)))
        rnd = round(max(self._y_arr), 1-max_len)
        self._ax.set_ylim([0, rnd])

    def make_scatter_plot(self, title, marker: str, size):
        color = self.get_random_color()

        plt.scatter(self._x_arr, self._y_arr, label="dots", color=color, marker=marker, s=size)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title(title)
        plt.legend()

        for x, y in zip(self._x_arr, self._y_arr):
            plt.text(x, y, " " + str(y).ljust(3, " "), color="black", fontsize=size / 1.75)

        plt.show()

    def get_random_color(self):
        num = random.randrange(0, len(self._colors) - 1, 1)
        return self._colors[num]

    def make_line_plot(self, title, marker, size):
        color = self.get_random_color()

        plt.plot(self._x_arr, self._y_arr, label="line", color=color, marker=marker, s=size)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title(title)
        plt.legend()
