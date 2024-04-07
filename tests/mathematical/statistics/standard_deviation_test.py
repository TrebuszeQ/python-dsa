import unittest
from app.mathematical.statistics.standard_deviation import StandardDeviation


class StandardDeviationTest(unittest.TestCase):

    def test_sigma_valid(self):
        arithmetic_average = StandardDeviation([5, 6, 8, 9])
        self.assertEqual(1.8257, arithmetic_average.value)

    def test_sigma_valid2(self):
        arithmetic_average = StandardDeviation([20, 11, 18, 1, 3])
        self.assertEqual(10.6, arithmetic_average.value)

    def test_single_algo_gpt_valid(self):
        self.assertEqual(1.8257, StandardDeviation([5, 6, 8, 9]).single_algorithm_gpt3([5, 6, 8, 9]))

    def test_single_algo_valid(self):
        self.assertEqual(1.8257, StandardDeviation([5, 6, 8, 9]).single_algorithm([5, 6, 8, 9]))


if __name__ == '__main__':
    unittest.main()
