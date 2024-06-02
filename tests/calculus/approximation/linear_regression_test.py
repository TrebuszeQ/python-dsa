import math
import unittest
from app.calculus.approximation.linear_regression import linear_regression


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.points_x = [2, 4, 6, 8, 10]
        self.points_y = [14, 27, 24, 44, 48]
        self.n = math.floor(len(self.points_x) / 2)

    def test_linear_regression(self):
        r = linear_regression(self.n, self.points_x, self.points_y)
        self.assertAlmostEqual(r, 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
