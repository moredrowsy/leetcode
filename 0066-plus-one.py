"""
66. Plus One
Easy
https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
from typing import List


class Solution:
    """
    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(n)
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        remainder = 0

        n = len(digits)-1
        for i in range(n, -1, -1):
            digits[i] += remainder

            if digits[i] > 9:
                digits[i] = 0
                remainder = 1
            else:
                remainder = 0

        if remainder:
            digits = [1] + digits

        return digits


if __name__ == "__main__":
    digits = [1, 2, 3]
    output = Solution().plusOne(digits)
    expected = [1, 2, 4]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    digits = [4, 3, 2, 1]
    output = Solution().plusOne(digits)
    expected = [4, 3, 2, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    digits = [9]
    output = Solution().plusOne(digits)
    expected = [1, 0]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    digits = [9, 9, 9]
    output = Solution().plusOne(digits)
    expected = [1, 0, 0, 0]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
