"""
9. Palindrome Number
Easy
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        num = str(x)
        left, right = 0, len(num) - 1

        while left < right:
            if num[left] != num[right]:
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    x = 121
    output = Solution().isPalindrome(x)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    x = -121
    output = Solution().isPalindrome(x)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    x = 10
    output = Solution().isPalindrome(x)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
