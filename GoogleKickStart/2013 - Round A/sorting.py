'''
Name: Sorting
URL: https://bit.ly/3fc1tB6
Date: May 23, 2021

Test Cases:
2
5
5 2 4 3 1
7
-5 -12 87 2 88 20 11

Output:
Case #1: 1 4 2 3 5
Case #2: -5 88 11 20 2 -12 87

'''


def solve(books):
    a = []
    b = []
    for n in books:
        if n % 2 == 0:
            b.append(n)
        else:
            a.append(n)

    a.sort()
    b.sort(reverse=True)

    result = []
    for i in books:
        book = str(a.pop(0) if i % 2 else b.pop(0))
        result.append(book)
    return result


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        N = int(input())
        nums = list(map(int, input().split()))

        result = solve(nums)
        print(f"Case #{case}: {' '.join(result)}")
