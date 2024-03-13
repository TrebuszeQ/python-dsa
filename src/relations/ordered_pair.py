from dataclasses import dataclass


@dataclass(repr=True)
class OrderedPair:

    @property
    def predecessor(self):
        return self._successor

    @property
    def successor(self):
        return self._successor

    @property
    def ordered_pair(self):
        return [self._predecessor, self._successor]

    @property
    def collection(self):
        return self._collection

    @predecessor.setter
    def predecessor(self, value):
        self._predecessor = value

    @successor.setter
    def successor(self, value):
        self._successor = value

    # here
    @collection.setter
    def collection(self, value):
        while value != 0:
            self._collection[value - 1] = value
            value -= 1

    def __init__(self, predecessor, successor):
        self._collection = successor
        if successor < predecessor:
            self._successor = predecessor
            self._predecessor = successor

        else:
            self._successor = successor
            self._predecessor = predecessor


