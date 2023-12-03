import unittest
from unittest.mock import patch
# my modules
import row_kwad


class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['10.5'])
    def test_wejscie_float_prawidlowy_float(self, mock_input):
        result = row_kwad.odczytaj_wejscie_float("Wprowadz wartosc typu float: ")
        self.assertEqual(result, 10.5)

    # sprawdza, czy funkcja zwroci oczekiwana wartosc None z racji wystapienia wyjatku
    @patch('builtins.input', side_effect=['not_a_number'])
    def test_wejscie_float_nieprawidlowy_float(self, mock_input):
        result = row_kwad.odczytaj_wejscie_float("Enter a number: ")
        self.assertEqual(result, None)

    @patch("builtins.input", side_effect=["0.0"])
    @patch("builtins.input", side_effect=["2.0"])
    @patch("builtins.input", side_effect=["3.2"])
    def test_odczytaj_trzy_zmienne_float_prawidlowe(self, mock_input1, mock_input2, mock_input3):
        result = row_kwad.odczytaj_trzy_zmienne_float()
        self.assertEqual(result, [mock_input1, mock_input2, mock_input3])


if __name__ == '__main__':
    unittest.main()
