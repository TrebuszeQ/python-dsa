# Robert Sedgewick, Kevin Wayne Algorytmy IV edycja pl, strona 144.
# stos oparty o liste
class Stack:
    def __init__(self, stack):
        if stack is None:
            self._stack = []

        else:
            self._stack = stack

    def __repr__(self):
        return f'(Stack({self._stack})'

    def push(self, elem):
        if type(self._stack) is list:
            self._stack.append(elem)

        elif type(self._stack) is tuple:
            self._stack[len(self._stack)] = elem

        return self._stack

    # # here
    # def _push_multiple(self, multi):
    #     if self.empty():
    #         self._stack = [multi]

    def pop(self):
        pass

    def empty(self):
        if self._stack is None:
            return True

        else:
            return False

    def size(self):
        return len(self._stack)

    def top(self):
        pass

    def peek(self):
        pass
