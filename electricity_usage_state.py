import threading
from math import sin
from datetime import datetime
from time import time
from freezegun import freeze_time
from threading import Timer
from leap_year import LeapYear
# my
from cli import Cli


class ElectricityUsageState:
    _started = False
    _start = None
    _year = None
    _is_leap_year = None
    _month = None
    _day = None
    _passed_sec = 0
    _power = 0
    _power_passive = 0
    _power_passive_sum_i = 0
    _power_passive_sum_ii = 0
    _power_sum_i = 0
    _power_sum_ii = 0
    _last_month_max_passive_sum = 0

    def __init__(self, start, power):
        _started = True
        _start = start
        _year = datetime.year
        _month = datetime.month
        _day = datetime.day
        _power = power
        _power_passive = power * 0.1

    @staticmethod
    async def _set_func_interval(func):
        timer = Timer(1.00, func)
        timer.start()

    @staticmethod
    def get_year_seconds():
        if LeapYear.is_leap_year(datetime.now()):
            return 60 * 60 * 24 * 366

        else:
            return 60 * 60 * 24 * 365

    def get_electricity_usage_i(self, _power, _power_passive, _last_month_max_passive_sum, _power_sum_i, _power_passive_sum_i):
        return [_power + _power_sum_i, _power_passive + _power_passive_sum_i]

    def get_electricity_usage_ii(self, _power, _power_passive, _last_month_max_passive_sum, _power_sum_ii, _power_passive_sum_ii):
        return [_power + _power_sum_ii, _power_passive + _power_passive_sum_ii]

    @staticmethod
    def print_results():
        pass

    @staticmethod
    def main():
        pass


if __name__ == "__main__":
    ElectricityUsageState.main()
