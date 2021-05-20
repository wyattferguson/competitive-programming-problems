"""
Name: Power digit sum
Problem URL: https://projecteuler.net/problem=16
Date Completed: May 15 2021 

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

This is a recursive solution to problem 16, mostly just to practice doing recursion, not because its the best solution.

"""


def calc(k):
    if len(k) == 0:
        return 0
    return int(k[-1]) + calc(k[:-1])


if __name__ == "__main__":
    n = 2 ** 1000
    cnt = calc(str(n))
    print(cnt)
