from rabin_miller import isPrimeRM
from lucas import lucas_test


def jacobi_symbol(n, k):
    assert k > 0 and k % 2 == 1
    n %= k
    t = 1
    while n != 0:
        while n % 2 == 0:
            n //= 2
            r = k % 8
            if r == 3 or r == 5:
                t = -t
        n, k = k, n  # Swap n and k
        if n % 4 == 3 and k % 4 == 3:
            t = -t
        n %= k
    return t if k == 1 else 0


def select_D(candidate):
    D = 5
    while jacobi_symbol(D, candidate) != -1:
        if D > 0:
            D += 2
        else:
            D = -2
        D *= -1
    return D


def baillie_test(num):
    known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for known_prime in known_primes:
        if num == known_prime:
            return True
        elif num % known_prime == 0:
            return False
    if not isPrimeRM(num, 2):
        return False
    if not lucas_test(num):
        return False
    return True