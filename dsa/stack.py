# Robert Sedgewick, Kevin Wayne Algorytmy IV edycja pl, strona 144.
# stos oparty o liste
class Stack:
    def __init__(self, lis):
        if lis is None:
            self.arr = None

        else:
            self.arr = lis

    def push(self, elem):
        if self.empty():
            self.arr = [elem]

        else:
            self.arr[self.arr.__len__()] = elem

        return self.arr

    # here
    def _push_multiple(self, multi):
        if self.empty():
            self.arr = [multi]

    def pop(self):
        pass

    def empty(self):
        if self.arr is None:
            return True

        else:
            return False

    def size(self):
        pass

    def top(self):
        pass

    def peek(self):
        pass
