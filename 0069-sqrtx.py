"""
69. Sqrt(x)
Easy
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""


class Solution:
    """
    Time Complexity
    ---------------
    O(log n)

    Space Complexity
    ----------------
    O(1)
    """

    def mySqrt(self, x: int) -> int:
        """
        Binary Search

        Explanation:
        Brute force numbers smaller than sqrtx whereby a*a <= x
        Since, we're searching linearly, can use binary search
        """
        left, right = 0, x

        while left + 1 < right:
            root = (left + right) // 2

            if root*root <= x:
                left = root
            else:
                right = root

        if right * right <= x:
            return right
        return left


if __name__ == "__main__":
    x = 4
    output = Solution().mySqrt(x)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    x = 8
    output = Solution().mySqrt(x)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
