import math

import app.calculus.approximation.least_squares_method as lm


def linear_regression(n, points_x, points_y):
    x = points_x
    y = points_y
    r = 0
    sigma_xy = lm.find_sigma_xy(n, x, y)
    sigma_x = lm.find_sigma_x(n, x)
    sigma_x2 = lm.find_sigma_x2(n, x)
    sigma_y = lm.find_sigma_y(n, y)
    sigma_y2 = lm.find_sigma_y2(n, y)

    for i in range(n):
        r += (n * sigma_xy - sigma_x * sigma_y) / math.sqrt((n * sigma_x2 - sigma_x ** 2) * (n * sigma_y2 - sigma_y ** 2))

    return r
