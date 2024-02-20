class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return (f'<{type(self).__name__}\n'
                f'self.data {self.data}\n'
                f'self.next {self.next}\n'
                f'at 0x{id(self):x}>')


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def __repr__(self):
        nodes = []
        while self.head is not None:
            nodes.append(self.head.data)
            self.head = self.head.next

        nodes.append('None')
        " -> ".join(nodes)
        return f'<{type(self).__name__} at 0x{id(self):x}'

    def insert_head(self, data):
        self.head, self.head.next = Node(data), self.head






