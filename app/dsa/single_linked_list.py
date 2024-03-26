from dataclasses import dataclass


@dataclass(repr=True)
class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None


@dataclass(repr=True)
class SingleLinkedList:
    head = None
    tail = None
    n = 0

    def __init__(self):
        self.head = None
        self.tail = None
        n = 0

    def empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def push_tail(self, item):
        if self.n == 0:
            self.head = self.tail = Node(item)

        elif self.n == 1:
            self.head = self.tail
            self.tail = Node(item)
            self.tail.next = self.head

        else:
            old_tail = self.tail
            self.tail = Node(item)
            self.tail.next = old_tail

        self.n += 1

    def push_head(self, item):
        if self.n >= 1:
            self.head.next = Node(item)
            self.head = self.head.next
            self.n += 1

        else:
            self.push_tail(item)

    






