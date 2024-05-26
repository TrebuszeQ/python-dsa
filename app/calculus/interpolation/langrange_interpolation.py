from app.calculus.polynomials.single_polynomial import SinglePolynomial


class LagrangeInterpolation:

    @property
    def polynomial(self):
        return self._poly

    def __init__(self, x_points: [float], y_points: [float]):
        self.x_points = x_points
        self.y_points = y_points
        self._poly = SinglePolynomial(x_points, y_points)
        if len(x_points) != len(y_points):
            raise ValueError("x_points and y_points must have the same length")

    def _basis_polynomial(self, i, x):
        pi = 1

        for j in range(self._poly.degree):
            try:
                if i != j:
                    pi *= (x - self.x_points[j]) / (self.x_points[i] - self.x_points[j])
                else:
                    pi *= (x - self.x_points[i]) / (self.x_points[i] - self.x_points[j])

            except ZeroDivisionError:
                return 0

            # l0 = (x - x1)(x - x2) / (x0 - x1)(x0 - x2)
            # l1 = (x - x0)(x - x2) / (x1 - x0)(x1 - x2)
            # l2 = (x - x0)(x - x1) / (x2 - x0)(x2 - x1)
            #
            # l0 = (x - x1)(x - x2)(x - x3) / (x0 - x1)(x0 - x2)(x0 - x3)
            # l1 = (x - x0)(x - x2)(x - x3) / (x1 - x0)(x1 - x2)(x1 - x3)
            # l2 = (x - x0)(x - x1)(x - x3) / (x2 - x0)(x2 - x1)(x2 - x3)

        return pi

    def interpolate(self, x):
        sigma = 1

        i = 0
        for y_point in self.y_points:
            sigma += y_point * self._basis_polynomial(i, x)
            i += 1

        return sigma

    def __str__(self):
        return f"Lagrange interpolation polynomial for points {list(zip(self.x_points, self.y_points))})"

