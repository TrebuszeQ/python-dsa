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

    def __init__(self, pair1: OrderedPair, pair2: OrderedPair):
        self._pair1 = pair1
        self._pair2 = pair2
        self._product = self.__combine_collections()

    def __combine_collections(self):
        result = []

        for num1 in self._pair1.collection:
            for num2 in self._pair2.collection:
                result.append((num1, num2))

        return result




