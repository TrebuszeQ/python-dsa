from cli import Cli
from dsa.stack import Stack


# Robert Sedgewick, Kevin Wayne Algorytmy IV edycja pl, strona 141.
class DijkstraEvaluator:
    @staticmethod
    def matcher(char):
        match char:
            case '(', ')', '-', '+', '*', '/', ':', '%', 'sqrt', '^': return True

    @staticmethod
    def evaluate():
        print("Program oblicza wyrazenie arytmetyczne w nawiasach.\n")
        operator_stack = Stack(())
        value_stack = Stack(())

        expression = Cli.try_read_input_string("Podaj wyrazenie arytmetyczne.\n")

        for char in expression:
            match char:
                case '(', ')': pass
                case '-': pass
                case '+': pass
                case '*': pass
                case '/': pass
                case ':': pass
                case '%': pass
                case 'sqrt': pass
                case '^': pass
        