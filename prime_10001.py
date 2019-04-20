def prime_generator():
    primes = []
    prime_candidate = 2
    while True:
        for prime in primes:
            if prime_candidate % prime == 0:
                prime_candidate += 1
                break
        else:
            primes.append(prime_candidate)
            yield prime_candidate


prime_gen = prime_generator()
for i in range(10001):
    x = prime_gen.next()
else:
    print x

for i, p in enumerate(prime_generator()):
    if i == 10000:
        print p
    elif i > 10000:
        break
