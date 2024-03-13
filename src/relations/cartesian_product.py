from dataclasses import dataclass
from src.relations.ordered_pair import OrderedPair


@dataclass(repr=True)
class CartesianProduct:
    @property
    def pair1(self):
        return self._pair1

    @property
    def pair2(self):
        return self._pair2

    @property
    def product(self):
        return self._product

    @pair1.setter
    def pair1(self, value):
        self._pair1 = value

    @pair2.setter
    def pair2(self, value):
        self._pair2 = value

    @product.setter
    def product(self, value):
        self._product = value

    def __init__(self, pair1: OrderedPair, pair2: OrderedPair):
        self._pair1 = pair1
        self._pair2 = pair2
        self._product = self._combine_collections()

    def _combine_collections(self):
        size = self.pair1.collection.__sizeof__() if self.pair2.collection.__sizeof__() > self.pair2.collection.__sizeof__() else self.pair2.collection.__sizeof__()
        result = []

        for i in range(size):
            num = self.pair1.collection[i]
            num2 = self.pair2.collection[i]

            if num2 is None or num < num2:
                result.append(num)

            elif num is None or num > num2:
                result.append(num2)

        return result




