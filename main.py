from cli import Cli

if __name__ == '__main__':
    opts = ("1. Struktury i typy danych.\n",
            "2. Sortowanie.\n",
            "3. Matematyczne.\n",
            "4. Data.\n",
            "5. Rozne.\n",
            "6. Wyjscie.\n")

    Cli.print_menu("Struktury danych i algorytmy.\n", "", opts)

    opt = 0
    while opt != opts.__len__():
        opt = Cli.try_read_input_int("Podaj numer opcji [typu calkowitego].\n")

        
