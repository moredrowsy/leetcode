"""
127. Word Ladder
Hard
https://leetcode.com/problems/word-ladder/

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time Complexity
        ---------------
        O(n * 26 * l^2)
        n = length of wordList
        l = length of each words

        Space Complexity
        ----------------
        O(n * 26 * l^2)
        """
        words = set(wordList)
        distance = 0
        queue = deque([beginWord])

        while queue:
            distance += 1
            size = len(queue)

            for _ in range(size):
                word = queue.popleft()

                if word == endWord:
                    return distance

                for next_word in self.get_next_word(word):
                    if next_word in words:
                        queue.append(next_word)
                        words.remove(next_word)

        return 0

    def get_next_word(self, word):
        words = []
        size = len(word)
        for i in range(size):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    output = Solution().ladderLength(beginWord, endWord, wordList)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    output = Solution().ladderLength(beginWord, endWord, wordList)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    output = Solution().ladderLength(beginWord, endWord, wordList)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
