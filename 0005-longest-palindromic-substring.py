"""
5. Longest Palindromic Substring
Medium
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.dp_palindrome(s)

    def dp_palindrome(self, s: str) -> str:
        """
        Time Complexity
        ---------------
        O(n^2)

        Space Complexity
        ----------------
        O(n^2)
        """
        if not s:
            return ""

        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        for i in range(1, n):
            dp[i][i-1] = True

        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n-length):
                j = i + length
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

                if dp[i][j] and length + 1 > longest:
                    longest = length + 1
                    start, end = i, j

        return s[start:end+1]

    def bruteforce(self, s: str) -> str:
        """
        Time Complexity
        ---------------
        O(n^2)

        Space Complexity
        ----------------
        O(1)
        """
        if not s:
            return ""

        answer = (0, 0)
        for mid in range(len(s)):
            answer = max(answer, self.get_palindrom_from(s, mid, mid))
            answer = max(answer, self.get_palindrom_from(s, mid, mid + 1))

        return s[answer[1]: answer[0] + answer[1]]

    def get_palindrom_from(self, s, left, right):
        """
        Using left and right pointers:
         - return the starting position @ left
         - return the distance from left to right
         - return distance as the first tuple so we can take the max

        NOTE
        1. left and right is out of bounds after while loop
        2. left and right do not point to palindromic chars after while loop
        3. B/c #1 and #2:
            a. left starting position is left + 1
            b. right ditance is right - left plus - 1

        Return
        ------
        (right_dist, start_pos)
        substring = [start_pos : start_pos + right_dist]
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 1, left + 1)


if __name__ == "__main__":
    s = "babad"
    output = Solution().longestPalindrome(s)
    expected = ["bab", "aba"]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output in expected)

    s = "cbbd"
    output = Solution().longestPalindrome(s)
    expected = ["bb"]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output in expected)

    s = "a"
    output = Solution().longestPalindrome(s)
    expected = ["a"]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output in expected)

    s = "ac"
    output = Solution().longestPalindrome(s)
    expected = ["a", "c"]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output in expected)
