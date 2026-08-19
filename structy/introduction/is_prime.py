from math import floor, sqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for num in range(2, n):
        if n % num == 0:
            return False
    return True

def is_prime_2(n: int) -> bool:
    if n < 2:
        return False
    for num in range(2, floor(sqrt(n)) + 1):
        if n % num == 0:
            return False
    return True

def driver():
    res = is_prime_2(2048)
    print(res)