import pytest
from rabin_miller import isPrimeRM
from baillie_psw import baillie_test

# Тестові дані
PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 83813]
COMPOSITE_NUMBERS = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 10000000]
CARMICHAEL_NUMBERS = [561, 1105, 1729, 2465, 2821, 6601]


@pytest.mark.parametrize("number", PRIME_NUMBERS)
def test_miller_rabin_primes(number):
    assert isPrimeRM(number, 5) == True, f"Failed on prime {number}"


@pytest.mark.parametrize("number", COMPOSITE_NUMBERS + CARMICHAEL_NUMBERS)
def test_miller_rabin_composites(number):
    assert isPrimeRM(number, 5) == False, f"Failed on composite {number}"


@pytest.mark.parametrize("number", PRIME_NUMBERS)
def test_baillie_psw_primes(number):
    assert baillie_test(number) == True, f"Failed on prime {number}"


@pytest.mark.parametrize("number", COMPOSITE_NUMBERS + CARMICHAEL_NUMBERS)
def test_baillie_psw_composites(number):
    assert baillie_test(number) == False, f"Failed on composite {number}"


if __name__ == "__main__":
    pytest.main()