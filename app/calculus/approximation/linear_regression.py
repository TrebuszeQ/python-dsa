import math

from app.calculus.approximation.least_squares_method import LeastSquaresMethod


def linear_regression(n, points_x, points_y):
    x = points_x
    y = points_y
    r = 0
    lsm = LeastSquaresMethod(x, y)
    sigma_xy = lsm.sigma_xy
    sigma_x = lsm.sigma_x
    sigma_x2 = lsm.sigma_x2
    sigma_y = lsm.sigma_y
    sigma_y2 = lsm.sigma_y2

    for i in range(n):
        r += (n * sigma_xy - sigma_x * sigma_y) / math.sqrt((n * sigma_x2 - sigma_x ** 2) * (n * sigma_y2 - sigma_y ** 2))

    return r
