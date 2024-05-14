from app.utils.input_readers import try_read_input_int


class Cli:
    @staticmethod
    # wyswietla opcje menu i wiadomosc koncowa oraz poczatkowa
    def print_menu(start_message, end_message, options):
        if start_message is not None:
            print(start_message)

        if options is None or options.__len__() == 0:
            print("Brak wybranej opcji.")

        else:
            print("Menu:\n")
            for option in options:
                print(option)

        if end_message is not None:
            print(end_message)

    @staticmethod
    def print_menu_dict(start_message, end_message, options_dict):
        if start_message is not None:
            print(start_message)

        if options_dict is None or options_dict.__len__() == 0:
            print("Brak wybranej opcji.")

        else:
            print("Menu:\n")
            for dic in options_dict:
                print(dic.__getitem__("name"))

        if end_message is not None:
            print(end_message)

    @staticmethod
    def _callback(fun, args):
        # print(args, isinstance(args, tuple))
        if args is not None and isinstance(args, tuple):
            fun(*args)

        if args is not None and not isinstance(args, tuple):
            fun(args)

        elif args is None:
            fun()

    @staticmethod
    def menu(options_dict, menu_msg, end_msg):

        opt = 0
        while opt != options_dict.__len__():
            Cli.print_menu_dict(menu_msg, "", options_dict)

            opt = try_read_input_int("Podaj numer opcji [typu calkowitego].\n")
            opt -= 1

            if opt == options_dict.__len__():
                print("Wyjscie.\n")

                if end_msg is not None:
                    print(end_msg)

                return

            elif options_dict.__len__() > 0:
                args = options_dict[opt]["func_args"]
                Cli._callback(options_dict[opt]["function"], args)

