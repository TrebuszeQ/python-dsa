from dataclasses import dataclass


@dataclass(repr=True)
class HardcodedOta:

    @property
    def c(self):
        return self._c

    @property
    def value(self):
        return self._value

    def __init__(self, arr: list[float]):
        _c = [None] * len(arr)
        self.populate_cs(arr)
        self._value = _c[0] + _c[1] *

    def set_c(self, arr: list[float]):
        for i in range(len(arr)):
            c = self._c
            num = arr[i]
            c[i] = num if i == 0 else num - arr[i - 1]
            return c

