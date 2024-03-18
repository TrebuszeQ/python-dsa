from dataclasses import dataclass
from src.relations.ordered_pair import OrderedPair


@dataclass(repr=True)
class CartesianProduct2:
    @property
    def ordered_pairs(self):
        return self._ordered_pairs

    @property
    def product(self):
        return self._product

    def __init__(self, ordered_pairs: [OrderedPair]):
        self._ordered_pairs = ordered_pairs
        self._product = self.__combine_collections()

    def __combine_collections(self):
        result = []
        cords = ()
        pairs = self._ordered_pairs
        n = pairs.__len__()

        leading_pair = pairs[0].collection
        # i++
        for num in leading_pair:
            cord = (num)
            # j - next pair counter
            j = 1
            # k - in next pair counter
            k = 0

            # j++
            next_collection = pairs[j].collection
            while j != n and j != next_collection.len:
                cord.__append__(pairs[j].collection[k])
                j += 1

            # k++
            last_collection = pairs[n].collection
            while j == n and k != last_collection.len:
                cord.__append__(last_collection[k])
                k += 1

            k = 0
            cords.__add__(cord)

        return result


    # przechodzi przez wszystkie pary,
    # dodaje pierwsza liczbe z pair._collection do cords
    # dochodzi do ostatniej pary
    # dla kazdej liczby z drugiej pary dodaje cords i = 0 j++ i = 1
    # 



