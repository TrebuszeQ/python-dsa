from app.mathematical.polynomials.single_polynomial_dict import SinglePolynomialDict
import unittest


class MyTestCase(unittest.TestCase):
    def test_sort_valid(self):
        poly_ar = {23.0: 1.0, 4.0: 3.0, 2.0: 2.0}
        poly = SinglePolynomialDict(poly_ar, 0)
        self.assertEqual([[4.0, 3.0], [2.0, 2.0], [23.0, 1.0]], poly.poly)

    def test_y_valid(self):
        poly_dct = {-3.0: 3.0, 2.21: 2.0, -2.5: 1.0}
        poly = SinglePolynomialDict(poly_dct, 0)
        poly.y = 1
        self.assertEqual(-24.6159, poly.y)

    def test_horner_method_valid(self):
        poly_ar = {2.0: 4.0, 5.0: 2.0, 4.0: 1.0}
        poly = SinglePolynomialDict(poly_ar, 1.0)
        self.assertEqual(47/8, poly.horner_method(3/2))


if __name__ == '__main__':
    unittest.main()
