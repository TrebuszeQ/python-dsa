def horner_method(polynomial, n, x):
    p = 0

    for i in range(n):
        term = polynomial[i][0]
        p = p * x + term

    return p * x