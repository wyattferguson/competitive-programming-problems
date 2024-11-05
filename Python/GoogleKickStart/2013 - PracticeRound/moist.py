'''
Name: Moist
URL: https://bit.ly/3hJLo7l
Date: May 23, 2021

Test Cases:
2
2
Oksana Baiul
Michelle Kwan
3
Elvis Stojko
Evgeni Plushenko
Kristi Yamaguchi

Output:
Case #1: 1
Case #2: 0
'''


def solve(names=[]):
    cost = 0
    for a in range(len(names) - 1):
        b = a+1
        if names[b] < names[a]:
            names[a], names[b] = names[b], names[a]
            cost += 1

    return cost


if __name__ == "__main__":
    n_cases = int(input())
    for case in range(1, n_cases+1):
        N = int(input())
        tests = [input() for _ in range(N)]

        result = solve(tests)
        print(f"Case #{case}: {result}")
