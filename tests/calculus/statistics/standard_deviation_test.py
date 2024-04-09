import unittest
from app.calculus.statistics.standard_deviation import StandardDeviation


class StandardDeviationTest(unittest.TestCase):

    def test_sigma_valid(self):
        standard_deviation = StandardDeviation([5, 6, 8, 9])
        corrected = standard_deviation.corrected
        self.assertEqual(1.8257418583505538, corrected)

    def test_sigma_valid2(self):
        standard_deviation = StandardDeviation([20, 11, 18, 1, 3])
        corrected = standard_deviation.corrected
        self.assertEqual(8.561541917201598, corrected)

    def test_single_bessel_valid(self):
        standard_deviation = StandardDeviation([5, 6, 8, 9])
        corrected = standard_deviation.bessel_correction_unbiased()
        self.assertAlmostEqual(1.8257418583505538, corrected)

    def test_single_bessel_valid2(self):
        standard_deviation = StandardDeviation([20, 11, 18, 1, 3])
        corrected = standard_deviation.bessel_correction_unbiased()
        self.assertEqual(8.561541917201598, corrected)


if __name__ == '__main__':
    unittest.main()
