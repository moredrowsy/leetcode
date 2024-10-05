"""
2760. Longest Even Odd Subarray With Threshold
Easy
https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

You are given a 0-indexed integer array nums and an integer threshold.

Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length) that satisfies the following conditions:

nums[l] % 2 == 0
For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
For all indices i in the range [l, r], nums[i] <= threshold
Return an integer denoting the length of the longest such subarray.

Note: A subarray is a contiguous non-empty sequence of elements within an array.
"""

from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        left = 0
        ans = int(nums[0] % 2 == 0 and nums[0] <= threshold)
        n = len(nums)

        for right in range(n):
            if nums[left] % 2 != 0 or nums[left] > threshold \
            or nums[right] > threshold \
            or (right and nums[right] % 2 == nums[right - 1] % 2):
                left = right

            if nums[left] % 2 == 0 and nums[left] <= threshold:
                ans = max(ans, right - left + 1)

        return ans

if __name__ == "__main__":
    nums = [3,2,5,4]
    threshold = 5
    output = Solution().longestAlternatingSubarray(nums, threshold)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [2,3,4,5]
    threshold = 4
    output = Solution().longestAlternatingSubarray(nums, threshold)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [2,2]
    threshold = 18
    output = Solution().longestAlternatingSubarray(nums, threshold)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1,1]
    threshold = 18
    output = Solution().longestAlternatingSubarray(nums, threshold)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
