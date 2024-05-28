from app.services.plot_maker_service import PlotMaker


class Trapezium:
    @property
    def area(self):
        return self._area

    def __init__(self, a, b, h, plot_maker_service: PlotMaker):
        self._a = a
        self._b = b
        self._h = h
        self._area = 1/2 * (a + b) * h
        self._plot_maker_service = plot_maker_service

    def make_plot(self):
        plot = self._plot_maker_service.make_single_line_plot("Trapezium Plot", marker="o", size="30")
        plot.show()
