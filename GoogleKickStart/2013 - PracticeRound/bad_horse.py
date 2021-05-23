'''
Name: Bad Horse
URL: https://bit.ly/3wvRBYC
Date: May 23, 2021

Test Cases:
2
1
Dead_Bowie Fake_Thomas_Jefferson
3
Dead_Bowie Fake_Thomas_Jefferson
Fake_Thomas_Jefferson Fury_Leika
Fury_Leika Dead_Bowie

1
6
a b
d f
b c
c a
f g
b f

1
1
Dead_Bowie Fake_Thomas_Jefferson

Output:
Case #1: Yes
Case #2: No
Case #3: No

'''

from collections import defaultdict


def has_cycle(node, edges):
    pass


def solve(pairs):
    graph = defaultdict(list)
    for p1, p2 in pairs:
        graph[p1].append(p2)

    for n, e in graph.items():
        print(n, e)
        if has_cycle(n, e):
            return "No"

    return "Yes"


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        pairs = [input().strip().split() for _ in range(N)]

        result = solve(pairs)
        print(f"Case #{case}: {result}")
