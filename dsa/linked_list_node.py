
class Node:
    def __init__(self):
        self.item: Node
        self.next: Node

    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x}>'

