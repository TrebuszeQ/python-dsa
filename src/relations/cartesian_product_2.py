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
        self._product = self._combine_collections()

    def _of_two_sets(self):
        result = []
        set1 = self._ordered_pairs[0]
        set2 = self._ordered_pairs[1]

        for num1 in set1.collection:
            for num2 in set2.collection:
                result.append((num1, num2))

        return result


    # def __combine_collections(self):
    #     result = []
    #     cords = []
    #     pairs = self._ordered_pairs
    #     n = pairs.__len__()
    #
    #     leading_pair = pairs[0].collection
    #     # i++
    #     for num in leading_pair:
    #         cord = [num]
    #         # j - next pair counter
    #         j = 1
    #         # k - in next pair counter
    #         k = 0
    #
    #         # j++
    #         next_collection = pairs[j].collection
    #         while j != n - 1 and j != next_collection.__len__():
    #             cord.append(pairs[j].collection[k])
    #             j += 1
    #             if j == next_collection.__len__():
    #                 j = 0
    #
    #         # k++
    #         last_collection = pairs[n - 1].collection
    #         while j == n - 1 and k != last_collection.__len__():
    #             cord.append(last_collection[k])
    #             k += 1
    #             if j == last_collection.__len__():
    #                 k = 0
    #
    #         cords.append(cord)
    #
    #     return result

    # def _combine_collections(self):
    #     cords = []
    #     pairs = self._ordered_pairs
    #     counters = []
    #     final_counters = []
    #     for pair in pairs:
    #         counters.append(0)
    #         final_counters.append(pair.collection.__len__() - 1)
    #
    #     while counters != final_counters:
    #         j = counters.__len__() - 1
    #         lead_counter = counters[0]
    #         focal_counter = counters[j]
    #
    #         # i
    #         i = 0
    #         cord = []
    #         for pair in pairs:
    #             cord.append(pair.collection[counters[i]])
    #             i += 1
    #
    #         cords.append(cord)
    #         if j == 0:
    #             j = counters.__len__() - 1
    #
    #         elif focal_counter == final_counters[j]:
    #             counters[j] = 0
    #             j -= 1
    #
    #         else:
    #             counters[j] += 1
    #
    #     return cords

    def _of_three_sets(self):
        set1 = self._ordered_pairs[0]
        set2 = self._ordered_pairs[1]
        set3 = self._ordered_pairs[2]

        iterations = set1.collection.__len__() * set2.collection.__len__() * set3.collection.__len__()

        j, k, l = 0, 0, 0
        counters = [j, k, l]
        iter = 1
        cords = [counters]
        cord = []

        for iter in range(iterations):
            # 2 4 6 8
            if iter % 2 == 0:
                l += 1

            # 3 5 7
            elif iter != 1:
                l -= 1

            # 5





