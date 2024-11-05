'''
Name: Count Substrings
URL: https://www.hackerrank.com/challenges/find-a-string/problem
Date Completed: May 21, 2021
'''


def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            sub_len = len(sub_string) + i
            if sub_len <= len(string) and string[i:sub_len] == sub_string:
                cnt += 1
    return cnt


if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"

    count = count_substring(string, sub_string)
    print(count)
