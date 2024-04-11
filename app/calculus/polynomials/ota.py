from dataclasses import dataclass


# bit-polynomial function

@dataclass(repr=True)
class Ota:
    @property
    def degree(self):
        return self.degree

    def __init__(self, arr: [float]):
        self._degree = len(arr)
        