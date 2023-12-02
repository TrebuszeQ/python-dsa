
class BubbleSort:
    def __init__(self, lis):
        self.lis: [int] = lis

    def sort(self):
        lis = self.lis
        if lis.__len__().__gt__(1):
            counter = 1

            for i in range(len(lis)):
                j = i + 1
                for j in range(len(lis)):
                    if (j + 1).__lt__(len(lis)) and lis[i].__gt(lis[j]):
                        lis[i], lis[j] = lis[j], lis[i]
        return lis
