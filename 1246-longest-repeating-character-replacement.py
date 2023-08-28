"""
1246. Longest Repeating Character Replacement
Medium
https://www.lintcode.com/problem/1246/

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Constraints:
- Both the string's length and k will not exceed 10^4.
"""


class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """

    def characterReplacement(self, s, k):
        counter = {}
        answer = 0
        right = 0
        max_freq = 0
        for left in range(len(s)):
            while right < len(s) and right - left - max_freq <= k:
                if s[right] in counter:
                    counter[s[right]] += 1
                else:
                    counter[s[right]] = 1

                max_freq = max(max_freq, counter[s[right]])
                right += 1

            if right - left - max_freq > k:
                answer = max(answer, right - 1 - left)
            else:
                answer = max(answer, right - left)

            counter[s[left]] -= 1
        return answer


if __name__ == "__main__":
    s, k = "ABAB", 2
    output = Solution().characterReplacement(s, k)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s, k = "AABABBA", 1
    output = Solution().characterReplacement(s, k)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
