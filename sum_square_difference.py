def sum_squares(n):
    return reduce(lambda x, y: x + y, map(lambda x: x*x, range(1, n + 1)), 0)


def square_ofSum(n):
    return pow(sum(range(1, n + 1)), 2)


print sum_squares(100) - square_ofSum(100)


