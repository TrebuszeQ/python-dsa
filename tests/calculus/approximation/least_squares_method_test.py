import unittest
import app.calculus.approximation.least_squares_method as lsm


class MyTestCase(unittest.TestCase):
    def setUp1(self):
        self.points_x = self.x = [2, 4, 6, 8, 10]
        self.points_y = self.y = [13, 27, 24, 44, 38]
        self.n = len(self.points_x)

    def test_find_a_valid(self):
        self.setUp1()
        sigma_xy = lsm.find_sigma_xy(self.n, self.x, self.y, debug=True)
        sigma_x = lsm.find_sigma_x(self.n, self.x, debug=True)
        sigma_y = lsm.find_sigma_y(self.n, self.y, debug=True)
        sigma_x2 = lsm.find_sigma_x2(self.n, self.x, debug=True)
        a = lsm.find_a(self.n, sigma_xy, sigma_x, sigma_y, sigma_x2, debug=True)
        self.assertAlmostEqual(3.35, a)

    def test_find_b_valid(self):
        self.setUp1()
        sigma_xy = lsm.find_sigma_xy(self.n, self.x, self.y, debug=True)
        sigma_x = lsm.find_sigma_x(self.n, self.x, debug=True)
        sigma_y = lsm.find_sigma_y(self.n, self.y, debug=True)
        sigma_x2 = lsm.find_sigma_x2(self.n, self.x, debug=True)
        a = lsm.find_a(self.n, sigma_xy, sigma_x, sigma_y, sigma_x2, debug=True)
        b = lsm.find_b(self.n, a, sigma_y, sigma_x, debug=True)
        self.assertAlmostEqual(9.1, b)  # add assertion here


    def setUp2(self):
        self.points_x = self.x = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.points_y = self.y = [1.0, 5.0, 7.0, 12.0, 17.0]
        self.n = len(self.points_x)

    def test_find_a_valid2(self):
        self.setUp2()
        sigma_xy = lsm.find_sigma_xy(self.n, self.x, self.y)
        sigma_x = lsm.find_sigma_x(self.n, self.x)
        sigma_y = lsm.find_sigma_y(self.n, self.y)
        sigma_x2 = lsm.find_sigma_x2(self.n, self.x)
        a = lsm.find_a(self.n, sigma_xy, sigma_x, sigma_y, sigma_x2)
        self.assertAlmostEqual(3.9, a)

    def test_find_b_valid2(self):
        self.setUp2()
        sigma_xy = lsm.find_sigma_xy(self.n, self.x, self.y)
        sigma_x = lsm.find_sigma_x(self.n, self.x)
        sigma_y = lsm.find_sigma_y(self.n, self.y)
        sigma_x2 = lsm.find_sigma_x2(self.n, self.x)
        a = lsm.find_a(self.n, sigma_xy, sigma_x, sigma_y, sigma_x2)
        b = lsm.find_b(self.n, a, sigma_y, sigma_x)
        self.assertAlmostEqual(-3.3, b)  # add assertion here


if __name__ == '__main__':
    unittest.main()
