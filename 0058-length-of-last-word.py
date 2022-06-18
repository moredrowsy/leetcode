"""
58. Length of Last Word
Easy
https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
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

    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1

        while right > -1 and s[right] == " ":
            right -= 1

        count = 0
        while right > -1 and s[right] != " ":
            count += 1
            right -= 1

        return count


if __name__ == "__main__":
    s = "Hello World"
    output = Solution().lengthOfLastWord(s)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = "   fly me   to   the moon  "
    output = Solution().lengthOfLastWord(s)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = s = "luffy is still joyboy"
    output = Solution().lengthOfLastWord(s)
    expected = 6
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = s = "Today is a nice day"
    output = Solution().lengthOfLastWord(s)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
