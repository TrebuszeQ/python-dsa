import unittest
from unittest.mock import patch
from app.algebra.prime_numbers import inverse_prime_sum_with_spacing
from app.algebra.prime_numbers.inverse_prime_sum_with_spacing import sum_inverted_primes_with_spacing


class SumInversePrimeWithSpacingTests(unittest.TestCase):

    def test_sum_inverse_primes_valid(self):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.662397268)

    # @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=2)
    # @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50)
    # def test_sum_inverse_primes_valid(self, input1, input2):
    #     inv_sum = sum_inverted_primes_with_spacing()
    #     self.assertEqual(inv_sum, 1.662397268)


if __name__ == '__main__':
    unittest.main()
