from cli import Cli


class LeapYear(object):

    # funkcja zwraca rok integer
    # 4a)
    @staticmethod
    def take_year():
        return Cli.try_read_input_int("Podaj numer roku:\n")

    # funkcja sprawdza czy rok jest przestepny
    # 4b)
    @staticmethod
    def is_leap_year(year):
        if ((year.__mod__(4) == 0) and (year.__mod__(100) > 0)) or year.__mod__(400) == 0:
            return True

        else:
            return False

    @staticmethod
    def print_is_leap_year(year, truth):
        if truth:
            print("Rok %i jest przestepny.\n" % year)

        else:
            print("Rok %i nie jest przestepny.\n" % year)

    # funkcja glowna
    # 4d)
    @staticmethod
    def main():

        while True:
            print("Program podaje informacje, czy rok jest przestepny.\n")
            year = LeapYear.take_year()

            if year <= 0:
                print("Rok wynosi 0 lub mniej.\n")

            else:
                LeapYear.print_is_leap_year(year, LeapYear.is_leap_year(year))



