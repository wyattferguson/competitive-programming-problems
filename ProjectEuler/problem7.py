'''
Name: 10001st prime
Problem URL: https://projecteuler.net/problem=7
Date Completed: 2019 

Description:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from math import sqrt


def main():
    prime_goal = 10001

    # skip only even prime, 2
    prime_cnt = 2
    current = 3

    while prime_cnt < prime_goal:
        current += 2
        if is_prime(current):
            prime_cnt += 1
            # print(prime_cnt,current)


def is_prime(current):
    # max possible factor
    roof = int(sqrt(current)) + 1

    # check odd factors up to max
    for k in range(3, roof, 2):
        if current % k == 0:
            return False
    return True


if __name__ == "__main__":
    main()
