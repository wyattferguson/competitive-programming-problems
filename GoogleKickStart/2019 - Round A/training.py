'''
Name: Training
URL: https://bit.ly/3vqYiLE
Date: May 27, 2021

Test Cases:
3
4 3
3 1 9 100
6 2
5 5 1 2 3 4
5 5
7 7 1 7 7

Output:
Case #1: 14
Case #2: 0
Case #3: 6
'''


def solve(p, students):
    picks = [s for s in range(P)]
    min_training = 0
    for s in students:
        pass

    return min_training


def gen(S, rotor, pick):
    if rotor >= len(pick):
        return True
    for l in S:
        if l not in pick:
            pick[rotor] = l
            print(pick)
            gen(S, rotor+1, pick)
    return True


if __name__ == "__main__":
    P = 2
    S = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    picks = [S[0]] * P
    gen(S, 0, picks)

    '''
    T = int(input())
    for case in range(1, T+1):
        N, P = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        result = solve(P, S)
        print(f"Case #{case}: {result}")
    '''
