import unittest
from app.calculus.approximation.least_squares_method import LeastSquaresMethod
from app.services.plot_maker_service import PlotMaker


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.plt = PlotMaker()

    def test_find_a_valid(self):
        lsm = LeastSquaresMethod([2, 4, 6, 8, 10], [13, 27, 24, 44, 38])
        self.assertAlmostEqual(3.35, lsm.a)

    def test_find_b_valid(self):
        lsm = LeastSquaresMethod([2, 4, 6, 8, 10], [13, 27, 24, 44, 38])
        self.assertAlmostEqual(9.1, lsm.b)  # add assertion here

    def test_plot_visual_valid(self):
        lsm = LeastSquaresMethod([2, 4, 6, 8, 10], [13, 27, 24, 44, 38])
        lsm.make_linear_approximation_plot(30, True)

    def test_find_a_valid2(self):
        lsm = LeastSquaresMethod([1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 5.0, 7.0, 12.0, 17.0])
        self.assertAlmostEqual(3.9, lsm.a)

    def test_find_b_valid2(self):
        lsm = LeastSquaresMethod([1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 5.0, 7.0, 12.0, 17.0])
        self.assertAlmostEqual(-3.3, lsm.b)  # add assertion here


if __name__ == '__main__':
    unittest.main()
