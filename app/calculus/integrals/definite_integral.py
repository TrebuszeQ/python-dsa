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
        sigma = 0

        for i in range(1, self._num_intervals + 1):
            x = self._upper_bound + h * i
            podstawa_b = self._function(x)

        return sigma

    def __str__(self):
        return f"Definite integral of {self.function.__name__} from {self._lower_bound} to {self._upper_bound} to {self._upper_bound}."
