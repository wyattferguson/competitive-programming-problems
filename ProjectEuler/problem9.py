'''
Special Pythagorean triplet
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

from math import sqrt

def main():
    prod = 1000
    for a in range(1,prod):
        for b in range(1,a):
            c = sqrt(a**2 + b**2)
            # skip non-natural numbers
            if c.is_integer():
                if a + b + c == prod:
                    print(a,b,c)
                    print(int(a*b*c))
                    exit()
                       

if __name__ == "__main__":
    main()