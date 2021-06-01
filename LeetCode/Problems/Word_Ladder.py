'''
Name: Word Ladder
URL: https://bit.ly/3oXFJMs
Date: May 27, 2021

Test Cases:
Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''

from collections import defaultdict


class Solution:
    def ladderLength(self, start: str, end: str, wordList) -> int:
        if end not in wordList or not start:
            return 0

        n = len(start)
        words = defaultdict(list)
        for w in wordList:
            for i in range(n):
                words[w[:i] + "*" + w[i+1:]].append(w)

        que = [(start, 1)]
        visited = set()
        visited.add(start)
        while que:
            word, level = que.pop(0)
            for i in range(n):
                pick = word[:i] + "*" + word[i+1:]
                for w in words[pick]:
                    if w == end:
                        return level + 1
                    if w not in visited:
                        visited.add(w)
                        que.append((w, level+1))

        return 0


if __name__ == "__main__":
    # beginWord = "teach"
    # endWord = "place"
    # wordList = ["peale", "wilts", "place", "fetch", "purer", "pooch",
    #            "peace", "poach", "berra", "teach", "rheum", "peach"]
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    solve = Solution()
    print(solve.ladderLength(beginWord, endWord, wordList))
