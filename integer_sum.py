from cli import Cli


class IntegerSum:
    # b)
    @staticmethod
    def _sum_integer_len(value):
        sumi = 0
        value_str = value.__str__()

        if value_str.__len__().__gt__(1):
            for i in value_str:
                sumi += int(i)

        else:
            return value
        
        return sumi

    # c)
    @staticmethod
    def _print_sum(value):
        print(f"Suma wynosi {value}.\n")

    # d)
    @staticmethod
    def cls_main():
        # Cli.try_read_input_int() == a)
        sumi = IntegerSum._sum_integer_len(Cli.try_read_input_int("Podaj liczbe calkowita.\n"))
        IntegerSum._print_sum(sumi)


if __name__ == '__main__':
    IntegerSum.cls_main()



