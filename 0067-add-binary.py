"""
67. Add Binary
Easy
https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.
"""


class Solution:
    """
    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(n)
    """

    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        m -= 1
        n -= 1
        binary = ""
        remainder = 0

        while m > -1 and n > -1:
            sum_ = int(a[m]) + int(b[n]) + remainder

            result = self.helper(sum_, binary)
            binary = result[0]
            remainder = result[1]

            m -= 1
            n -= 1

        while m > -1:
            sum_ = int(a[m]) + remainder

            result = self.helper(sum_, binary)
            binary = result[0]
            remainder = result[1]

            m -= 1

        while n > -1:
            sum_ = int(b[n]) + remainder

            result = self.helper(sum_, binary)
            binary = result[0]
            remainder = result[1]

            n -= 1

        if remainder:
            binary = str(remainder) + binary

        return binary

    def helper(self, sum_, binary):
        remainder = 0

        if sum_ == 2:
            remainder = 1
            binary = "0" + binary
        elif sum_ == 3:
            remainder = 1
            binary = "1" + binary
        else:
            binary = str(sum_) + binary

        return [binary, remainder]


if __name__ == "__main__":
    a, b = "11", "1"
    output = Solution().addBinary(a, b)
    expected = "100"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    a, b = "1010", "1011"
    output = Solution().addBinary(a, b)
    expected = "10101"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
