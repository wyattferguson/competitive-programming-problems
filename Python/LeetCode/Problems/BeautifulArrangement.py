'''
Name: Beautiful Arrangement
Problem URL: https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3591/
Date Completed: May 19, 2021

Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

Constraints:
1 <= n <= 15

Ex. 
Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
'''


class Solution:
    def countArrangement(self, n, perm=[], cnt=0):
        if len(perm) == n:
            return cnt + 1

        for p in range(1, n+1):
            if p not in perm:
                if (len(perm) + 1) % p == 0 or p % (len(perm) + 1) == 0:
                    cnt = self.countArrangement(n, perm + [p], cnt)

        return cnt
