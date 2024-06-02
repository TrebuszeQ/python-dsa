import unittest
import app.calculus.approximation.least_squares_method as lsm
from math import floor


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.points_x = self.x = [2, 4, 6, 8, 10]
        self.points_y = self.y = [14, 27, 24, 44, 48]
        self.n = len(self.points_x)

    def test_find_a_valid(self):
        sigma_xy = lsm.find_sigma_xy(self.n, self.x, self.y)
        sigma_x = lsm.find_sigma_x(self.n, self.x)
        sigma_y = lsm.find_sigma_y(self.n, self.y)
        sigma_x2 = lsm.find_sigma_x2(self.n, self.x)
        a = lsm.find_a(self.n, sigma_xy, sigma_x, sigma_y, sigma_x2)
        self.assertEqual(4.25, a)

    def test_find_b_valid(self):
        sigma_xy = lsm.find_sigma_xy(self.n, self.x, self.y)
        sigma_x = lsm.find_sigma_x(self.n, self.x)
        sigma_y = lsm.find_sigma_y(self.n, self.y)
        sigma_x2 = lsm.find_sigma_x2(self.n, self.x)
        a = lsm.find_a(self.n, sigma_xy, sigma_x, sigma_y, sigma_x2)
        b = lsm.find_b(self.n, a, sigma_y, sigma_x)
        self.assertEqual(5.9, b)  # add assertion here

    def setUp(self):
        self.points_x = self.x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
        self.points_y = self.y = [5.0, 3.0, 6.0, 3.5, 4.5, 7.0, 5.5]
        self.n = len(self.points_x)

    def test_find_a_valid2(self):
        sigma_xy = lsm.find_sigma_xy(self.n, self.x, self.y)
        sigma_x = lsm.find_sigma_x(self.n, self.x)
        sigma_y = lsm.find_sigma_y(self.n, self.y)
        sigma_x2 = lsm.find_sigma_x2(self.n, self.x)
        a = lsm.find_a(self.n, sigma_xy, sigma_x, sigma_y, sigma_x2)
        self.assertEqual(4.25, a)

    def test_find_b_valid2(self):
        sigma_xy = lsm.find_sigma_xy(self.n, self.x, self.y)
        sigma_x = lsm.find_sigma_x(self.n, self.x)
        sigma_y = lsm.find_sigma_y(self.n, self.y)
        sigma_x2 = lsm.find_sigma_x2(self.n, self.x)
        a = lsm.find_a(self.n, sigma_xy, sigma_x, sigma_y, sigma_x2)
        b = lsm.find_b(self.n, a, sigma_y, sigma_x)
        self.assertEqual(5.9, b)  # add assertion here


if __name__ == '__main__':
    unittest.main()
