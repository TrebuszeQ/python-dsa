from app.mathematical.polynomials.single_polynomial import SinglePolynomial
import unittest


class MyTestCase(unittest.TestCase):
    def test_y_valid(self):
        poly_ar = [[-3.0, 3.0], [2.21, 2.0], [-2.5, 1.0]]
        poly = SinglePolynomial(poly_ar)
        poly.y = 1
        self.assertEqual(-24.6159, poly.y)


if __name__ == '__main__':
    unittest.main()
