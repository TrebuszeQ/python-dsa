import threading
from math import sin
from datetime import datetime
from time import time
from freezegun import freeze_time
from threading import Timer

# my
from cli import Cli
from leap_year import LeapYear
from electricity_randomizer import ElectricityRandomizer


class ElectricityUsage:

    # True eq taryfa I
    # False eq taryfa II
    @staticmethod
    def _get_zone(hour):
        if (5 <= hour < 13) or (15 <= hour < 22):
            return True

        else:
            return False

    @staticmethod
    def _get_electricity_usage_i(power, power_passive, power_sum_i, power_passive_sum_i):
        return [power + power_sum_i, power_passive + power_passive_sum_i]

    @staticmethod
    def _get_electricity_usage_ii(power, power_passive, power_sum_ii, power_passive_sum_ii):
        return [power + power_sum_ii, power_passive + power_passive_sum_ii]

    @staticmethod
    def _print_results(power_sum_i, power_sum_ii, power_passive_sum_i, power_passive_sum_ii, max_power_last_month):
        print(f"Sumaryczne zyżycie energii czynnej w taryfie I:\n {power_sum_i}.\n"
              f"Sumaryczne zyżycie energii biernej w taryfie I:\n {power_passive_sum_i}.\n"
              f"Sumaryczne zyżycie energii czynnej w taryfie II:\n {power_sum_ii}.\n"
              f"Sumaryczne zyżycie energii biernej w taryfie II:\n {power_passive_sum_ii}.\n"
              f"Maksymalna moc czynna pobrana w minionym miesiącu:\n {max_power_last_month}.\n")

    @staticmethod
    async def _set_interval(func):
        timer = Timer(1.00, func)
        timer.start()

    # here
    @staticmethod
    def count():
        ElectricityUsage._set_interval(ElectricityUsage.main())

    @staticmethod
    def main(started=False, power_max=-1, power_sum_i=0, power_sum_ii=0, power_passive_sum_i=0, power_passive_sum_ii=0):
        if started is False or None:
            ElectricityUsage.set_interval(ElectricityUsage.main(True))

        else:
            power, power_passive, date, hour = ElectricityRandomizer.get_bulk()

            if date.month == 1:
                power_sum_i, power_passive_sum_i, power_sum_ii, power_passive_sum_ii, power_max = [0, 0, 0, 0, 0]

            if power_max == -1 and power > power_max:
                power_max = power

            if ElectricityUsage._get_zone(hour) is True:
                power_sum_i, power_passive_sum_i = ElectricityUsage._get_electricity_usage_i(power,
                                                                                             power_passive,
                                                                                             power_sum_i,
                                                                                             power_passive_sum_i)
            else:
                power_sum_ii, power_passive_sum_ii = ElectricityUsage._get_electricity_usage_i(power,
                                                                                               power_passive,
                                                                                               power_sum_ii,
                                                                                               power_passive_sum_ii)
            ElectricityUsage._print_results(power_sum_i, power_sum_ii, power_passive_sum_i, power_passive_sum_ii, power_max)

            return [power_sum_i, power_sum_ii, power_passive_sum_i, power_passive_sum_ii, power_max]


if __name__ == "__main__":
    ElectricityUsage.main()
