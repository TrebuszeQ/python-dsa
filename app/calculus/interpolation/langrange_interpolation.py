from app.calculus.polynomials.single_polynomial import SinglePolynomial


class LagrangeInterpolation:

    @property
    def polynomial(self):
        return self._poly

    def __init__(self, x_points: [float], y_points: [float], constant_term: float):
        poly_arr = [[y, x] for y, x in zip(y_points, x_points)]
        poly_arr.append([constant_term, 0])
        self.x_points = x_points
        self.y_points = y_points
        self._poly = SinglePolynomial(x_points, y_points, constant_term)
        if len(x_points) != len(y_points):
            raise ValueError("x_points and y_points must have the same length")

    def l(self, x, i):
        result = 1

        n = self._poly.degree - 1
        for j in range(n):
            xj = self.x_points[j]
            xi = self.x_points[i]
            if i != j:
                result *= (x - xj) / (xi - xj)

        return result

    def _basis_polynomial(self, i, x):
        result = 1

        for j in range(len(self.x_points)):
            if i != j:
                result *= (x - self.x_points[j]) / (self.x_points[i] - self.x_points[j])

        return result

    def interpolate(self, x):
        interpolated_value2 = 1
        interpolated_value = 1
        degree = self._poly.degree

        for i in range(1, degree):
            interpolated_value *= self.y_points[i] * self._basis_polynomial(i, x)
            interpolated_value2 *= self.y_points[i] * self.l(x, i)

        interpolated_value2 *= self._poly.horner_method(x)
        return interpolated_value

    def __str__(self):
        return f"Lagrange interpolation polynomial for points {list(zip(self.x_points, self.y_points))})"

