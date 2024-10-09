"""
525. Contiguous Array
Medium
https://leetcode.com/problems/contiguous-array/

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = 0
        indices = {0: -1}
        ans = 0

        for i in range(n):
            if nums[i] == 1:
                _sum += 1
            else:
                _sum -= 1

            if _sum in indices:
                ans = max(ans, i - indices[_sum])
            else:
                indices[_sum] = i

        return ans


if __name__ == "__main__":
    nums = [0,1]
    output = Solution().findMaxLength(nums)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
