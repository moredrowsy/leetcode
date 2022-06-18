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
        if len(s) <= 1:  # invalid case when only one char
            return False

        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:  # invalid if empty stack has no complement char
                    return False

                match = stack.pop()

                if match == "(" and char != ")":
                    return False

                if match == "{" and char != "}":
                    return False

                if match == "[" and char != "]":
                    return False

        return True if not stack else False  # invalid if stack still have chars


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
