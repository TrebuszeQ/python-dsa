import unittest
from app.mathematical.statistics.arithmetic_average import ArithmeticAverage


class StandardDeviationTest(unittest.TestCase):

    def test_sigma_valid(self):
        arithmetic_average = ArithmeticAverage([5, 6, 8, 9])
        self.assertEqual(7, arithmetic_average.value)

    def test_sigma_valid2(self):
        arithmetic_average = ArithmeticAverage([20, 11, 18, 1, 3])
        self.assertEqual(10.6, arithmetic_average.value)


if __name__ == '__main__':
    unittest.main()
