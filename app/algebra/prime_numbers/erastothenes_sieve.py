import logging


class ErastothenesSieve:
    def __init__(self, start, end, increment=1):
        self.logger = logging.getLogger(__name__)
        self._start = start
        self._end = end
        self._validate_start()
        self._increment = increment
        self.primes = []
        self.sieve = []
        self._sieve_size = end - start

    def _validate_start(self):
        if self._start < 2:
            self._start = 2
            self.logger.error("Start is less than 2. Set to 2.")

        if self._start > self._end >= 2:
            self.logger.error("Start is greater than end, inverting.")
            self._end = self._start

        else:
            self.logger.error("Start is greater than end, inverting.")
            self._end = self._start
            self.logger.error("End increased by 2")
            self._end += 2

    def find_primes(self):
        for i in range(self._start, self._end, self._increment):
            self.primes.append(i)
