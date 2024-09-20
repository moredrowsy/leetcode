"""
392. Is Subsequence
Easy
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first, second = 0, 0
        n1 = len(s)
        n2 = len(t)

        while second < n2 and first < n1:
            if s[first] == t[second]:
                first += 1

            second += 1

        return first == n1

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    output = Solution().isSubsequence(s, t)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
