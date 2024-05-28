from app.services.plot_maker_service import PlotMaker


class DefiniteIntegral:
    @property
    def computed_area(self):
        return self._computed_area

    def __init__(self, function, lower_bound, upper_bound, plot_maker_service: PlotMaker, num_intervals=1000):

        self._function = function
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        self._plot_maker = plot_maker_service
        self._num_intervals = num_intervals
        self._arr_x = []
        self._arr_y = []
        self._set_computed_area()
        self.plot = None
        self.set_plot()

    def _set_computed_area(self):
        a = self._lower_bound
        b = self._upper_bound
        n = self._num_intervals
        f = self._function

        h = (b - a) / n
        sigma = 0

        for i in range(1, n + 1):
            self._arr_x.append(i)
            p = (f(a + (i - 1) * h) + f(a + i * h)) / 2.0 * h
            sigma += p
            self._arr_y.append(sigma)

        self._computed_area = sigma

    def set_plot(self):
        self._plot_maker.x_arr = self._arr_x
        self._plot_maker.y_arr = self._arr_y
        self.plot = self._plot_maker.make_single_line_plot("Definite Integral Plot", 30)

    def __str__(self):
        return f"Definite integral of {self.function.__name__} from {self._lower_bound} to {self._upper_bound} to {self._upper_bound}."
