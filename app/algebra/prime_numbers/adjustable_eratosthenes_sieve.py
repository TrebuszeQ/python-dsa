import logging


class AdjustableEratosthenesSieve:
    @property
    def primes(self):
        return self._primes

    def __init__(self, end, increment):
        self._logger = logging.getLogger(__name__)
        self._end = end
        self._increment = increment
        self._validate_end()
        self._validate_increment()
        self._primes = [2]
        self.find_primes()
        self._filter_out_by_increment()

    def _validate_end(self):
        if self._end < 2:
            self._end = 2
            self._logger.error("End is lesser than 2. Set to 2.")

    def _validate_increment(self):
        if self._increment < 0 or self._increment > self._end:
            self._increment = 1
            self._logger.error("Increment is invalid. Set to 1.")

    def _filter_out_by_increment(self):
        if self._increment == 1:
            return

        filtered = []
        for i in range(0, len(self._primes), self._increment):
            filtered.append(self._primes[i])

        self._primes = filtered

    def find_primes(self):
        not_filtered = [i for i in range(2, self._end)]
        filtered = []
        to_range = len(self._primes)

        i = 0
        while i != to_range:
            self._logger.debug(f"{i}:")
            prime = self._primes[i]
            for j in range(len(not_filtered)):
                self._logger.debug(f"{j}:")
                print(j)
                num = not_filtered[j]
                if num not in self._primes and num % prime != 0:
                    filtered.append(num)

            not_filtered = filtered
            if len(filtered) == 0:
                break
            self.primes.append(filtered[0])
            filtered = []
            to_range = len(self._primes)
            i += 1
