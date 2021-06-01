'''
Name: Boats to Save People
URL: https://bit.ly/3c168nu
Date: May 30, 2021

Test Cases:
Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
'''


class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        boats = low = 0
        high = len(people) - 1
        while low <= high:
            if (people[low] + people[high]) <= limit:
                low += 1
            high -= 1
            boats += 1

        return boats


if __name__ == "__main__":
    #people = [3, 5, 3, 4]
    people = [1, 4, 1, 5, 5, 5, 5, 5]
    limit = 5

    solve = Solution()
    print(solve.numRescueBoats(people, limit))
