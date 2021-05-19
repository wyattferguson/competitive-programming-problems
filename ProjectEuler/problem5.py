'''
Name: Smallest multiple
Problem URL: https://projecteuler.net/problem=5
Date Completed: 2019 

Description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

found = 0
i = 2520
max = 20

while(found == 0):
    # skip numbers below 10, since they divide evenly into values above 10
    for k in range(11, max+1):
        if i % k == 0:
            if k == max:
                found = i
        else:
            break
    i += max  # solution must be a multiple of 20
print(found)
