import unittest
from app.mathematical.polynomials.single_polynomial import SinglePolynomial


class MyTestCase(unittest.TestCase):

    def test_poly_str_valid(self):
        poly = SinglePolynomial([[-3.0, 3.0], [2.21, 2.0], [-2.5, 1.0]])
        self.assertEqual("-3.0^3.0 +2.21^2.0 -2.5^1.0", poly.poly_str)

    def test_y_valid(self):
        poly_ar = [[-3.0, 3.0], [2.21, 2.0], [-2.5, 1.0]]
        poly = SinglePolynomial(poly_ar)
        poly.y = 1
        self.assertEqual(-24.6159, poly.y)

    # def test_horner_method(self):
    #     polynomial_dct: {float: float} = {1.0: 4.0, 3.0: 3.0, 1.0: 1.0, -3: 0}
    #     self.assertEqual(-2, SinglePolynomial())


if __name__ == '__main__':
    unittest.main()
