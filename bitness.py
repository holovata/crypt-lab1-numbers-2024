import random
from baillie_psw import baillie_test
from rabin_miller import isPrimeRM


def generate_prime(bits):
    """Передбачити пошук простих чисел з заданою “бітністю”. (степені двійки)"""
    assert bits > 1  # Число повинно бути хоча б двобітним
    while True:
        # Генеруємо випадкове число на 'bits' біт
        candidate = random.getrandbits(bits)
        # Встановлюємо найстаршій та наймолодший біт у 1 для забезпечення бітності та непарності
        candidate |= (1 << (bits - 1)) | 1
        if isPrimeRM(candidate, 50):
            return candidate