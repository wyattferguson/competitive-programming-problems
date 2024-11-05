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
3
Dead_Bowie Fake_Thomas_Jefferson
Fake_Thomas_Jefferson Fury_Leika
Fury_Leika Dead_Bowie

1
1
Dead_Bowie Fake_Thomas_Jefferson

Output:
Case #1: Yes
Case #2: No
Case #3: No

'''

from collections import defaultdict


def has_cycle(g):
    path = set()
    visited = set()

    def visit(vertex):
        if vertex in visited:
            return False
        visited.add(vertex)
        path.add(vertex)
        print(path)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in g)


def solve(pairs):
    graph = defaultdict(list)
    for p1, p2 in pairs:
        graph[p1].append(p2)

    if has_cycle(graph):
        return "No"

    return "Yes"


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        pairs = [input().strip().split() for _ in range(N)]

        result = solve(pairs)
        print(f"Case #{case}: {result}")
