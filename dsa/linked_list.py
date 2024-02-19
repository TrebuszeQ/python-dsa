class LinkedList:
    class Node:
        def __init__(self, data):
            self.Node = data
            self.next: LinkedList.Node | None = None

        def __repr__(self):
            return f'<{type(self).__name__} at 0x{id(self):x}>'

    def __init__(self, data):
        self.head = self.Node(data)

    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x}'

    def insert_head(self, data):
        self.head = self.Node(data)






