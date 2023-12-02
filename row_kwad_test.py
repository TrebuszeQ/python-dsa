import unittest
from unittest.mock import patch
# my modules
import row_kwad


class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['10.5'])
    def test_read_input_with_valid_float(self, mock_input):
        result = row_kwad.read_input("Wprowadz wartosc typu float: ")
        self.assertEqual(result, 10.5)

    # sprawdza, czy funkcja zwroci oczekiwana wartosc None z racji wystapienia wyjatku
    @patch('builtins.input', side_effect=['not_a_number'])
    def test_read_input_with_invalid_float(self, mock_input):
        result = row_kwad.read_input("Enter a number: ")
        self.assertEqual(result, None)

    @patch("a, b, c", side_effect=[0, 2, 5])
    def test_results_linear(self):
        result = row_kwad.rownanie()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
