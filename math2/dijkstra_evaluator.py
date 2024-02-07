import math

from cli import Cli
from dsa.stack import Stack


# Robert Sedgewick, Kevin Wayne Algorytmy IV edycja pl, strona 141.
class DijkstraEvaluator:
    # (2 * 3 + (1 + 2) / 2)

    @staticmethod
    def _evaluate(operator, val1, val2):
        operations = (
            {"name": "+", "operation": val1 + val2},
            {"name": "-", "operation": val1 - val2},
            {"name": "*", "operation": val1 * val2},
            {"name": "/", "operation": val1 / val2},
            {"name": ":", "operation": val1 / val2},
            {"name": "%", "operation": val1 % val2},
            {"name": "sqrt", "operation": val1 ** (val2/2)},
            {"name": "^", "operation": val1 ** val2},
            {"name": "pow", "operation": val1 ** val2},
        )

        for op in operations:
            if op["name"] == operator:
                return op

    @staticmethod
    def _trim_empty(text):
        return text.replace(' ', '')

    @staticmethod
    def _traverse():
        operators = Stack([])
        values = Stack([])

        expression = DijkstraEvaluator._trim_empty(Cli.try_read_input_string("Podaj wyrazenie arytmetyczne.\n"))

        result = 0

        for char in expression:
            match char:
                case '(':
                    operators.push('(')

                case ')':
                    while operators.peek() != '(':
                        value2 = values.pop()
                        value1 = values.pop()
                        result = DijkstraEvaluator._evaluate(operators.pop(), value1, value2)

                    operators.pop()
                    values.push(result)

                case '-' | '+' | '*' | '/' | ':' | '%' | 'sqrt' | '^':
                    operators.push(char)

                case _:
                    if char.isalnum():
                        values.push(char)

        print(operators)
        print(values)
        return result

    @staticmethod
    def main():
        print("Program oblicza wyrazenie arytmetyczne w nawiasach.\n")


if __name__ == '__main__':
    DijkstraEvaluator._traverse()

