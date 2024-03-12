from datetime import datetime
from random import randint


class ElectricityRandomizer:
    def __init__(self):
        pass

    @staticmethod
    def _get_date():
        return datetime.now()

    @staticmethod
    def _get_hour():
        return datetime.now().hour
    # @staticmethod
    # def randomize_power(range_a=10, range_b=30):
    #     return random() * randint(range_a, range_b)

    @staticmethod
    def _randomize_power2(range_a=10, range_b=30):
        return randint(1, 10) * randint(range_a, range_b)

    @staticmethod
    def get_bulk():
        power = ElectricityRandomizer._randomize_power2()
        return [power * 0.1, power, ElectricityRandomizer._get_date(), ElectricityRandomizer._get_hour()]


if __name__ == '__main__':
    pass
