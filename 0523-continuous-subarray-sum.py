"""
523. Continuous Subarray Sum
Medium
https://leetcode.com/problems/continuous-subarray-sum/

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        indices = {0: -1}
        prefix_mod = 0
        n = len(nums)

        for i in range(n):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in indices:
                if i - indices[prefix_mod] > 1:
                    return True
            else:
                indices[prefix_mod] = i

        return False

if __name__ == "__main__":
    nums = [23,2,4,6,7]
    k = 6
    output = Solution().checkSubarraySum(nums, k)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
