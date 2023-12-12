import unittest
from unittest.mock import patch, Mock
import math
# my modules
import quad_equation


class TestMain(unittest.TestCase):

    def test_is_float_valid(self):
        print(__name__)
        result = quad_equation.is_float(3.5)

        self.assertTrue(result)

    def test_is_float_invalid(self):
        print(__name__)
        result = quad_equation.is_float("3.5")

        self.assertFalse(result)

    @patch("builtins.input", side_effect=['10.5'])
    def test_try_read_input_float_valid(self, mock_input):
        print("try_read_input_float_valid")
        result = quad_equation.try_read_input_float("Wprowadz wartosc typu float: \n")

        self.assertEqual(result, 10.5)

    @patch("builtins.input", side_effet=['1.0'])
    def test_read_float_triple_valid(self, mock_input):
        print("test_read_float_triple_valid")
        result = quad_equation.read_float_triple()

        self.assertEqual(result, [1.0, 1.0, 1.0])

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
