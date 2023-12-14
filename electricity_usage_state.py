import threading
from math import sin
from datetime import datetime
from time import time
from freezegun import freeze_time
from threading import Timer
from leap_year import LeapYear
# my
from cli import Cli


class ElectricityUsage:
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

    def set_interval(self):
        

    @staticmethod
    def get_year_seconds():
        if LeapYear.is_leap_year(datetime.now()):
            return 60 * 60 * 24 * 366

        else:
            return 60 * 60 * 24 * 365

    @staticmethod
    def get_electricity_usage(power=3):
        power_passive = power * 0.1
        power_unit = "kW"
        start = datetime.now()
        freezer = freeze_time(datetime.now())
        start_ts = datetime.timestamp(freezer)
        time = datetime.now().time()
        time_passed = datetime.now() - start



        print(start)
        print(freezer)
        power_passive_sum_i = 0
        power_passive_sum_ii = 0
        power_sum_i = 0
        power_sum_ii = 0
        last_month_max_passive_sum = 0

        # if (time < 16:00)
        #
        # sin(time)
    @staticmethod
    def get_start(started):
        if started:
            return

    @staticmethod
    def set_interval(func):
        pass

    @staticmethod
    def print_results():
        pass

    @staticmethod
    def main():
        pass


if __name__ == "__main__":
    ElectricityUsage.main()
