import logging
import math


class EratosthenesSieve:
    @property
    def primes(self):
        return self._primes

    def __init__(self, end):
        self._logger = logging.getLogger(__name__)
        self._end = end
        self._validate_end()
        self._primes = [2]

    def _validate_end(self):
        if self._end < 2:
            self._logger.error("End is lesser than 2. Set to 2.")
            self._end = 2

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
        for i in range(3, len(nums)):
            if nums[i] is True:
                self._primes.append(i)

        return self._primes





