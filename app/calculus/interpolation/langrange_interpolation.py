from app.calculus.polynomials.single_polynomial import SinglePolynomial


class LagrangeInterpolation:

    @property
    def polynomial(self):
        return self._poly

    @property
    def interpolated_x_points(self):
        return self._pi_points

    @property
    def interpolated_y_points(self):
        return self._sigma_points

    def __init__(self, x_points: [float], y_points: [float]):
        self.x_points = x_points
        self.y_points = y_points
        self._pi_points = []
        self._sigma_points = []
        self._poly = SinglePolynomial(x_points, y_points)
        if len(x_points) != len(y_points):
            raise ValueError("x_points and y_points must have the same length")

    def _basis_polynomial(self, i, x):
        pi = 1

        for j in range(self._poly.degree):
            try:
                if i != j:
                    print(f"{pi} *= ({x} - {self.x_points[j]}) / ({self.y_points[i]} - {self.x_points[j]})")
                    pi *= (x - self.x_points[j]) / (self.x_points[i] - self.x_points[j])

            except ZeroDivisionError:
                print("0")
                return 0

        self._pi_points.append(pi)
        return pi

    def interpolate(self, x):
        sigma = 0

        i = 0
        for y_point in self.y_points:
            poly_value = self._basis_polynomial(i, x)
            print(f"{sigma} += {y_point} * {poly_value})")
            sigma += y_point * poly_value
            self._sigma_points.append(sigma)
            i += 1

        return sigma

    def __str__(self):
        return f"Lagrange interpolation polynomial for points {list(zip(self.x_points, self.y_points))})"
