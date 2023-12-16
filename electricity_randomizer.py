from datetime import datetime
from random import random, randint


class ElectricityRandomizer:

    @staticmethod
    def get_date():
        return datetime.now()

    @staticmethod
    def get_hour():
        return datetime.now().hour
    # @staticmethod
    # def randomize_power(range_a=10, range_b=30):
    #     return random() * randint(range_a, range_b)

    @staticmethod
    def randomize_power2(range_a=10, range_b=30):
        return randint(1, 10) * randint(range_a, range_b)

    @staticmethod
    def get_bulk():
        power = ElectricityRandomizer.randomize_power2()
        return [power * 0.1, power, ElectricityRandomizer.get_date(), ElectricityRandomizer.get_hour()]


if __name__ == '__main__':
    print(ElectricityRandomizer.randomize_power2())
