import unittest

from app.calculus.interpolation.langrange_interpolation import LagrangeInterpolation
from app.services.plot_maker_service import PlotMaker


class LagrangeInterpolationTests(unittest.TestCase):
    def setUp(self):
        self._plot_maker = PlotMaker()

    def test_interpolation_valid(self):
        x_points = [1, 2, 3, 4]
        y_points = [1, 4, 9, 16]
        self.lagrange_interpolation = LagrangeInterpolation(x_points, y_points)
        value = self.lagrange_interpolation.interpolate(2)
        self.assertEqual(4, value)

    def test_interpolation_valid2(self):
        x_points = [0, 1, 3]
        y_points = [1, 3, 2]
        self.lagrange_interpolation = LagrangeInterpolation(x_points, y_points)
        value = self.lagrange_interpolation.interpolate(2)
        self.assertAlmostEqual(10/3, value)

    def test_interpolation_valid3(self):
        x_points = [1, 2, 3]
        y_points = [2, 0, 1]
        self.lagrange_interpolation = LagrangeInterpolation(x_points, y_points)
        value = self.lagrange_interpolation.interpolate(201)
        self.assertAlmostEqual(59302, value)

    def test_interpolation_valid3_plots_visually(self):
        x_points = [1, 2, 3]
        y_points = [2, 0, 1]
        self.lagrange_interpolation = LagrangeInterpolation(x_points, y_points)
        value = self.lagrange_interpolation.interpolate(201)
        self._plot_maker.x_arr = x_points
        self._plot_maker.y_arr = y_points
        plot = self._plot_maker.make_single_line_plot("Interpolation Polynomial Plot", 32, True)
        plot.show()

        self.lagrange_interpolation.x_points = self.lagrange_interpolation._pi_points
        self.lagrange_interpolation.y_points = self.lagrange_interpolation._sigma_points
        plot = self._plot_maker.make_single_line_plot("Lagrange Interpolation Plot", 32, True)
        plot.show()


if __name__ == '__main__':
    unittest.main()
