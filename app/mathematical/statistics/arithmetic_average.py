from dataclasses import dataclass


@dataclass
class ArithmeticAverage:

    @property
    def degree(self):
        return self.degree

    @property
    def value(self):
        return self._value

    def __init__(self, collection: [float]):
        self._degree = len(collection)
        self._value = self.__sigma(collection)

    def __sigma(self, collection: [float]):
        sigma = 0
        for num in collection:
            sigma += num

        return sigma * 1/self._degree

