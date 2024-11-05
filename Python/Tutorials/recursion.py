"""
Sum all the numbers from 0 to N
"""


def calc(x):
    if x == 0:
        return 0
    return x + calc(x - 1)


n = 5
s = calc(n)
print(s)
