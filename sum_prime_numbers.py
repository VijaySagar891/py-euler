def prime_generator(max):
    prime_candidate=2
    prime_list=[]
    while prime_candidate<max:
        for prime in prime_list:
            if prime_candidate % prime==0:
                break
        else:
            prime_list.append(prime_candidate)
            yield prime_candidate
        prime_candidate += 1


# pg = prime_generator(2000000)
# pg = prime_generator(10)
# print sum(pg)


def sum_primes(max):
    prime_candidate=2
    prime_list=[]
    while prime_candidate<max:
        for prime in prime_list:
            if prime_candidate%prime==0:
                break
            elif prime*prime > prime_candidate:
                prime_list.append(prime_candidate)
                break
        else:
            prime_list.append(prime_candidate)
        prime_candidate += 1
    return sum(prime_list)

print sum_primes(2000000)
