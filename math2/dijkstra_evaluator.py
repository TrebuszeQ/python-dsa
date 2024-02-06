import math

from cli import Cli
from dsa.stack import Stack


# Robert Sedgewick, Kevin Wayne Algorytmy IV edycja pl, strona 141.
class DijkstraEvaluator:
    # (2 * 3 + (1 + 2) / 2)

    @staticmethod
    def _evaluate(operation, val1, val2):
        operations = (
            {"name": "add", "operation": lambda: val1 + val2},
            {"name": "sub", "operation": lambda: val1 - val2},
            {"name": "mul", "operation": lambda: val1 * val2},
            {"name": "div", "operation": lambda: val1 / val2},
            {"name": "mod", "operation": lambda: val1 % val2},
            {"name": "sqrt", "operation": lambda: val1 ** (val2/2)},
            {"name": "pow", "operation": lambda: val1 ** val2},
        )

        return 

    @staticmethod
    def _eval_matcher2(char, val1, val2, callback):

        match char:
            case '-':
                return callback(callbackval1, val2)

            case '+':
                return val1 + val2

            case '*':
                return val1 * val2

            case '/':
                return val1 / val2

            case ':':
                return val1 / val2

            case '%':
                return val1 % val2

            case 'sqrt':
                return val1 ** (val2 / 2)

            case '^':
                return val1 ** val2

            case _:
                return None

    @staticmethod
    def _eval_matcher(char, val1, val2):
        match char:
            case '-':
                return val1 - val2

            case '+':
                return val1 + val2

            case '*':
                return val1 * val2

            case '/':
                return val1 / val2

            case ':':
                return val1 / val2

            case '%':
                return val1 % val2

            case 'sqrt':
                return val1 ** (val2 / 2)

            case '^':
                return val1 ** val2

            case _:
                return None

    @staticmethod
    def _trim_empty(text):
        return text.replace(' ', '')

    @staticmethod
    def _traverse():
        print("Program oblicza wyrazenie arytmetyczne w nawiasach.\n")
        operators = Stack([])
        values = Stack([])

        expression = DijkstraEvaluator._trim_empty(Cli.try_read_input_string("Podaj wyrazenie arytmetyczne.\n"))

        result = 0
        i = 0
        op_active = True

        for char in expression:
            match char:
                case '(':
                    operators.push('(')

                case ')':
                    operators.push(')')

                case '-':
                    operators.push('-')

                case '+':
                    operators.push('+')

                case '*':
                    operators.push('*')
                    op_active = True

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

                case _:
                    if char.isalnum() and op_active is True:
                        op = operators.pop()
                        result = values.pop() * values.pop()
                        values.push(result)

                    else:
                        values.push(char)

            i += 1

        print(operators)
        print(values)

    # @staticmethod
    # def _multiply(value, value2):
    #     return value * value2
    #
    # @staticmethod
    # def _add(value, value2):
    #     return value + value2
    #
    # @staticmethod
    # def _subtract(value, value2):
    #     return value - value2
    #
    # @staticmethod
    # def _divide(value, value2):
    #     return value / value2
    #
    # @staticmethod
    # def _mod(value, value2):
    #     return value % value2
    #
    # @staticmethod
    # def _sqrt(value):
    #     return value ** 0.5
    #
    # @staticmethod
    # def _pow(value, value2):
    #     return value ** value2
if __name__ == '__main__':
    DijkstraEvaluator._traverse()

