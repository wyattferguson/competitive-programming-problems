"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt
import time

start = time.time()


def is_prime(x):
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = 2000000
    cnt = 2
    for x in range(3, n, 2):
        if is_prime(x):
            cnt += x

    print(cnt)
    print(f"time taken: {time.time() - start}")
