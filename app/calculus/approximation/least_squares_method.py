from app.services.plot_maker_service import PlotMaker


class LeastSquaresMethod:
    @property
    def points_x(self):
        return self._points_x

    @property
    def points_y(self):
        return self._points_y

    @property
    def sigma_xy(self):
        return self._sigma_xy

    @property
    def sigma_x(self):
        return self._sigma_x

    @property
    def sigma_y(self):
        return self._sigma_y

    @property
    def sigma_x2(self):
        return self._sigma_x2

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    def __init__(self, points_x, points_y):
        self._points_x = points_x
        self._points_y = points_y
        self.n = len(self.points_x)
        self._sigma_xy = self.find_sigma_xy()
        self._sigma_x = self.find_sigma_x()
        self._sigma_x2 = self.find_sigma_x2()
        self._sigma_y = self.find_sigma_y()
        self.sigma_y2 = self.find_sigma_y2()
        self._a = self.find_a()
        self._b = self.find_b()
        self._points_y_approx = self.find_points_y_approx()

    def find_a(self, debug=False):
        n = self.n
        denom = (n * self._sigma_xy - self._sigma_x * self._sigma_y)
        meter = n * self._sigma_x2 - (self._sigma_x ** 2)
        if debug:
            print("a = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_x2 - (sigma_x ** 2))")
            print(f"a = ({n} * {self._sigma_xy} - {self._sigma_x} * {self._sigma_y}) / ({n} * {self._sigma_x2} - {self._sigma_x ** 2})")
            print(f"denom: {denom}; meter: {meter}")

        a = denom / meter
        if debug:
            print(f"a: {a}\n")
        return a

    def find_b(self, debug=False):
        n = self.n

        denom = (1 / n)
        meter = (self._sigma_y - self.a * self._sigma_x)
        if debug:
            print("b = (n * sigma_x - a) / (sigma_x * sigma_y)")
            print(f"b = {(1 / n)} * ({self._sigma_y} - {self.a} * {self._sigma_x}))")
            print(f"denom: {denom}; meter: {meter}")

        b = denom * meter
        if debug:
            print(f"b: {b}\n")
        return b

    def least_squares_method(self, debug=False):
        x = self._points_x
        y = self._points_y
        n = self.n
        sigma = 0

        for i in range(n):
            num = (y[i] - self._a * x[i] - self._b) ** 2
            if debug:
                print(f"no. {i}: sigma: {sigma} += ({y[i]} - {self._a} * {x[i]} - {self._b})^2 ; {num}")
            sigma += num

            if debug:
                print(f"sigma least_squares_method: {sigma}\n")
        return sigma

    def find_sigma_xy(self, debug=False):
        x = self._points_x
        y = self._points_y
        n = self.n
        sigma = 0

        for i in range(n):
            num = y[i] * x[i]
            if debug:
                print(f"no. {i}; sigma {sigma} += {y[i]} * {x[i]} ; {num} ")
            sigma += num

        if debug:
            print(f"find_sigma_xy: {sigma}\n")
        return sigma

    def find_sigma_y(self, debug=False):
        y = self._points_y
        n = self.n
        sigma = 0

        for i in range(n):
            if debug:
                print(f"no. {i}; sigma {sigma} += {y[i]} ; {y[i]} ")
            sigma += y[i]

        if debug:
            print(f"find_sigma_y: {sigma}\n")
        return sigma

    def find_sigma_y2(self, debug=False):
        y = self._points_y
        n = self.n
        sigma = 0

        for i in range(n):
            num = y[i] ** 2
            if debug:
                print(f"no. {i}; sigma {sigma} += {y[i]} ** 2; {num}")
            sigma += num

        if debug:
            print(f"find_sigma_y2: {sigma}\n")
        return sigma

    def find_sigma_x(self, debug=False):
        x = self._points_x
        n = self.n
        sigma = 0

        for i in range(n):
            if debug:
                print(f"no. {i}; sigma {sigma} += {x[i]} ; {x[i]} ")
            sigma += x[i]

        if debug:
            print(f"find_sigma_x: {sigma}\n")
        return sigma

    def find_sigma_x2(self, debug=False):
        x = self._points_x
        n = self.n
        sigma = 0

        for i in range(n):
            num = x[i] ** 2
            if debug:
                print(f"no. {i}; sigma {sigma} += {x[i]} ** 2; {num}")
            sigma += x[i] ** 2

        if debug:
            print(f"find_sigma_x2: {sigma}\n")
        return sigma

    def find_points_y_approx(self):
        y_points2 = []
        for i in range(self.n):
            y = self._a * self.points_x[i] + self._b
            y_points2.append(y)

        self._points_y_approx = y_points2
        return y_points2

    def make_linear_approximation_plot(self, size, points_on_plot: bool):
        plot_maker = PlotMaker()
        plot_maker.x_arr = self._points_x
        plot_maker.y_arr = self._points_y_approx
        plot = plot_maker.make_single_linear_plot("Approximation Function Plot", size, points_on_plot)
        plot.show()
        plot_maker.y_arr = self._points_y
        plot = plot_maker.make_single_linear_plot("Approximation Function Plot", size, points_on_plot)
        plot.show()

    def make_linear_plot(self, size, points_on_plot: bool):
        pass



