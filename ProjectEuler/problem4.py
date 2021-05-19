'''
Largest palindrome product
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. 

Find the largest palindrome made from the product of two 3-digit numbers.

'''

import math
sum = 0
for a in range(100,1000):
    for b in range(100, 1000):
        prod = str(a * b)
        prod_len = int(len(prod) / 2)
        if prod_len % 2 > 0:
            prod_len = math.floor(prod_len)

        part_a, part_b = prod[0:prod_len], prod[-prod_len:]
        if part_a == part_b[::-1] and int(prod) > int(sum):
            sum = prod

print(sum)