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
        result = 1

        for j in range(self._poly.degree):
            try:
                if i == j:
                    result *= (x - self.x_points[i]) / (self.x_points[i] - self.x_points[j])
                else:
                    result *= (x - self.x_points[j]) / (self.x_points[i] - self.x_points[j])
            except ZeroDivisionError:
                return 0

        return result

    def interpolate(self, x):
        interpolated_value = 1

        i = 0
        for y_point in self.y_points:
            interpolated_value += y_point * self._basis_polynomial(i, x)
            i += 1

        return interpolated_value

    def __str__(self):
        return f"Lagrange interpolation polynomial for points {list(zip(self.x_points, self.y_points))})"

