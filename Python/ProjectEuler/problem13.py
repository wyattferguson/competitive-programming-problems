'''
Name: Large sum
Problem URL: https://projecteuler.net/problem=13
Date Completed: May 2021 
Description: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''

total = 0
with open("problem13.in", "r") as f:
    for num in f:
        total += int(num.strip())

print(str(total)[0:10])
