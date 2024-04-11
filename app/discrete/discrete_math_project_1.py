from dataclasses import dataclass
from app.dsa.random_int_array import gen_1d_random_int_array


@dataclass(repr=True)
class DiscreteMathProject:
    @property
    def sequence(self):
        return self._sequence

    def __init__(self):
        self._sequence = gen_1d_random_int_array(8, 1, 50)
        self._sequence.sort()
        print(self._sequence)
