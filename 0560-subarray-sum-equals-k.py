"""
560. Subarray Sum Equals K
Medium
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # calc prefix sum on the original array
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        count = defaultdict(int)
        count[0] = 1
        ans = 0

        for i in range(len(nums)):
            if nums[i] - k in count:
              ans += count[nums[i] - k]

            count[nums[i]] += 1

        return ans


if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    output = Solution().subarraySum(nums, k)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1,2,3]
    k = 3
    output = Solution().subarraySum(nums, k)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
