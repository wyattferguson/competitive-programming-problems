'''
Name: Longest Collatz sequence
Problem URL: https://projecteuler.net/problem=14
Date Completed: May 2021 
Description: A iterative solution to problem 14 vs the math solution in the other file.
'''

import time

start = time.time()

n = 1000000
max_chain = max_start = 0
jumps = {1: 1}
for i in range(2, n):
    if i not in jumps:
        new_jumps = []
        chain = 1
        k = i

        while True:
            k = k / 2 if k % 2 == 0 else (k * 3) + 1

            if k in jumps:
                chain += jumps[k]
                for v, j in enumerate(reversed(new_jumps)):
                    if j > i and j < n:
                        jumps[j] = v + jumps[k] + 1
                break
            else:
                new_jumps.append(k)
                chain += 1

        if chain > max_chain:
            max_chain = chain
            max_start = i

print(max_start, max_chain)
print(f"time taken: {time.time() - start}")
