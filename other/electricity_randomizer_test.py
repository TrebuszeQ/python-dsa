import unittest
from unittest import mock
from unittest.mock import patch
# my
from electricity_randomizer import ElectricityRandomizer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.randomizer = ElectricityRandomizer()

    # @patch('electricity_randomizer.randint', return_value=15)
    # @patch('electricity_randomizer.random', return_value=0.5)
    # def test_randomize_power(self, mock_randint, mock_random):
    #     assert self.randomizer.randomize_power2() == 0.5 * 15

    @patch('electricity_randomizer.randint', return_value=15)
    def test_randomize_power2(self, mock_randint):
        assert self.randomizer._randomize_power2() == 15 * 15


if __name__ == '__main__':
    unittest.main()
