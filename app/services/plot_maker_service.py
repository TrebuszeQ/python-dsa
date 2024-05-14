import random
import matplotlib.pyplot as plt
from pygments.lexers import q


class PlotMakerService:
    @property
    def colors(self):
        return self._colors

    @property
    def x_arr(self):
        return self._x_arr

    @property
    def y_arr(self):
        return self._y_arr

    def __init__(self, x_arr: [], y_arr: []):
        self._colors = ["brown", "teal", "red", "blue", "green", "cyan", "magenta", "orange", "pink", "purple"]
        self._x_arr = x_arr
        self._y_arr = y_arr
        self._ax = plt.gca()
        self.__x_limit = None
        self.__set_x_axis_limit()
        self.__y_limit = None
        self.__set_y_axis_limit()

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