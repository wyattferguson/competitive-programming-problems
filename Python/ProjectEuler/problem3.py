'''
Name: Largest prime factor
Problem URL: https://projecteuler.net/problem=3
Date Completed: 2019 

Description:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from __future__ import division

i = 3
n = 600851475143

while i*i < n/2:
    while n % i == 0:
        n = n / i
    i += 2
print(n)
