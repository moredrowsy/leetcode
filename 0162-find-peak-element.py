"""
162. Find Peak Element
Easy
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.find_peak_re(nums, 0, len(nums)-1)

    def find_peak_re(self, nums: List[int], left: int, right: int):
        """
        Time Complexity
        ---------------
        O(log n)

        Space Complexity
        ----------------
        O(1)
        """
        if left + 1 < right:
            mid = (left + right) // 2

            # Mountain peak
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            # ascending, go right
            elif nums[mid-1] < nums[mid]:
                return self.find_peak_re(nums, mid, right)
            # descending, go left
            else:
                return self.find_peak_re(nums, left, mid)

        # If we get to this point, we didn't find mountain peak (n=3)
        # At this point, n=1 or n=2
        # When n=1, left=right
        # When n=2, return max
        if nums[left] < nums[right]:
            return right
        else:
            return left

    def find_peak_iter(self, nums: List[int]):
        """
        Time Complexity
        ---------------
        O(log n)

        Space Complexity
        ----------------
        O(1)
        """
        left = 0
        right = len(nums) - 1

        # Either find mountain peak or reduces search to 1 or 2 elements
        while left + 1 < right:
            mid = (left + right) // 2

            # Mountain peak
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            # ascending, go right
            elif nums[mid-1] < nums[mid]:
                left = mid
            # descending, go left
            else:
                right = mid

        # If we get to this point, we didn't find mountain peak (n=3)
        # At this point, n=1 or n=2
        # When n=1, left=right
        # When n=2, return max
        if nums[left] < nums[right]:
            return right
        else:
            return left


if __name__ == "__main__":
    nums = [1]
    output = Solution().findPeakElement(nums)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 2]
    output = Solution().findPeakElement(nums)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [2, 1]
    output = Solution().findPeakElement(nums)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [3, 1, 2]
    output = Solution().findPeakElement(nums)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [3, 2, 1]
    output = Solution().findPeakElement(nums)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 2, 3, 1]
    output = Solution().findPeakElement(nums)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = nums = [1, 2, 1, 3, 5, 6, 4]
    output = Solution().findPeakElement(nums)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = nums = [1, 2, 3, 4, 3]
    output = Solution().findPeakElement(nums)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = nums = [1, 2, 3, 4, 5, 2, 1]
    output = Solution().findPeakElement(nums)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = nums = [1, 3, 2, 1]
    output = Solution().findPeakElement(nums)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
