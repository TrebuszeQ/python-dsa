import unittest
from app.algebra.prime_numbers.adjustable_eratosthenes_sieve import AdjustableEratosthenesSieve


class AdjustableEratosthenesSieveTests(unittest.TestCase):
    def test_adj_eratosthenes_sieve_valid(self):
        primes = [2, 3,	5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        sieve = AdjustableEratosthenesSieve(100, 1)
        primes2 = sieve.find_primes()
        self.assertEqual(primes, primes2)

    def test_adj_eratosthenes_sieve_valid2(self):
        primes = [2, 5, 11, 17, 23, 31, 41, 47]
        sieve = AdjustableEratosthenesSieve(50, 2)
        primes2 = sieve.find_primes()
        self.assertEqual(primes, primes2)

    def test_adj_eratosthenes_sieve_valid3(self):
        primes = [2, 31, 73]
        sieve = AdjustableEratosthenesSieve(100, 10)
        primes2 = sieve.find_primes()
        self.assertEqual(primes, primes2)


if __name__ == '__main__':
    unittest.main()
