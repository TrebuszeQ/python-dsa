from cli import Cli
from app.dsa.stack_initable import Stack


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
    def _count_parentheses(text):
        ope = 0
        close = 0

        for char in text:
            if char == "(":
                ope += 1

            elif char == ")":
                close += 1

        return ope, close

    @staticmethod
    def _check_parentheses_parity(ope, close):
        if ope == close:
            return True

        return False

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

        priority = False
        for char in expression:
            match char:
                case '(':
                    if priority is True:
                        priority = False

                    operators.push('(')

                case ')':
                    while operators.top() != '(' and values.size() > 0:
                        value2 = values.pop()
                        value1 = values.pop()
                        values.push(DijkstraEvaluator._evaluate(operators.pop(), value1, value2))

                    operators.pop()

                case '*' | '/' | ':' | '%' | 'sqrt' | '^':
                    priority = True
                    operators.push(char)

                case '-' | '+':
                    operators.push(char)

                case _:
                    if char.isdigit() and priority is True:
                        values.push(
                            DijkstraEvaluator._evaluate(operators.pop(), values.pop(),
                                                        DijkstraEvaluator._char_to_number(char)))
                        priority = False

                    elif char.isdigit() and priority is False:
                        values.push(DijkstraEvaluator._char_to_number(char))

        return values.pop()

    @staticmethod
    def main():
        print("Program oblicza wyrazenie arytmetyczne w nawiasach.\n")
        print("Program wymaga domkniecia nawiasow.\n")
        expr = DijkstraEvaluator._trim_whitespace(DijkstraEvaluator._take_expression())
        ope, close = DijkstraEvaluator._count_parentheses(expr)

        if DijkstraEvaluator._check_parentheses_parity(ope, close):
            return DijkstraEvaluator._traverse(expr)

        else:
            print("Program wymaga parzystej ilosci nawiasow.\n")
            return False


if __name__ == '__main__':
    DijkstraEvaluator.main()

