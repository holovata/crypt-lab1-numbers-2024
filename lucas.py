import random
import math
from rabin_miller import mod_pow


def prime_factors(n):
    factors = []
    # Check for number of 2s that divide n
    if n % 2 == 0:
        factors.append(2)
    while n % 2 == 0:
        n //= 2
    # n must be odd at this point, thus a skip of 2 (i.e., i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # While i divides n, append i and divide n
        if n % i == 0:
            factors.append(i)
        while n % i == 0:
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def lucas_test(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # фактори n-1
    factors = prime_factors(n - 1)
    trial_count = 10  # к-ть спроб тесту

    for _ in range(trial_count):
        a = random.randint(2, n - 2)
        if mod_pow(a, n - 1, n) != 1:
            return False  # n не просте число
        flag = True
        for factor in factors:
            if mod_pow(a, (n - 1) // factor, n) == 1:
                flag = False
                break
        if flag:
            return True  # n імовірно просте число
    return False  # n не просте, якщо не пройшло жоден тест