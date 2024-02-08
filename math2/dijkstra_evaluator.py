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
                return op["operation"]

    @staticmethod
    def _trim_whitespace(text):
        return text.replace(' ', '')

    @staticmethod
    def _char_to_number(char):
        if char.isdigit():
            return int(char)

        return ord(char)

    @staticmethod
    def _take_expression():
        return DijkstraEvaluator._trim_whitespace(Cli.try_read_input_string("Podaj wyrazenie arytmetyczne.\n"))

    @staticmethod
    def _traverse(expression):
        operators = Stack([])
        values = Stack([])

        result = 0
        precedense = False
        for char in expression:
            match char:
                case '(':
                    operators.push('(')

                case ')':
                    while operators.top() != '(' and values.size() > 0:
                        value2 = values.pop()
                        value1 = values.pop()
                        values.push(DijkstraEvaluator._evaluate(operators.pop(), value1, value2))

                    operators.pop()

                case '*' | '/' | ':' | '%' | 'sqrt' | '^':
                    precedense = True
                    operators.push(char)

                case '-' | '+':
                    operators.push(char)

                case _:
                    if char.isalnum() and precedense is True:
                        values.push(DijkstraEvaluator._evaluate(operators.pop(), values.pop(), DijkstraEvaluator._char_to_number(char)))
                        precedense = False

                    if char.isalnum() and precedense is not True:
                        values.push(DijkstraEvaluator._char_to_number(char))

        return result

    @staticmethod
    def main():
        print("Program oblicza wyrazenie arytmetyczne w nawiasach.\n")
        return DijkstraEvaluator._traverse(DijkstraEvaluator._trim_whitespace(DijkstraEvaluator._take_expression()))


if __name__ == '__main__':
    DijkstraEvaluator.main()

