"""
28. Implement strStr()
Easy
https://leetcode.com/problems/implement-strstr/

Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time Complexity
        ---------------
        O(n*m)

        Space Complexity
        ----------------
        O(1)
        """
        n, m = len(haystack), len(needle)

        for i in range(n):
            j = 0

            while j < m and i+j < n:
                if needle[j] != haystack[i+j]:
                    break
                j += 1

            if j == m:
                return i

        return -1


if __name__ == "__main__":
    haystack, needle = "hello", "ll"
    output = Solution().strStr(haystack, needle)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    haystack, needle = "aaaaa", "bba"
    output = Solution().strStr(haystack, needle)
    expected = -1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
