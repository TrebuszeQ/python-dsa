import unittest
from unittest.mock import patch
# my
from cli import Cli
from leap_year import LeapYear


class MyTestCase(unittest.TestCase):

    @patch("builtins.input", side_effect=["1997"])
    def test_take_year(self, mock_input):
        self.assertEqual(LeapYear.take_year(), 1997)

    def test_is_leap_year_true(self):
        self.assertTrue(LeapYear.is_leap_year(1996))

    def test_is_leap_year_false(self):
        self.assertFalse(LeapYear.is_leap_year(2021))


if __name__ == '__main__':
    unittest.main()
