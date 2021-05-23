'''
Name:
URL:
Date:

Test Cases:
'''


def solve(n):
    return True


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        tests = [input() for _ in range(N)]

        result = solve(tests)
        print(f"Case #{case}: {result}")
