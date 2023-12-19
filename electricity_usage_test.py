import datetime
import unittest
from electricity_usage import ElectricityUsage


class TestElectricityUsage(unittest.TestCase):
    def test_get_tariff_I(self):
        self.assertTrue(ElectricityUsage._get_tariff(5))

    def test_get_tariff_II(self):
        self.assertFalse(ElectricityUsage._get_tariff(4))


if __name__ == '__main__':
    unittest.main()
