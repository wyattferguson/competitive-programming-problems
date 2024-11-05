"""
Name: Longest Collatz sequence
Problem URL: https://projecteuler.net/problem=14
Date Completed: May 2021 

Description:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
import time

start = time.time()

n = 1000000
max_chain = max_start = 0
jumps = {1: 1}
for i in range(2, n):
    chain = 1
    k = i

    while True:
        k = k / 2 if k % 2 == 0 else (k * 3) + 1

        if k in jumps:
            chain += jumps[k]
            break
        else:
            chain += 1

    jumps[i] = chain
    if chain > max_chain:
        max_chain = chain
        max_start = i

print(max_start, max_chain)
print(f"time taken: {time.time() - start}")
