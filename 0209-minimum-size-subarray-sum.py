"""
209. Minimum Size Subarray Sum
Medium
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = self.get_prefix_sum(nums)
        ans = float('inf')
        n = len(nums)
        j = 0

        for i in range(n):
            while j < n and prefix_sum[j] - prefix_sum[i] < target:
                j += 1

            if prefix_sum[j] - prefix_sum[i] >= target:
                length = j - i
                ans = min(ans, length)

        return 0 if ans == float('inf') else ans

    def get_prefix_sum(self, nums):
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        return prefix_sum

    def minSubArrayLen_jj(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1

        n = len(nums)
        min_length = n + 1
        _sum = 0
        j = 0

        for i in range(n):
            while j < n and _sum < target:
                _sum += nums[j]
                j += 1

            if _sum >= target:
                min_length = min(min_length, j - i)

            _sum -= nums[i]

        return 0 if min_length == n + 1 else min_length

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    output = Solution().minSubArrayLen(target, nums)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    target = 4
    nums = [1,4,4]
    output = Solution().minSubArrayLen(target, nums)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    target = 11
    nums = [1,1,1,1,1,1,1,1]
    output = Solution().minSubArrayLen(target, nums)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    target = 11
    nums = [1,2,3,4,5]
    output = Solution().minSubArrayLen(target, nums)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
