#!/usr/bin/env python2

from collections import defaultdict

ID_LEN = 5

def gen_primes():
    """Using the Sieve of Erastothenes solution"""
    composites = defaultdict(list)
    checker = 2

    while True:
        if checker not in composites:
            yield checker
            composites[checker*checker].append(checker)
        else:
            for prime in composites[checker]:
                composites[prime+checker].append(prime)
            del composites[checker]

        checker += 1

def solution(i):
    pointer = 0
    id_ = ''
    primes = gen_primes()

    while True:
        prime_str = str(next(primes))
        threshold = pointer + len(prime_str) - i
        if threshold > 0:
            prime_str = prime_str[i-pointer:]
            while len(id_) < ID_LEN:
                for num in prime_str[:ID_LEN-len(id_)]:
                    id_ += num
                prime_str = str(next(primes))
            return id_

        pointer += len(prime_str)