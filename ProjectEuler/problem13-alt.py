"""
This is an alternative solution that keeps the numbers as strings so they can be as big as your computer can handle and not limited by the size of an int. This was a personal challenge and not the best solution to the problem fyi.
"""

n = []
with open("problem13.in", "r") as f:
    for num in f:
        n.append(num.strip())

b = n[0]
for a in n[1:]:
    total = ""
    carry = 0

    # keep strings the same length
    if len(b) > len(a):
        a = "0" * (len(b) - len(a)) + a

    # start at right of string and move left
    for i in range(len(a) - 1, -1, -1):
        tmp = int(a[i]) + int(b[i]) + carry
        carry = 1 if tmp > 9 else 0
        total = str(tmp)[carry] + total

    if carry == 1:
        total = str(carry) + total
    b = total[:]

print(total)
print(total[0:10])
