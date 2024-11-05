'''
Name: Captain Hammer
URL: https://bit.ly/3fGedyW
Date: May 23, 2021

Test Cases:
3
98 980
98 490.00
299.00 1234.00

Case #1: 45.0000000
Case #2: 15.0000000
Case #3: 3.8870928

Equation:
θ = asin(dg/v^2) / 2

'''
from decimal import Decimal
from math import asin, degrees


def solve(v, d):
    x = (Decimal(9.8) * d) / (v**2)
    return degrees(asin(x) / 2)


if __name__ == "__main__":
    T = int(input().strip())
    for case in range(1, T+1):
        v, d = map(Decimal, input().split())
        result = solve(v, d)
        print(f"Case #{case}: {result:.7f}")
