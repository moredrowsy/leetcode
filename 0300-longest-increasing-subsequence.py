"""
300. Longest Increasing Subsequence
Medium
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums:
            n = len(nums)
            dp = [1] * n

            for i in range(1, n):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)

            return max(dp)
        else:
            return 0


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    solution = Solution()
    answer = solution.lengthOfLIS(nums)
    print(answer)

    nums = [0, 1, 0, 3, 2, 3]
    solution = Solution()
    answer = solution.lengthOfLIS(nums)
    print(answer)

    nums = [7, 7, 7, 7, 7, 7, 7]
    solution = Solution()
    answer = solution.lengthOfLIS(nums)
    print(answer)
