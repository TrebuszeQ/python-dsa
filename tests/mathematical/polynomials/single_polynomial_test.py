import unittest
from src.mathematical.polynomials.single_polynomial import SinglePolynomial


class MyTestCase(unittest.TestCase):
    def test_y(self):
        polynomial_dct: {float: float} = {-3.0: 3.0, 2.21: 2.0, -2.5: 1.0}
        poly = SinglePolynomial(polynomial_dct)
        poly.y = 1
        print(poly.poly_str)
        self.assertEqual(-24.6159, poly.y)

    def test_solve(self):
        polynomial_dct: {float: float} = {-1.0: 3.0, 7.0: 2.0, 1.0: 1.0}
        self.assertEqual(-24.6159, SinglePolynomial(polynomial_dct).solve)

    def test_horner_method(self):
        polynomial_dct: {float: float} = {1.0: 4.0, 3.0: 3.0, 1.0: 1.0, -3: 0}
        self.assertEqual(-2, SinglePolynomial())


if __name__ == '__main__':
    unittest.main()
