"""
680. Valid Palindrome II
Easy
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
from typing import List, Tuple


class Solution:
    """
    Example cases
    abbad: Delete d and it's valid -> abba
    acbba: Delete c and it's valid -> abba
    """

    def validPalindrome(self, s: str) -> bool:
        """
        1. Find if original string is symmetric.
        2. If not symmetric, produce two variants
            a. First variant has first non-matching char removed
            b. Second variant has second non-matching char removed.
            c. Find if first or second variants is symmetric.

        Time Complexity
        ---------------
        Copy array to alpanum: O(n)
        Test original string: O(0.5n)
        Produce two variants: O(2n)
        Test two variants: O(n)
        Total: O(4.5n)

        Space Complexity
        ----------------
        Best: O(2n)
        Worst: O(4n)
        """
        # Build new string with only alphanumeric characters
        alphanum = ''
        n = len(s)
        for i in range(n):
            if s[i].isalnum():
                alphanum += s[i].upper()

        # Now test for symmetry
        has_symmetry, begin, end = self.is_symmetric(alphanum)

        # There's an off character
        if not has_symmetry:
            # Create first mutated string without the first off character
            alphanum1 = ''
            for j in range(0, begin):
                alphanum1 += alphanum[j]
            for j in range(begin+1, n):
                alphanum1 += alphanum[j]

            # Test for first mutated string
            has_symmetry, _, _ = self.is_symmetric(alphanum1, begin)
            if has_symmetry:
                return True

            # Create second mutated string without the second off character
            alphanum2 = ''
            for j in range(0, end):
                alphanum2 += alphanum[j]
            for j in range(end+1, n):
                alphanum2 += alphanum[j]

            # Test for second mutated string
            has_symmetry, _, _ = self.is_symmetric(alphanum2, begin)
            if has_symmetry:
                return True

            # No strings have symmetry
            return False

        # Original string has symmetry
        return True

    def is_symmetric(self, s: str, begin: int = 0) -> Tuple[bool, int, int]:
        """
        Test for symmetric alphanum string, case insensitive.
        T(n) = O(0.5n)
        """
        p = len(s)
        mid = p // 2
        end = p - 1
        begin = 0  # Walk until mid
        while begin < mid:
            if s[begin] != s[end-begin]:  # test against second half
                return (False, begin, end-begin)
            begin += 1
        return (True, begin, end-begin)


if __name__ == "__main__":
    s = "acbba"
    answer = Solution().validPalindrome(s)
    print(answer)

    s = "abbad"
    answer = Solution().validPalindrome(s)
    print(answer)

    s = "aba"
    answer = Solution().validPalindrome(s)
    print(answer)

    s = "abca"
    answer = Solution().validPalindrome(s)
    print(answer)

    s = "abc"
    answer = Solution().validPalindrome(s)
    print(answer)
