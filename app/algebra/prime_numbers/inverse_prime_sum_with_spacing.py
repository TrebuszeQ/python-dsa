import app.utils.input_readers as input_readers
from app.algebra.prime_numbers.adjustable_eratosthenes_sieve import AdjustableEratosthenesSieve


class SumInversePrimesWithSpacing(AdjustableEratosthenesSieve):
    @property
    def inverted_primes_sum(self):
        return self._inverted_primes_sum

    def __init__(self):
        self._inverted_primes_sum = 0
        increment = self.__read_s() + 1
        end = self.__read_upper_limit()
        super().__init__(end, increment)
        self._sum_inverse_primes()

    def __read_s(self):
        value = 0
        allowed = [2, 3, 4, 5, 6, 7, 10, 20, 50, 100, 1000, 5000, 10000]
        while value not in allowed:
            value = input_readers.try_read_input_int("Insert one of the following incremental values: [2, 3, 4, 5, 6, 7, 10, 20, 50, 100, 1000, 5000, 10000]")

        return value

    def __read_upper_limit(self):
        value = 0
        allowed = [1000000, 10000000, 50000000]
        while value not in allowed:
            value = input_readers.try_read_input_int("Choose upper limit from: [1m, 10m, 50m].")

        return value

    def __print_sum_of_opposites(self, s, upper_lim):
        print(f"Sum of opposites of prime numbers per increment of {s} to {upper_lim}")

    def _sum_inverse_primes(self):
        for prime in self._primes:
            inverse_prime = 1.0/prime
            self._inverted_primes_sum += inverse_prime
