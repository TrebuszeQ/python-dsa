import logging
import math
from app.algebra.prime_numbers.eratosthenes_sieve import EratosthenesSieve


class AdjustableEratosthenesSieve(EratosthenesSieve):
    @property
    def primes(self):
        return self._primes

    def __init__(self, end, increment):
        self._increment = increment
        super().__init__(end)
        self._logger = logging.getLogger(__name__)
        self._validate_increment()

    def _validate_increment(self):
        if self._increment < 0 or self._increment > self._end:
            self._increment = 1
            self._logger.error("Increment is invalid. Set to 1.")

    def find_primes(self):
        nums = [True for i in range(2, self._end)]
        sqrt_end = math.sqrt(self._end)
        i = self._primes[0]
        while i <= sqrt_end:
            if nums[i]:
                incr = 0
                j = i ** 2 + incr * i
                while j <= self._end:
                    j = i ** 2 + incr * i
                    try:
                        nums[j] = False
                    except IndexError:
                        break
                    incr += 1
            i += 1
        return self._filter_primes(nums)

    def _filter_primes(self, nums):
        prime = self.primes[0]
        for i in range(self.primes[0], len(nums), self._increment):
            if nums[i] is True:
                self._primes.append(i)

        return self._primes
