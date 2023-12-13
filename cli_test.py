import unittest
from unittest.mock import patch
# my
from cli import Cli


class MyTestCase(unittest.TestCase):
    def test_is_float_valid(self):
        print(__name__)
        result = Cli.is_float(3.5)

        self.assertTrue(result)

    def test_is_float_invalid(self):
        print(__name__)
        result = Cli.is_float("3.5")

        self.assertFalse(result)

    @patch("builtins.input", side_effect=['10.5'])
    def test_try_read_input_float_valid(self, mock_input):
        print("try_read_input_float_valid")
        result = Cli.try_read_input_float("Wprowadz wartosc typu float: \n")

        self.assertEqual(result, 10.5)

    @patch("builtins.input", side_effet=['1.0'])
    def test_read_float_triple_valid(self, mock_input):
        print("test_read_float_triple_valid")
        result = Cli.read_float_triple()

        self.assertEqual(result, [1.0, 1.0, 1.0])


if __name__ == '__main__':
    unittest.main()
