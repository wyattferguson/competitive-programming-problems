'''
Name: Captain Hammer   
URL: https://bit.ly/3fGedyW
Date: May 23, 2021

Test Cases:
3
98 980
98 490
299 1234

Case #1: 45.0000000
Case #2: 15.0000000
Case #3: 3.8870928

Equation:
θ = asin(dg/v^2) / 2

'''

from math import asin, degrees


def solve(v, d):
    g = 9.8
    part1 = (g * d) / (v*v)
    return degrees(asin(part1) / 2)


if __name__ == "__main__":
    n_cases = int(input().strip())
    for case in range(1, n_cases+1):
        v, d = input().strip().split()

        result = solve(int(v), int(d))
        print(f"Case #{case}: {result:.7f}")
