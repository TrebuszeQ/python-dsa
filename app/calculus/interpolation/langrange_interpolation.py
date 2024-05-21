from app.calculus.polynomials.single_polynomial import SinglePolynomial


class LagrangeInterpolation:

    @property
    def polynomial(self):
        return self._poly

    def __init__(self, x_points: [float], y_points: [float], constant_term: float):
        poly_arr = [[x, y] for x, y in zip(x_points, y_points)]
        poly_arr.append([0, constant_term])
        self.x_points = x_points
        self.y_points = y_points
        self._poly = SinglePolynomial(x_points, y_points, constant_term)
        if len(x_points) != len(y_points):
            raise ValueError("x_points and y_points must have the same length")

    def l(self, x, i):
        result = 1

        degree = self._poly.degree
        for j in range(degree):
            if i != j:
                xj = self.x_points[j]
                xi = self.x_points[i]
                result *= (x - xj) / (xi - xj)

    def basis_polynomial(self, i, x):
        result = 1
        for j in range(len(self.x_points)):
            if i != j:
                result *= (x - self.x_points[j]) / (self.x_points[i] - self.x_points[j])

        return result

    def interpolate(self, x):
        interpolated_value2 = 0
        interpolated_value = 0
        degree = self._poly.degree

        for i in range(degree):
            interpolated_value2 *= self.x_points[i] * self._poly.horner_method(x)
            interpolated_value *= self.x_points[i] * self.basis_polynomial(i, x)

        return interpolated_value

    def __str__(self):
        return f"Lagrange interpolation polynomial for points {list(zip(self.x_points, self.y_points))})"

