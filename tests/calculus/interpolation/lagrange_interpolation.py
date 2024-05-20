import unittest

from app.calculus.interpolation.langrange_interpolation import LagrangeInterpolation


class LagrangeInterpolationTests(unittest.TestCase):
   def setUp(self):
       x_points = [1, 2, 3, 4]
       y_points = [1, 4, 9, 16]
       self.lagrange_interpolation = LagrangeInterpolation(x_points, y_points)

   def test_interpolation_valid(self):
       pass


if __name__ == '__main__':
    unittest.main()
