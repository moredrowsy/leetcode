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
        m, n = len(haystack), len(needle)

        for i in range(m):
            j = 0

            while j < n and i+j < m:
                if needle[j] != haystack[i+j]:
                    break
                j += 1

            # base case is taken care of when needle is empty
            # m is 0 and then j is also 0 because whlle loop does not exec
            if j == n:
                return i

        return -1


if __name__ == "__main__":
    haystack, needle = "hello", ""
    output = Solution().strStr(haystack, needle)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

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
