"""
67. Add Binary
Easy
https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        m, n = len(a)-1, len(b)-1
        binary = ""
        carry = 0

        while m > -1 or n > -1:
            x = int(a[m]) if m > -1 else 0
            y = int(b[n]) if n > -1 else 0

            sum_ = x + y + carry
            binary = str(sum_ % 2) + binary
            carry = sum_ // 2

            m -= 1
            n -= 1

        if carry:
            binary = "1" + binary

        return binary


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
