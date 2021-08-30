"""
263. Ugly Number
Easy
https://leetcode.com/problems/ugly-number/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]

        for f in factors:
            while n >= f and n % f == 0:
                n /= f

        return n == 1


if __name__ == "__main__":
    n = 0
    output = Solution().isUgly(n)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 6
    output = Solution().isUgly(n)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 6
    output = Solution().isUgly(n)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 14
    output = Solution().isUgly(n)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
