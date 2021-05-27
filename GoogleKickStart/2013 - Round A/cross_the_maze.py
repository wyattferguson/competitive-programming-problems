'''
Name: Cross The Maze
URL: https://bit.ly/3uopg5j
Date: May 26, 2021

Test Cases:
3
2
.#
#.
1 1 2 2
5
.##.#
.....
...#.
.###.
...#.
1 1 5 3
3
...
.#.
...
1 1 3 3

Output:
Case #1: Edison ran out of energy.
Case #2: 22
SEEENSESSSNNNWWSWWSSEE
Case #3: 4
EESS

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
