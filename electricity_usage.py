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
        start_date = freeze_time(datetime.now())
        start_date_ts = datetime.timestamp(start_date)
        passed_secs = 0

        month_secs = 60 * 60 * 24
        year_secs = ElectricityUsage.get_year_seconds()

        ElectricityUsage.get_electricity_usage()


if __name__ == "__main__":
    ElectricityUsage.main()
