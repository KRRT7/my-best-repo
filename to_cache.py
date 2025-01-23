from functools import lru_cache


@lru_cache(maxsize=32)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


@lru_cache(maxsize=32)
def nth_prime(n):
    prime_count = 0
    num = 1
    while prime_count < n:
        num += 1
        if is_prime(num):
            prime_count += 1
    return num
