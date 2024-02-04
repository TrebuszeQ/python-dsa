import math

from cli import Cli
from dsa.stack import Stack


# Robert Sedgewick, Kevin Wayne Algorytmy IV edycja pl, strona 141.
class DijkstraEvaluator:
    # (2 * 3 + (1 + 2) / 2)

    @staticmethod
    def _multiply(value, value2):
        return value * value2

    @staticmethod
    def _add(value, value2):
        return value + value2

    @staticmethod
    def _subtract(value, value2):
        return value - value2

    @staticmethod
    def _divide(value, value2):
        return value / value2

    @staticmethod
    def _mod(value, value2):
        return value % value2

    @staticmethod
    def _sqrt(value):
        return value ** 0.5

    @staticmethod
    def _pow(value, value2):
        return value ** value2

    @staticmethod
    def _evaluate(operators, values):
        if operators.size() == values.size():
            op = operators.pop()
            val2 = values.pop()
            val2 = values.pop()

    @staticmethod
    def _trim_empty(text):
        text.trim
    #   here


    @staticmethod
    def _traverse():
        print("Program oblicza wyrazenie arytmetyczne w nawiasach.\n")
        operators = Stack([])
        values = Stack([])

        expression = Cli.try_read_input_string("Podaj wyrazenie arytmetyczne.\n")

        i = 0
        current = 0
        active = True

        for char in expression:
            match char:
                case '(':
                    operators.push('(')

                case ')':
                    operators.push(')')

                case '-':
                    operators.push('-')
                    if active is True:


                case '+':
                    operators.push('+')

                case '*':
                    operators.push('*')

                case '/':
                    operators.push('/')

                case ':':
                    operators.push(':')

                case '%':
                    operators.push('%')

                case 'sqrt':
                    operators.push('sqrt')

                case '^':
                    operators.push('^')

                case ' ':
                    pass

                case _:
                    if char.isalnum():
                        current = char
                        values.push(char)

            i += 1

        print(operators)
        print(values)


if __name__ == '__main__':
    DijkstraEvaluator._traverse()
