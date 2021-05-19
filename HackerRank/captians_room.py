"""
Name: The Captain's Room
Problem URL: https://www.hackerrank.com/challenges/py-the-captains-room/problem
Date Completed: May 12, 2021

Test Case:
Input: 
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

Output:
8
"""


k = int(input())
rooms = list(map(int, input().split()))

seen = {}
for r in rooms:
    seen[r] = seen[r] + 1 if r in seen else 1

for room, cnt in seen.items():
    if cnt == 1:
        print(room)
        break
