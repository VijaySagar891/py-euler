from sets import Set

def find_power_sums(max_base, max_pow):
    power_digit_sums = []
    for i in range(2, max_base + 1):
        power = 1
        for j in range(1, max_pow + 1):
            power *= i
            if digit_sum(power) == i and power > 10:
                power_digit_sums.append(power)

    return sorted(power_digit_sums)


def digit_sum(num):
    sum = 0
    while (num > 0):
        sum += num % 10
        num = num / 10
    return sum


print find_power_sums(100, 50)[29]
        
