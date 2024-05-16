from app.calculus.integrals.definite_integral import DefiniteIntegral
from app.services.plot_maker_service import PlotMaker
import unittest


class DefiniteIntegralTest(unittest.TestCase):

    def setUp(self):
        arr_x = [i for i in range(30)]
        arr_y = [i for i in range(10)]
        self.plot_maker = PlotMaker()

    def func(self, x):
        return x * x + x + 2.0

    def test_sum_valid(self):
        definite_integral = DefiniteIntegral(self.func, 1, 5,  self.plot_maker, 1000)
        definite_integral.set_computed_area()
        sigma = definite_integral.computed_area
        self.assertAlmostEqual(61.333, sigma, places=1)

    def test_plot_visually_valid(self):
        definite_integral = DefiniteIntegral(self.func, 1, 5, self.plot_maker, 1000)
        definite_integral.set_computed_area()
        sigma = definite_integral.computed_area




if __name__ == '__main__':
    unittest.main()
