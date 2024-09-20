"""
643. Maximum Average Subarray
Easy
https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        walker = 0
        sum_ = sum(nums[0:k])
        max_avg = sum_ / k

        while walker + k < n:
            sum_ = sum_ - nums[walker] + nums[walker + k]
            avg = sum_ / k
            max_avg = max(max_avg, avg)

            walker += 1

        return max_avg


if __name__ == "__main__":
    nums = [4,0,4,3,3]
    k = 5
    output = Solution().findMaxAverage(nums, k)
    expected = 2.8
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
