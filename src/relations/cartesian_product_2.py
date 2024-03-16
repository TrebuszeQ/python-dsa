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

       # cords = (i, j, k+1)
       #
       #  cords2 = (i, j, k)
       #  cords3 = (i + 3, j, k)
       #  cords4 = (i + 1)


        for i in range(pairs.len - 1):
            leading_pair = pairs[i]
            npair = pairs[n]

            while n != 0 and n != i:
                j = 0
                cords.__add__(leading_pair[j])

                for num in npair:
                    cords.__add__(leading_pair)
                    leading_pair[j]
                n -= 1

        return result


    # przechodzi przez wszystkie pary,
    # dodaje pierwsza liczbe z pair._collection do cords
    # dochodzi do ostatniej pary
    # dla kazdej liczby z drugiej pary dodaje cords i = 0 j++ i = 1
    # 



