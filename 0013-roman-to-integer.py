"""
13. Roman to Integer
Easy
https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


class Solution:
    """
    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(1)
    """

    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "IV": 4,
            "IX": 9,
            "V": 5,
            "X": 10,
            "XL": 40,
            "XC": 90,
            "L": 50,
            "C": 100,
            "CD": 400,
            "CM": 900,
            "D": 500,
            "M": 1000,
        }

        n = len(s)
        num = 0

        i = 0
        while i + 1 < n:
            duo = s[i:i+2]

            if duo in roman_to_int:
                num += roman_to_int[duo]
                i += 2
            else:
                num += roman_to_int[s[i]]
                i += 1

        if i < n:
            num += roman_to_int[s[i]]
            n += 1

        return num


if __name__ == "__main__":
    s = "III"
    output = Solution().romanToInt(s)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = "LVIII"
    output = Solution().romanToInt(s)
    expected = 58
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = "MCMXCIV"
    output = Solution().romanToInt(s)
    expected = 1994
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = "X"
    output = Solution().romanToInt(s)
    expected = 10
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
