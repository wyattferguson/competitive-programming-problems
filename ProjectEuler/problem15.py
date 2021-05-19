"""

Name: Lattice paths
Problem URL: https://projecteuler.net/problem=15
Date Completed: May 2021 

Description:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

(x + y)! / x!y! = PATHS

2x2 Grid : 6 Paths
4! / 2! * 2!
24 / 4 = 6

How many such routes are there through a 20×20 grid?
"""

from math import factorial

n = 20

paths = factorial(n + n) / (factorial(n) * factorial(n))
print(int(paths))
