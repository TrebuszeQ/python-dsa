import unittest
from app.mathematical.statistics.standard_deviation import StandardDeviation


class StandardDeviationTest(unittest.TestCase):

    def test_sigma_valid(self):
        arithmetic_average = StandardDeviation([5, 6, 8, 9])
        self.assertEqual(1.8257, arithmetic_average.value)

    def test_sigma_valid2(self):
        arithmetic_average = StandardDeviation([20, 11, 18, 1, 3])
        self.assertEqual(10.6, arithmetic_average.value)


if __name__ == '__main__':
    unittest.main()
