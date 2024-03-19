import unittest
from src.mathematical.polynomials.single_polynomial import SinglePolynomial


class MyTestCase(unittest.TestCase):
    def test_horner_method(self):
        polynomial_dct: {float: float} = {3.0: 3.0, 2.21: 2.0, 2.5: 1.0}
        self.assertEqual(-24.6159, SinglePolynomial(polynomial_dct))


if __name__ == '__main__':
    unittest.main()
