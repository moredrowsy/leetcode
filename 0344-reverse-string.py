"""
344. Reverse String
Easy
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        n = len(s)
        left, right = 0, n-1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left, right = left+1, right-1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    expected = ["o", "l", "l", "e", "h"]
    print(f"\noutput\t\t{s}")
    print(f"expected\t{expected}")
    print(s == expected)

    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    expected = ["h", "a", "n", "n", "a", "H"]
    print(f"\noutput\t\t{s}")
    print(f"expected\t{expected}")
    print(s == expected)
