import logging


class EratosthenesSieve:
    @property
    def primes(self):
        return self._primes

    def __init__(self, end):
        self._logger = logging.getLogger(__name__)
        self._end = end
        self._validate_end()
        self._primes = [2]
        self.find_primes()

    def _validate_end(self):
        if self._end < 2:
            self._logger.error("End is lesser than 2. Set to 2.")
            self._end = 2

    def find_primes(self):
        not_filtered = [i for i in range(2, self._end)]
        filtered = []
        to_range = len(self._primes)

        i = 0
        while i <= to_range:
            prime = self._primes[i]
            for j in range(len(not_filtered)):
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



