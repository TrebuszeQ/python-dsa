import unittest
from app.algebra.prime_numbers.eratosthenes_sieve import EratosthenesSieve


class MyTestCase(unittest.TestCase):
    def test_erastothenes_sieve(self):
        primes = [2, 3,	5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        sieve = EratosthenesSieve(100)
        primes2 = sieve.primes
        self.assertEqual(primes, primes2)


if __name__ == '__main__':
    unittest.main()
