def largest_prime_factor(n):
    largest_factor = 1
    factor = 2
    number = n
    while factor <= number:
        if number % factor == 0:
            largest_factor = factor

        while number % factor == 0:
            number = number / factor
        factor = factor + 1
    return largest_factor

print largest_prime_factor(13195)
print largest_prime_factor(600851475143)
