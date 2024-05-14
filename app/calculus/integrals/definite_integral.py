from app.geometry.trapezium import Trapezium
from app.services.plot_maker_service import PlotMakerService


class DefiniteIntegral:
    @property
    def area(self):
        return self._area

    def __init__(self, function, lower_bound, upper_bound, plot_maker_service: PlotMakerService, num_intervals=1000):
        self._function = function
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        self._plot_maker_service = plot_maker_service
        self._num_intervals = num_intervals
        self._area = None

    def compute_integral(self):
        h = (self._upper_bound - self._lower_bound) / self._num_intervals
        integral_sum = 0
        # a = self._function(self._upper_bound)
        #
        # for i in range(1, self._num_intervals):
        #     b = self._function(self._lower_bound + h * i)
        #     trap = Trapezium(a, b, h, self._plot_maker_service)
        #     trap_area = trap.area
        #
        #     x_i = self._lower_bound + i * h
        #     integral_sum += self.function(x_i) * h

        return integral_sum

    def __str__(self):
        return f"Definite integral of {self.function.__name__} from {self._lower_bound} to {self._upper_bound} to {self._upper_bound}."
