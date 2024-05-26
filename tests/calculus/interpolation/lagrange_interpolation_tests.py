import unittest

from app.calculus.interpolation.langrange_interpolation import LagrangeInterpolation


class LagrangeInterpolationTests(unittest.TestCase):
    # def test_interpolation_valid(self):
    #     x_points = [1, 2, 3, 4]
    #     y_points = [1, 4, 9, 16]
    #     self.lagrange_interpolation = LagrangeInterpolation(x_points, y_points)
    #     value = self.lagrange_interpolation.interpolate(2)
    #     self.assertEqual(4, value)

    def test_interpolation_valid2(self):
        x_points = [0, 1, 3]
        y_points = [1, 3, 2]
        self.lagrange_interpolation = LagrangeInterpolation(x_points, y_points)
        value = self.lagrange_interpolation.interpolate(2)
        self.assertEqual(10/3, value)
        # l0(2) = (2 - 0)(2 - 1)(2 - 3) / (0 - 0)(0 - 1)(0 - 3)
        # l1(2) = (2 - 0)(2 - 1)(2 - 3) / (1 - 0)(1 - 1)(1 - 3)
        # l2(2) = (2 - 0)(2 - 1)(2 - 3) / (3 - 0)(3 - 1)(3 - 3)



if __name__ == '__main__':
    unittest.main()
