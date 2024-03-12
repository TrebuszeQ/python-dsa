from dataclasses import dataclass

@dataclass(repr=True)
class OrderedPair:
    @property
    def successor(self):
        return self.successor

    @successor.setter
    def successor(self, value):
        self._successor = value

    @property
    def predecessor(self):
        return self.successor

    @predecessor.setter
    def predecessor(self, value):
        self._predecessor = value

    @property
    def ordered_pair(self):
        return [self.successor, self.predecessor]

    def __init__(self, successor, predecessor):
        if successor > predecessor:
            self.successor = predecessor
            self.predecessor = successor

        else:
            self.successor = successor
            self.predecessor = predecessor


@dataclass(repr=True)
class CartesianProduct:
    @property
    def predecessor_collection(self):
        return self.predecessor_collection

    @predecessor_collection.setter
    def predecessor_collection(self):
        for i in range()

    def __init__(self, predecessor, successor):
        self.successor = OrderedPair.successor
        self.predecessor = OrderedPair.predecessor
        self.orderd_pair: OrderedPair()

        for i in range(self.predecessor):




