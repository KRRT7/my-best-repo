from functools import lru_cache


@lru_cache(maxsize=128)
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True  # Since 2 is the only even prime number
    if num % 2 == 0:
        return False  # Exclude even numbers greater than 2
    limit = int(num ** 0.5) + 1
    for i in range(3, limit, 2):  # Start from 3 and check only odd numbers
        if num % i == 0:
            return False
    return True
