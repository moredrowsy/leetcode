"""
780. Remove Invalid Parentheses
Hard
https://www.lintcode.com/problem/780/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
"""


class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """

    def removeInvalidParentheses(self, s):
        output = []

        left, right = self.get_left_right_count(s)
        self.dfs(s, left, right, 0, output)

        return output

    def dfs(self, s, left, right, index, output):
        """
        @param left is left count, NOT left pointer
        @param right is right count, NOT right pointer
        @param index is the starting index to the for loop
        """
        if self.is_valid(s):
            output.append(s)
            return

        for i in range(index, len(s)):
            if i > index and s[i] == s[i] == s[i-1]:
                continue

            substr = s[:i] + s[i+1:]
            if s[i] == "(" and left > 0:
                self.dfs(substr, left-1, right, i, output)

            if s[i] == ")" and right > 0:
                self.dfs(substr, left, right-1, i, output)

    def is_valid(self, s):
        left, right = self.get_left_right_count(s)
        return left == right == 0

    def get_left_right_count(self, s):
        """Get left and right mismatched count"""
        left = right = 0

        for char in s:
            if char == "(":
                left += 1
            if char == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1

        return left, right


if __name__ == "__main__":
    s = "()())()"
    output = Solution().removeInvalidParentheses(s)
    expected = ["(())()", "()()()"]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    s = ")("
    output = Solution().removeInvalidParentheses(s)
    expected = [""]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
