"""
Name: Multiples of 3 and 5
Problem URL: https://projecteuler.net/problem=1
Date Completed: 2019 

Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

max = 1000
sum = 0
for n in range(max):
    if n % 3 == 0 or n % 5 == 0:
        sum += n

print(sum)
