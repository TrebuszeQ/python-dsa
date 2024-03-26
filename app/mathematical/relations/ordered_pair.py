from dataclasses import dataclass


@dataclass(repr=True)
class OrderedPair(list):

    @property
    def predecessor(self):
        return self._predecessor

    @property
    def successor(self):
        return self._successor

    @property
    def pair(self):
        return [self._predecessor, self._successor]

    @property
    def collection(self):
        return self._collection

    def __init__(self, predecessor, successor):
        super().__init__()

        if successor < predecessor:
            self._successor, self._predecessor = predecessor, successor

        self._successor, self._predecessor = successor, predecessor

        self._collection = self.__populate_collection()

    def __populate_collection(self):
        i = self.predecessor
        collection = []

        while True:
            collection.append(i)
            i += 1
            if collection.__len__() > self._successor - self._predecessor:
                return collection
