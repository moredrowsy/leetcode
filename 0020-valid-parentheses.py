"""
20. Valid Parentheses
Easy
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        matches = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []

        for ch in s:
            if ch in matches:
                stack.append(ch)
            else:
                if not stack:
                    return False

                open_ = stack.pop()
                if ch != matches[open_]:
                    return False

        return True if not stack else False


if __name__ == "__main__":
    s = "{"
    output = Solution().isValid(s)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = "(("
    output = Solution().isValid(s)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = "()"
    output = Solution().isValid(s)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = "()[]{}"
    output = Solution().isValid(s)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = s = "(]"
    output = Solution().isValid(s)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
