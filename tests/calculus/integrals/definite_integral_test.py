from app.calculus.integrals.definite_integral import DefiniteIntegral
from app.services.plot_maker_service import PlotMaker
import unittest


class DefiniteIntegralTest(unittest.TestCase):

    def setUp(self):
        self.plot_maker = PlotMaker()

    def func(self, x):
        return x * x + x + 2.0

    def func2(self, x):
        return x * x + 4

    def test_sum_valid(self):
        definite_integral = DefiniteIntegral(self.func, 1, 5,  self.plot_maker, 1000)
        area = definite_integral.computed_area
        self.assertAlmostEqual(61.333, area, places=1)

    def test_make_plot_visually_valid(self):
        definite_integral = DefiniteIntegral(self.func, 1, 5, self.plot_maker, 1000)
        definite_integral.plot.show()

    def test_sum_valid_func2(self):
        definite_integral = DefiniteIntegral(self.func2, 0, 6,  self.plot_maker, 1000)
        area = definite_integral.computed_area
        self.assertAlmostEqual(96, area, places=1)

    def test_make_plot_visually_func2_valid(self):
        definite_integral = DefiniteIntegral(self.func, 0, 6, self.plot_maker, 1000)
        definite_integral.plot.show()


if __name__ == '__main__':
    unittest.main()
