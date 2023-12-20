import datetime
import unittest

import electricity_usage
from electricity_usage import ElectricityUsage


class TestElectricityUsage(unittest.TestCase):
    def test_get_tariff_I(self):
        self.assertTrue(ElectricityUsage._get_tariff(5))

    def test_get_tariff_II(self):
        self.assertFalse(ElectricityUsage._get_tariff(4))

    def test_get_electricity_usage_i(self):
        self.assertEqual(electricity_usage.ElectricityUsage()._get_electricity_usage_i(2, 2.5, 20, 12), [22, 14.5])

    def test_get_electricity_usage_ii(self):
        self.assertEqual(electricity_usage.ElectricityUsage()._get_electricity_usage_ii(2, 2.5, 20, 12), [22, 14.5])

    def test_is_new_month_true(self):
        self.assertTrue(electricity_usage.ElectricityUsage()._is_new_month(datetime.date(2019, 12, 1)))

    def test_is_new_month_false(self):
        self.assertFalse(electricity_usage.ElectricityUsage()._is_new_month(datetime.date(2019, 12, 2)))

    def test_is_new_year_true(self):
        self.assertTrue(electricity_usage.ElectricityUsage()._is_new_year(datetime.date(2021, 12, 4), 31536000))

    def test_is_new_year_false(self):
        self.assertFalse(electricity_usage.ElectricityUsage()._is_new_year(datetime.date(2021, 12, 4), 31536000 - 1))

    def test_is_new_year_leap_true(self):
        self.assertTrue(electricity_usage.ElectricityUsage()._is_new_year(datetime.date(2000, 1, 4), 31622400))

    def test_is_new_year_leap_false(self):
        self.assertFalse(electricity_usage.ElectricityUsage()._is_new_year(datetime.date(2000, 1, 4), 31622400 - 1))

    def test_count_powers_t_1(self):
        self.assertEqual(ElectricityUsage._count_powers(True, ))


if __name__ == '__main__':
    unittest.main()
