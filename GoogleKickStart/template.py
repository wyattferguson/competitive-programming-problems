'''
Name:
URL:
Date:

Test Cases:
'''


def solve(names=[]):
    cost = 0

    return cost


if __name__ == "__main__":
    n_cases = int(input())
    for case in range(1, n_cases+1):
        N = int(input())
        tests = [input() for _ in range(N)]

        result = solve(tests)
        print(f"Case #{case}: {result}")
