def find_a(n, sigma_xy, sigma_x, sigma_y, sigma_x2, debug=False):
    denom = (n * sigma_xy - sigma_x * sigma_y)
    meter = n * sigma_x2 - (sigma_x ** 2)
    if debug:
        print("a = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_x2 - (sigma_x ** 2))")
        print(f"a = ({n} * {sigma_xy} - {sigma_x} * {sigma_y}) / ({n} * {sigma_x2} - {sigma_x ** 2})")
        print(f"denom: {denom}; meter: {meter}")

    a = denom / meter
    if debug:
        print(f"a: {a}\n")
    return a


def find_b(n, a, sigma_y, sigma_x, debug=False):
    denom = (1 / n)
    meter = (sigma_y - a * sigma_x)
    if debug:
        print("b = (n * sigma_x - a) / (sigma_x * sigma_y)")
        print(f"b = {(1 / n)} * ({sigma_y} - {a} * {sigma_x}))")
        print(f"denom: {denom}; meter: {meter}")

    b = denom * meter
    if debug:
        print(f"b: {b}\n")
    return b

def least_squares_method(n, points_x, points_y, a=None, b=None, debug=False):
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
        num = (y[i] - a * x[i] - b) ** 2
        if debug:
            print(f"no. {i}: sigma: {sigma} += ({y[i]} - {a} * {x[i]} - {b})^2 ; {num}")
        sigma += num

        if debug:
            print(f"sigma least_squares_method: {sigma}\n")
    return sigma


def find_sigma_xy(n, points_x, points_y, debug=False):
    x = points_x
    y = points_y
    sigma = 0

    for i in range(n):
        num = y[i] * x[i]
        if debug:
            print(f"no. {i}; sigma {sigma} += {y[i]} * {x[i]} ; {num} ")
        sigma += num

    if debug:
        print(f"find_sigma_xy: {sigma}\n")
    return sigma


def find_sigma_y(n, points_y, debug=False):
    y = points_y
    sigma = 0

    for i in range(n):
        if debug:
            print(f"no. {i}; sigma {sigma} += {y[i]} ; {y[i]} ")
        sigma += y[i]

    if debug:
        print(f"find_sigma_y: {sigma}\n")
    return sigma


def find_sigma_y2(n, points_y, debug=False):
    y = points_y
    sigma = 0

    for i in range(n):
        num = y[i] ** 2
        if debug:
            print(f"no. {i}; sigma {sigma} += {y[i]} ** 2; {num}")
        sigma += num

    if debug:
        print(f"find_sigma_y2: {sigma}\n")
    return sigma


def find_sigma_x(n, points_x, debug=False):
    x = points_x
    sigma = 0

    for i in range(n):
        if debug:
            print(f"no. {i}; sigma {sigma} += {x[i]} ; {x[i]} ")
        sigma += x[i]

    if debug:
        print(f"find_sigma_x: {sigma}\n")
    return sigma


def find_sigma_x2(n, points_x, debug=False):
    x = points_x
    sigma = 0

    for i in range(n):
        num = x[i] ** 2
        if debug:
            print(f"no. {i}; sigma {sigma} += {x[i]} ** 2; {num}")
        sigma += x[i] ** 2

    if debug:
        print(f"find_sigma_x2: {sigma}\n")
    return sigma
