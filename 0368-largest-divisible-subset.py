"""
368. Largest Divisible Subset
Medium
https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Time Complexity
        ---------------
        O(n^2)

        Space Complexity
        ----------------
        O(n)
        """
        if nums is None or not nums:
            return []

        nums = sorted(nums)
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_count, max_index = -1, -1
        for i in range(n):
            if dp[i] > max_count:
                max_count = dp[i]
                max_index = i

        results = [-1] * dp[max_index]
        m = dp[max_index] - 1
        results[m] = nums[max_index]
        count = max_count - 1

        # rebuild the divisible subset backwards
        for i in range(max_index-1, -1, -1):
            if results[m] % nums[i] == 0 and count == dp[i]:
                m -= 1
                count -= 1
                results[m] = nums[i]

        return results


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    answer = solution.largestDivisibleSubset(nums)
    print(answer)

    nums = [1, 2, 4, 8]
    solution = Solution()
    answer = solution.largestDivisibleSubset(nums)
    print(answer)

    nums = [4, 8, 10, 240]
    solution = Solution()
    answer = solution.largestDivisibleSubset(nums)
    print(answer)

    nums = [2, 3, 4, 8]
    solution = Solution()
    answer = solution.largestDivisibleSubset(nums)
    print(answer)
