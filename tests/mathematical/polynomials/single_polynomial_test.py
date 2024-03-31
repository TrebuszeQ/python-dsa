from app.mathematical.polynomials.single_polynomial import SinglePolynomial
import unittest


class MyTestCase(unittest.TestCase):
    def test_sort_valid(self):
        poly_ar = [[23.0, 1.0], [4.0, 3.0], [2.0, 2.0]]
        poly = SinglePolynomial(poly_ar)
        self.assertEqual([[23.0, 1.0], [2.0, 2.0], [4.0, 3.0]], poly.poly)
    # def test_y_valid(self):
    #     poly_ar = [[-3.0, 3.0], [2.21, 2.0], [-2.5, 1.0]]
    #     poly = SinglePolynomial(poly_ar)
    #     poly.y = 1
    #     self.assertEqual(-24.6159, poly.y)


if __name__ == '__main__':
    unittest.main()
