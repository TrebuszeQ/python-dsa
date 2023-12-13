
class BubbleSort:
    def __init__(self):
        pass

    # worst case O(N^2), in place, stable
    @staticmethod
    def sort(lis: list):
        if lis.__len__().__gt__(1):
            counter = 1

            for i in range(len(lis)):
                j = i + 1
                for j in range(len(lis)):
                    if (j + 1).__lt__(len(lis)) and lis[j].__gt__(lis[i]):
                        lis[i], lis[j] = lis[j], lis[i]

        return lis
