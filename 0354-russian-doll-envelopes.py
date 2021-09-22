"""
354. Russian Doll Envelopes
Hard
https://leetcode.com/problems/russian-doll-envelopes/

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Constraints:

1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 104
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Time Complexity
        ---------------
        O(n log n)

        Space Complexity
        ----------------
        O(n)
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        n = len(envelopes)
        dp = [float('inf')] * (n + 1)
        dp[0] = -float('inf')

        longest = 0
        for _, h in envelopes:
            index = self.first_gte(dp, h)
            dp[index] = h
            longest = max(longest, index)

        return longest

    def first_gte(self, nums, target):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if nums[left] >= target:
            return left
        return right


if __name__ == "__main__":
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    output = Solution().maxEnvelopes(envelopes)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    envelopes = [[1, 1], [1, 1], [1, 1]]
    output = Solution().maxEnvelopes(envelopes)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
    output = Solution().maxEnvelopes(envelopes)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
    output = Solution().maxEnvelopes(envelopes)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
