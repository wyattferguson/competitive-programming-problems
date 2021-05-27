'''
Name: Rational Number Tree
URL: https://bit.ly/3ujmxdi
Date: May 26, 2021

Test Cases:
5
1 2
2 1 2
1 5
2 3 2
1 7

Output:
Case #1: 1 2
Case #2: 2
Case #3: 3 2
Case #4: 5
Case #5: 3 1

'''


def solve(p: int, q: int, n: int, question: bool):
    que = [[1, 1]]
    while True:
        cur_p, cur_q = que.pop(0)
        if question:
            if n == 1:
                return cur_p, cur_q
            n -= 1
        else:
            if p == cur_p and q == cur_q:
                return n
            n += 1
        que.append([cur_p, (cur_p+cur_q)])
        que.append([(cur_p+cur_q), cur_q])


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        k = list(map(int, input().strip().split()))
        if k[0] == 1:
            p, q = solve(1, 1, k[1], True)
            print(f"Case #{case}: {p} {q}")
        else:
            n = solve(k[1], k[2], 1, False)
            print(f"Case #{case}: {n}")
