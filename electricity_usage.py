import asyncio
import threading
from math import sin
from datetime import datetime
from time import time, sleep
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
    def _get_tariff(hour):
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
    def _is_new_month(date):
        if date.day == 1:
            return True

    @staticmethod
    def _is_new_year(date, time_passed):
        if LeapYear.is_leap_year(date.year):
            year_seconds = 31622400

        else:
            year_seconds = 31536000

        if time_passed == year_seconds:
            return True

        else:
            return False

    # counts powers and time
    @staticmethod
    async def _count_powers(power, power_passive, tariff, power_max=-1, power_sum_i=0, power_sum_ii=0, power_passive_sum_i=0,
                            power_passive_sum_ii=0):

        if power_max == -1 and power > power_max:
            power_max = power

        if tariff:
            power_sum_i, power_passive_sum_i = ElectricityUsage._get_electricity_usage_i(power,
                                                                                         power_passive,
                                                                                         power_sum_i,
                                                                                         power_passive_sum_i)
        else:
            power_sum_ii, power_passive_sum_ii = ElectricityUsage._get_electricity_usage_i(power,
                                                                                           power_passive,
                                                                                           power_sum_ii,
                                                                                           power_passive_sum_ii)

        ElectricityUsage._print_results(power_sum_i, power_sum_ii, power_passive_sum_i, power_passive_sum_ii,
                                        power_max)

        return [power_max, power_sum_i, power_sum_ii, power_passive_sum_i, power_passive_sum_ii]

    # here
    @staticmethod
    def main(time_passed=0, values=None):
        power, power_passive, date, hour = ElectricityRandomizer.get_bulk()

        if time_passed == 0:
            tariff, power_max, power_sum_i, power_sum_ii, power_passive_sum_i, power_passive_sum_ii = (
                ElectricityUsage._get_tariff(hour), power, 0, 0, 0, 0)

        if ElectricityUsage._is_new_month(date) and ElectricityUsage._is_new_year(date, time_passed):
            return values

        elif ElectricityUsage._is_new_month(date):
            values = [power, power_passive, ElectricityUsage._get_tariff(hour), power, 0, 0, 0]

        if time_passed == 0:
            values = ElectricityUsage._count_powers(power, power_passive, tariff, power_max, power_sum_i, power_sum_ii, power_passive_sum_i,
                            power_passive_sum_ii)
        sleep(1)
        time_passed += 1
        ElectricityUsage.main()


if __name__ == "__main__":
    ElectricityUsage.main()
