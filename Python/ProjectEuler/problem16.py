"""
Name: Power digit sum
Problem URL: https://projecteuler.net/problem=16
Date Completed: May 15 2021 

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

n = 2 ** 1000
k = 0
for i in range(len(str(n))):
    k += int(str(n)[i])
print(k)
