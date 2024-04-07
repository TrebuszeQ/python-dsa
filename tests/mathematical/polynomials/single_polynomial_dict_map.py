from app.mathematical.polynomials.single_polynomial_map import SinglePolynomialDict
import unittest


class MyTestCase(unittest.TestCase):
    def test_sort_valid(self):
        poly_dct = {1.0: 23.0, 3.0: 4.0, 2.0: 2.0}
        poly = SinglePolynomialDict(poly_dct, 0)
        self.assertEqual({3.0: 4.0, 2.0: 2.0, 1.0: 23.0}, poly.poly)

    def test_y_valid(self):
        poly_dct = {3.0: -3.0, 2.0: 2.21, 1.0: -2.5}
        poly = SinglePolynomialDict(poly_dct, 0)
        poly.y = 1
        self.assertEqual(-24.6159, poly.y)

    def test_horner_method_valid(self):
        poly_dct = {4.0: 2.0, 2.0: -5.0, 1.0: 4.0}
        poly = SinglePolynomialDict(poly_dct, 1.0)
        self.assertEqual(47/8, poly.horner_method(1.5))


if __name__ == '__main__':
    unittest.main()
