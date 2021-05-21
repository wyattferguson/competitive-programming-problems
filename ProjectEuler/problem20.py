'''
Name: Factorial digit sum
Problem URL: https://projecteuler.net/problem=20
Date Completed: May 21, 2021 

Description:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 362880,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


n = 100
# calculate the factorial
fact = 1
for x in range(1, n):
    fact *= x

# sum up the digits
sum = 0
for i in str(fact):
    sum += int(i)

print(sum)
