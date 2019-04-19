def palindrome_product_brute_force(min=100, max=999):
    max_palindrome = 0;
    for x in range(min, max + 1):
        for y in range(min, max + 1):
            prod = x * y
            prod_str = str(prod)
            reverse = prod_str[::-1]
            if reverse == prod_str and max_palindrome < prod:
                max_palindrome = prod
    return max_palindrome

def palindrome_product_traverse_palindromes(min=10000, 
                                            max=999*999,
                                            min_factor=100, 
                                            max_factor=999):
    for x in range(max, min, -1):
        if str(x) == str(x)[::-1]:
            for fact in range(min_factor, max_factor):
                if x % fact == 0:
                    quot = x / fact
                    if quot < max_factor and quot > min_factor:
                        return x
    return 0


def palindrome_product_generate_palindromes(min=100, max=999):
    for x in range(max, min, -1):
        palindrome=int(str(x)+str(x)[::-1])
        for fact in range(max, min, -1):
            if palindrome % fact == 0:
                quot = palindrome / fact
                if quot <= max and quot >= min:
                    return palindrome 
    return 0

print palindrome_product_generate_palindromes()


print palindrome_product_brute_force(100, 999)

print palindrome_product_traverse_palindromes()
