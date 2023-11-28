
class BubbleSort:
    def __init__(self, lis):
        self.lis: [int] = lis

    def sort(self):
        if self.lis.__len__().__gt__(2):
            counter = 1
            for ind in self.lis:
                if self.lis[counter] is not None and ind > ind[counter]:
                    self.lis[counter - 1], self.lis[counter] = self.lis[counter], self.lis[counter - 1]
                counter += 1
        else:
            return self.lis

