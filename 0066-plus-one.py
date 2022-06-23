"""
66. Plus One
Easy
https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        carry = 1

        n = len(digits)-1
        for i in range(n, -1, -1):
            if carry == 0:
                return digits

            sum_ = digits[i] + carry
            digits[i] = sum_ % 10
            carry = sum_ // 10

        return [carry] + digits if carry else digits


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
