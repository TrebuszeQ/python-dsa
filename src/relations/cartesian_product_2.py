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
        cords = []
        pairs = self._ordered_pairs
        n = pairs.__len__()

        leading_pair = pairs[0].collection
        # i++
        for num in leading_pair:
            cord = [num]
            # j - next pair counter
            j = 1
            # k - in next pair counter
            k = 0

            # j++
            next_collection = pairs[j].collection
            while j != n - 1 and j != next_collection.__len__():
                cord.append(pairs[j].collection[k])
                j += 1
                if j == next_collection.__len__():
                    j = 0

            # k++
            last_collection = pairs[n - 1].collection
            while j == n - 1 and k != last_collection.__len__():
                cord.append(last_collection[k])
                k += 1
                if j == last_collection.__len__():
                    k = 0

            cords.append(cord)

        return result
    def __combine_collections(self):
        cords = []
        pairs = self._ordered_pairs
        n = pairs.__len__()
        counters = []
        for pair in pairs:
            counters.append(0)

        for pair in pairs:
            lead_counter = counters[0]
            last_counter = counters[counters.__len__() - 1]

            lead_node = pairs[0]
            lead_collection = lead_node.collection

            last_node = pairs[last_counter]

            cords.append(lead_collection[lead_counter])
            lead_counter += 1
            counters[lead_counter] += 1

            if lead_node == last_node:
                lead_counter = 0



        return cords

