"""
14. Longest Common Prefix
Easy
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time Complexity
        ---------------
        O(n^2)

        Space Complexity
        ----------------
        O(n)
        """
        n = len(strs)
        prefix = ""

        if n == 0:
            return prefix

        # iterate over each char in first word
        for i in range(len(strs[0])):
            # iterate over the other words
            for j in range(1, n):
                # boundary check
                if i >= len(strs[j]):
                    return prefix

                # new prefix no longer match, return cur prefix
                if strs[0][i] != strs[j][i]:
                    return prefix

            prefix += strs[0][i]

        return prefix


if __name__ == "__main__":
    strs = ["ab", "a"]
    output = Solution().longestCommonPrefix(strs)
    expected = "a"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    strs = ["flower", "flow", "flight"]
    output = Solution().longestCommonPrefix(strs)
    expected = "fl"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    strs = ["dog", "racecar", "car"]
    output = Solution().longestCommonPrefix(strs)
    expected = ""
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
