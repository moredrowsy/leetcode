"""
53. Maximum Subarray
Easy
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
from typing import List
import sys


class Solution:
    """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Need to know Kadane's Algorithm.
        How the eff is this 'easy' if we don't know Kadane's Algorithm???

        Kadane's Algoithm explaination: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
        -------------------------------
        Let L = left pointer, R = right pointer
        Prefix sum from L+1 to r is max(P[R] - P[L]) = P[L+1, R]
        In for loop, P[R] is fixed. So to get max, then we need to minimize P[L]
        Hence, we do prefix_sum - min_sum
        """
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    output = Solution().maxSubArray(nums)
    expected = 6
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1]
    output = Solution().maxSubArray(nums)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [5, 4, -1, 7, 8]
    output = Solution().maxSubArray(nums)
    expected = 23
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
