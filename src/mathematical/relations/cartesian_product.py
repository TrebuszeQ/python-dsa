from dataclasses import dataclass
from src.mathematical.relations.ordered_pair import OrderedPair


@dataclass(repr=True)
class CartesianProduct:
    @property
    def ordered_pairs(self):
        return self._ordered_pairs

    def __init__(self, ordered_pairs: [OrderedPair]):
        self._ordered_pairs = ordered_pairs

    def _of_two_sets(self):
        result = []
        set1 = self._ordered_pairs[0]
        set2 = self._ordered_pairs[1]

        for num1 in set1.collection:
            for num2 in set2.collection:
                result.append((num1, num2))

        return result

    def _of_three_sets(self):
        set1 = self._ordered_pairs[0]
        set2 = self._ordered_pairs[1]
        set3 = self._ordered_pairs[2]

        cords = []

        for num1 in set1.collection:
            for num2 in set2.collection:
                for num3 in set3.collection:
                    cords.append([num1, num2, num3])

        return cords




