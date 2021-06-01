'''
Name: Two Sum
Problem URL: https://leetcode.com/problems/two-sum/
Date Completed: May 2021

Test Cases:
[-1,-2,-3,-4,-5]
-8

[3, 2, 4]
6

[2,7,11,15]
9

'''


def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]


if __name__ == "__main__":
    nums = [-1, -2, -3, -4, -5, 7, 99, -12]
    target = -8

    #result = dict((v, i) for i, v in enumerate(nums))
    result = twoSum(nums, target)
    print(result)
