"""
125. Valid Palindrome
Easy
https://leetcode.com/problems/valid-palindrome/

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Create alphanumeric string. Test for symmetry.

        Time Complexity
        ---------------
        O(1.5n)

        Space Complexity
        ----------------
        O(2n)
        """
        # Build new string with only alphanumeric characters
        alphanum = ''
        n = len(s)
        for i in range(n):
            if s[i].isalnum():
                alphanum += s[i].upper()

        # Now test for symmetry
        p = len(alphanum)
        mid = p // 2
        end = p - 1
        i = 0  # Walk until mid
        while i < mid:
            if alphanum[i] != alphanum[end-i]:  # test against second half
                return False
            i += 1
        return True

    def isPalindrome1(self, s: str) -> bool:
        """
        Walk left n times and right n times and check for same char.

        Time Complexity
        ---------------
        O(2n)

        Space Complexity
        ----------------
        O(n)
        """
        n = len(s)

        l = 0  # Left walker
        r = n - 1  # Right walker

        while l < n and r > -1:
            # Walk left side until alphanumeric
            while l < n and not s[l].isalnum():
                l += 1
            # Walk right side until alphanumeric
            while r > -1 and not s[r].isalnum():
                r -= 1

            if s[l].upper() != s[r].upper():
                return False

            l += 1
            r -= 1

        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    answer = Solution().isPalindrome(s)
    print(answer)

    s = "race a car"
    answer = Solution().isPalindrome(s)
    print(answer)
