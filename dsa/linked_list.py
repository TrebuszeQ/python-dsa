from linked_list_node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x}'

    def insert_head(self, data):
        new_node = Node(data)




