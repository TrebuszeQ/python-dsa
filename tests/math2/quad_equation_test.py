import unittest
from unittest.mock import patch
import math
# my modules
import quad_equation


class TestMain(unittest.TestCase):

    def test_get_delta(self):
        print("test_get_delta")
        a = 1.0
        b = 2.0
        c = 3.0
        result = quad_equation.get_delta(a, b, c)

        self.assertEqual(result, ((b * b) - 4 * (a * c)))

    def test_get_equation_a0(self):
        print("test_get_equation_a0")
        values = [0, 1, 3]
        result = quad_equation.get_equation(values)

        self.assertFalse(0, result)

    @patch("row_kwad.get_delta", return_value=-1)
    def test_get_equation_delta_negative(self, mock_input):
        print("test_get_equation_delta_negative")
        values = [1, 0, 0]
        result = quad_equation.get_equation(values)
        self.assertEqual(result, None)

    @patch("row_kwad.get_delta", return_value=25)
    def test_get_equation_delta_positive(self, mock_input):
        print("test_get_equation_delta_positive")
        values = [1, 0, 0]
        a, b, c = values
        result = quad_equation.get_equation(values)
        x1 = ((-b - math.sqrt(25)) / (2 * a))
        x2 = ((-b + math.sqrt(25)) / (2 * a))

        self.assertEqual(result, [x1, x2])

    @patch("row_kwad.get_delta", return_value=0)
    def test_get_equation_delta_0(self, mock_input):
        print("test_get_equation_delta_0")
        result = quad_equation.get_equation([1, 0, 0])

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
