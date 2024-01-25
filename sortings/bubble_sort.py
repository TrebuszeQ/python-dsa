
class BubbleSort:
    # worst case O(N^2), in place, stable
    @staticmethod
    def sort(lis):
        if lis.__len__().__gt__(1):
            for i in range(len(lis)):
                j = i + 1
                for j in range(len(lis)):
                    if (j + 1).__lt__(len(lis)) and lis[j].__gt__(lis[i]):
                        lis[i], lis[j] = lis[j], lis[i]

        print(lis, "\n")
        return lis

    @staticmethod
    def sort_count(lis):
        comp_count = 0
        swap_count = 0

        if lis.__len__().__gt__(1):

            for i in range(len(lis)):
                j = i + 1
                for j in range(len(lis)):
                    if (j + 1).__lt__(len(lis)) and lis[j].__gt__(lis[i]):
                        lis[i], lis[j] = lis[j], lis[i]
                        comp_count += 1

        return lis, comp_count
