'''
Name: Kth Missing Number
URL: https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/
Date: May 20,2021

Description:
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Ex1.
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Ex2. 
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

'''


def findKthPositive(arr, k):
    cnt = 0
    for x in range(1, max(arr)+k+1):
        if x not in arr:
            cnt += 1
            if cnt == k:
                return x


if __name__ == "__main__":
    k = 2
    arr = [1, 2, 3, 4]
    x = findKthPositive(arr, k)
    print(x)
