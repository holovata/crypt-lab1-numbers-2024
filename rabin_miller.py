import random


def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result


def millerTest(d, n):
    """Ця функція викликається для всіх k випробувань.
    Повертає False, якщо n складене,
    Повертає True, якщо n ймовірно просте.
    d — непарне число таке, що d*2^r = n-1 для деякого r >= 1"""
    # Вибір випадкового числа в діапазоні [2; n-2]
    # Спеціальні випадки забезпечують, що n > 4
    a = 2 + random.randint(0, n - 4)

    x = mod_pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    # Продовжуємо підносити x в квадрат, поки не станеться одне з наступного:
    # 1) d не досягне n-1
    # 2) (x^2) % n не стане 1
    # 3) (x^2) % n не стане n-1
    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def isPrimeRM(n, k):
    # k — вхідний параметр, що визначає рівень точності
    # Спеціальні випадки
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Знаходимо r таке, що n = 2^d * r + 1 для деякого r >= 1
    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Повторюємо задану кількість разів 'k'
    for i in range(k):
        if not millerTest(d, n):
            return False
    return True
