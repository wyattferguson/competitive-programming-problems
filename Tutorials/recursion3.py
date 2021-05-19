"""
Write a function that takes N objects that you can break partion up into M parts (M>=0)

N = 4,  M = 3
N N N N | M M M

N + N + N + N
NN + N + N
NN + NN
NNN + N
N + NN + N
"""


def path(p, q):
    if p == 0:
        return 1
    if q == 0 or p < 0:
        return 0

    return path(p - q, q) + path(p, q - 1)


n = 9
m = 5
cnt = path(n, m)
print(cnt)
