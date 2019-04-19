def factors_map(number):
    factor=2
    factor_map = {}

    while number >= factor:
        if number % factor == 0:
            factor_map[factor] = 0
        while number % factor == 0:
            number = number/factor
            factor_map[factor] += 1
        factor += 1

    return factor_map


def smallest_multiple(factor_map):
    multiple=1
    for factor in factor_map.keys():
        for i in range(factor_map[factor]):
            multiple *= factor

    return multiple


def smallest_multiple_of(n):
    overall_factor_map = {}

    for i in range(2, n + 1):
        factor_map = factors_map(i)
        for factor in factor_map.keys():
            if factor not in overall_factor_map:
                overall_factor_map[factor] = factor_map[factor]
            else:
                overall_factor_map[factor] = max(overall_factor_map[factor],
                                                 factor_map[factor])

    return smallest_multiple(overall_factor_map)

print smallest_multiple_of(20)
