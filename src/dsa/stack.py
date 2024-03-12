
class Stack:
    def __init__(self):
        self._stack = []

    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>'

    def __len__(self):
        return len(self._stack)

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def empty(self):
        return self.__len__() == 0

    def top(self):
        if not self.empty():
            return self._stack[len(self) - 1]

        else:
            return None

    def peek(self):
        if not self.empty():
            return self._stack[0]

        else:
            return None
