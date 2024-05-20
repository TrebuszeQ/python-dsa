from app.calculus.polynomials.single_polynomial import SinglePolynomial


class LagrangeInterpolation:

    @property
    def polynomial(self):
        return self._poly

    def __init__(self, x_points: [float], y_points: [float], constant_term: float):
        poly_arr = [[x, y] for x, y in zip(x_points, y_points)]
        poly_arr.append([0, constant_term])


        if len(x_points) != len(y_points):
            raise ValueError("x_points and y_points must have the same length")

        self.x_points = x_points
        self.y_points = y_points

    def basis_polynomial(self, i, x):
        result = 1
        for j in range(len(self.x_points)):
            if i != j:
                result *= (x - self.x_points[j]) / (self.x_points[i] - self.x_points[j])

        return result

    def interpolate(self, x):
        interpolated_value = 0
        for i in range(len(self.y_points)):
            interpolated_value += self.y_points[i] * self.basis_polynomial(i, x)

            interpolated_value *= self.x_points[i] * self.basis_polynomial(i, x)

        return interpolated_value

    def __str__(self):
        return f"Lagrange interpolation polynomial for points {list(zip(self.x_points, self.y_points))})"

