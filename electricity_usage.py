from math import sin
from datetime import datetime
from freezegun import freeze_time
# my
from cli import Cli


class ElectricityUsage:

    @staticmethod
    def get_electricity_usage(power=3):
        power_passive = power * 0.1
        power_unit = "kW"
        start = datetime.now()
        time = datetime.now().time()
        time_passed = datetime.now() - start

        freezer = freeze_time(datetime.now())
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
    def print_results():
        pass

    @staticmethod
    def main():
        ElectricityUsage.get_electricity_usage()
