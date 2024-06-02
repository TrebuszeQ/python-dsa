def find_a(n, sigma_xy, sigma_x, sigma_y, sigma_x2):
    a = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_x2 - (sigma_x ** 2))
    return a


def find_b(n, a, sigma_y, sigma_x):
    b = (1 / n) * (sigma_y - a * sigma_x)
    return b


def least_squares_method(n, points_x, points_y, a=None, b=None):
    x = points_x
    y = points_y
    sigma = 0

    if a and b is None:
        sigma_xy = find_sigma_xy(n, x, y)
        sigma_x = find_sigma_x(n, x)
        sigma_y = find_sigma_y(n, y)
        sigma_x2 = find_sigma_x2(n, x)
        a = find_a(n, sigma_xy, sigma_x, sigma_y, sigma_x2)
        b = find_b(n, a, sigma_y, sigma_x)
    elif a is None:
        sigma_xy = find_sigma_xy(n, x, y)
        sigma_x = find_sigma_x(n, x)
        sigma_y = find_sigma_y(n, y)
        sigma_x2 = find_sigma_x2(n, x)
        a = find_a(n, sigma_xy, sigma_x, sigma_y, sigma_x2)
    elif b is None:
        sigma_x = find_sigma_x(n, x)
        sigma_y = find_sigma_y(n, y)
        b = find_b(n, a, sigma_y, sigma_x)

    for i in range(n):
        sigma += (y[i] - a * x[i] - b) ** 2

    return sigma


def find_sigma_xy(n, points_x, points_y):
    x = points_x
    y = points_y
    sigma = 0

    for i in range(n):
        sigma += (y[i] * x[i])

    return sigma


def find_sigma_y(n, points_y):
    y = points_y
    sigma = 0

    for i in range(n):
        sigma += y[i]

    return sigma


def find_sigma_x(n, points_x):
    x = points_x
    sigma = 0

    for i in range(n):
        sigma += x[i]

    return sigma


def find_sigma_x2(n, points_x):
    x = points_x
    sigma = 0

    for i in range(n):
        sigma += x[i] ** 2

    return sigma


def find_sigma_y2(n, points_y):
    y = points_y
    sigma = 0

    for i in range(n):
        sigma += y[i] ** 2

    return sigma
