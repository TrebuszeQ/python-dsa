import unittest
from app.algebra.prime_numbers.inverse_prime_sum_with_spacing import SumInversePrimesWithSpacing


class SumInversePrimeWithSpacingTests(unittest.TestCase):

    def test_sum_inverse_primes_valid(self):
        inv_sum = SumInversePrimesWithSpacing()
        self.assertAlmostEquals(inv_sum, 0)


if __name__ == '__main__':
    unittest.main()
