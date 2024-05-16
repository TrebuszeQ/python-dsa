import unittest
from app.discrete.ota import Ota
from app.services.plot_maker_service import PlotMaker


class OtaTests(unittest.TestCase):

    def test_degree_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        ota = Ota(lis)
        self.assertEqual(len(lis), ota.degree)

    def test_binary_degree_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        ota = Ota(lis)
        self.assertEqual(len(bin(7)[2:]), ota.binary_degree)

    def test_c_array_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        c_arr = [2, 1, 4, 4, 6, 6, 8, 16]
        ota = Ota(lis)
        self.assertEqual(c_arr, ota.c_array)

    def test_bin_array_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        bin_arr = [[0, 0, 0], [0, 0, 1],  [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
        ota = Ota(lis)
        self.assertEqual(bin_arr, ota.binary_array)

    def test_points_arr_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        ota = Ota(lis)
        points_arr = [[0, 2], [1, 3], [2, 7], [3, 11], [4, 17], [5, 23], [6, 31], [7, 47]]
        self.assertEqual(points_arr, ota.points_arr)

    def test_plot_visually_valid(self):
        lis = [2, 3, 7, 11, 17, 23, 31, 47]
        ota = Ota(lis)

        plot_maker = PlotMaker(ota.x_arr, ota.y_arr)
        plot_maker.make_scatter_plot("Plot of Ota function", 'o', 20)


if __name__ == '__main__':
    unittest.main()
