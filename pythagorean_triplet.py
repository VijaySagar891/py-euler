def is_pythagorean_triplet(x, y, z):
    return x * x + y * y == z * z


def is_py_triplet_has_total(x, y, total):
    return is_pythagorean_triplet(x, y, total - x - y)


for x in range(1, 999):
    for y in range(x +1, 1000):
        if is_py_triplet_has_total(x, y, 1000):
            print x*y*(1000-x-y)

