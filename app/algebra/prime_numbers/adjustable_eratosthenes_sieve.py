import logging


class AdjustableEratosthenesSieve:
    @property
    def primes(self):
        return self._primes

    def __init__(self, start, end, increment):
        self._logger = logging.getLogger(__name__)
        if start > end:
            temp = start
            start = end
            end = temp
        self._start = start
        self._end = end
        self._increment = increment
        self._validate_start()
        self._validate_end()
        self._primes = []
        self.find_primes()

    def _validate_start(self):
        if self._start < 0:
            self._logger.error("Start is lesser than 0. Set to 2.")
            self._end = 2

    def _validate_end(self):
        if self._end < 0:
            self._logger.error("End is lesser than 0. Set to 2.")
            self._end = 2

    def find_primes(self):





