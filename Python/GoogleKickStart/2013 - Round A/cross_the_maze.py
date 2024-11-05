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


def print_m(m):
    for r in m:
        print(r)
    print("\n")


def solve(m, sx, sy, ex, ey, size):
    path = []
    facing = ['N', 'E', 'S', 'W']
    last_move = 'N'
    m[ex][ey] = "X"
    for step in range(10000):
        m[sy][sx] = step
        print_m(m)
        for dir in facing[:]:
            if (sx+1) < size and m[sy][sx+1] != '#' and dir == 'E':
                last_move = 'E'
                sx += 1
                facing = ['N', 'E', 'S', 'W']
                break

            elif (sy+1) < size and m[sy+1][sx] != '#' and dir == 'S':
                last_move = 'S'
                sy += 1
                facing = ['E', 'S', 'W', 'N']
                break

            elif (sx-1) >= 0 and m[sy][sx-1] != '#' and dir == 'W':
                last_move = 'W'
                sx -= 1
                facing = ['S', 'W', 'N', 'E']
                break

            elif (sy-1) >= 0 and m[sy-1][sx] != '#' and dir == 'N':
                last_move = 'N'
                sy -= 1
                facing = ['W', 'N', 'E', 'S']
                break
        else:
            break

        path.append(last_move)
        if sy == ex and sx == ey:
            return len(path)

    return "Edison ran out of energy."


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        m = []
        for _ in range(N):
            line = input().strip()
            row = [c for c in line]
            m.append(row)
        sx, sy, ex, ey = list(map(int, input().strip().split()))
        result = solve(m, sx-1, sy-1, ex-1, ey-1, N)
        print(f"Case #{case}: {result}")
