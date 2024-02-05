import math

from cli import Cli
from dsa.stack import Stack


# Robert Sedgewick, Kevin Wayne Algorytmy IV edycja pl, strona 141.
class DijkstraEvaluator:
    # (2 * 3 + (1 + 2) / 2)

    @staticmethod
    def _evaluate(operators, values):

        eval_values = Stack(())

        if len(operators) > len(values):
            for i in range(len(values)):
                op = operators[i]

                match op:
                    case '-':
                        eval_values.push(values[i] - values[i + 1])

                    case '+':
                        eval_values.push(values[i] + values[i + 1])

                    case '*':
                        eval_values.push(values[i] * values[i + 1])

                    case '/':
                        eval_values.push(values[i] / values[i + 1])

                    case ':':
                        eval_values.push(values[i] / values[i + 1])

                    case '%':
                        eval_values.push(values[i] % values[i + 1])

                    case 'sqrt':
                        eval_values.push(values[i] ** values[i + 1])

                    case '^':
                        eval_values.push(math.pow(values[i], values[i + 1]))

        elif len(values) > len(operators):
            pass

        else:
            pass

    @staticmethod
    def _trim_empty(text):
        return text.replace(' ', '')

    @staticmethod
    def _traverse():
        print("Program oblicza wyrazenie arytmetyczne w nawiasach.\n")
        operators = Stack([])
        values = Stack([])

        expression = DijkstraEvaluator._trim_empty(Cli.try_read_input_string("Podaj wyrazenie arytmetyczne.\n"))

        i = 0
        active = True

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
                    if char.isalnum():
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

