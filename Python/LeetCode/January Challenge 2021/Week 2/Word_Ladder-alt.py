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


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)

        return self.dive(beginWord, endWord, wordList, [])

    def dive(self, start, end, words, path):
        n = 0
        for w in words[:]:
            if self.diff(w, start) == 1:
                sub_words = words[:]
                sub_words.remove(w)
                sub_path = path[:]
                sub_path.append(w)

                if w == end:
                    return len(sub_path) + 1

                found = self.dive(w, end, sub_words, sub_path)
                if n == 0 or (found < n and found > 0):
                    n = found

        return n

    def diff(self, a, b):
        return sum(x != y for x, y in zip(a, b))


if __name__ == "__main__":
    beginWord = "teach"
    endWord = "place"
    wordList = ["peale", "wilts", "place", "fetch", "purer", "pooch",
                "peace", "poach", "berra", "teach", "rheum", "peach"]
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    solve = Solution()
    print(solve.ladderLength(beginWord, endWord, wordList))
