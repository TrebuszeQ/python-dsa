from app.services.plot_maker_service import PlotMaker
from app.sortings.algebraic_sort import algebraic_sort
from app.discrete.ota import Ota
import unittest


class AlgebraicSortCase(unittest.TestCase):

    def test_algebraic_sort_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        ota = Ota(lis)
        bin_arr = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
        algebraic_sort(ota)
        self.assertEqual(ota.binary_array, bin_arr)

    def test_reverse_points_arr_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        ota = Ota(lis)
        points = [[0, 47], [1, 31], [2, 23], [3, 17], [4, 11], [5, 7], [6, 3], [7, 2]]
        algebraic_sort(ota)
        self.assertEqual(ota.points_arr, points)

    def test_plots_visually_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        ota = Ota(lis)

        ota_reversed = Ota(lis)
        algebraic_sort(ota_reversed)

        plot_maker = PlotMaker()
        plot_maker.x_arr = ota.x_arr
        plot_maker.y_arr = ota_reversed.y_arr
        plot = plot_maker.make_scatter_plot("Plot of Ota function", 'o', 20)
        plot.show()

    def test_both_plots_visually_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        ota = Ota(lis)

        ota_reversed = Ota(lis)
        algebraic_sort(ota_reversed)

        sum_x = ota.x_arr + ota_reversed.x_arr
        sum_y = ota.y_arr + ota_reversed.y_arr
        plot_maker = PlotMaker()
        plot_maker.x_arr = sum_x
        plot_maker.y_arr = sum_y
        plot = plot_maker.make_scatter_plot("Plot of ota and reverse sorted ota function", 'o', 20)
        plot.show()


if __name__ == '__main__':
    unittest.main()
