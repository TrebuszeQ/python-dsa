class Stack:
    def __init__(self, stack):
        if type(stack) is list:
            Stack._copy_list(self, stack)

        elif stack is None:
            self._stack = []

        else:
            self._stack = stack

    def __repr__(self):
        return f'(Stack({self._stack})'

    def _copy_list(self, lis):
        self._stack = []
        for item in lis:
            self._stack.append(item)

        return self._stack

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
        return self._stack.pop()

    def empty(self):
        if self._stack is None or len(self._stack) == 0:
            return True

        else:
            return False

    def size(self):
        return len(self._stack)

    def top(self):
        return self._stack[len(self._stack)-1]

    def peek(self):
        return self._stack[0]
