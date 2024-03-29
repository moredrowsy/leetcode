"""
12. Integer to Roman
Medium
https://leetcode.com/problems/integer-to-roman/

oman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ["M", "CM", "D", "CD", "C", "XC",
                  "L", "XL", "X", "IX", "V", "IV", "I"]
        digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ""

        for r, d in zip(romans, digits):
            # String can only be multiplied by int
            roman += r * (num // d)  # use integer dvision for int result
            num %= d  # use mod for int result

        return roman


if __name__ == "__main__":
    num = 3
    output = Solution().intToRoman(num)
    expected = "III"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    num = 58
    output = Solution().intToRoman(num)
    expected = "DVIII"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    num = 1994
    output = Solution().intToRoman(num)
    expected = "MCMXCIV"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
