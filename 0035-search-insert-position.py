"""
35. Search Insert Position
Easy
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    """
    Time Complexity
    ---------------
    O(log n)

    Space Complexity
    ----------------
    O(1)
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left + 1 < right:
            mid = (left+right) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid

        if target == nums[right]:
            return right
        if target == nums[left]:
            return left

        # Case 1: target between left and right
        if target < nums[right] and target > nums[left]:
            return left+1
        # Case 2: target less or equal to left
        elif target <= nums[left]:
            return left-1 if left-1 > 0 else 0
        # Case 3: target greater than right
        else:
            return right+1


if __name__ == "__main__":
    nums, target = [1], 1
    output = Solution().searchInsert(nums, target)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, target = [1, 3], 3
    output = Solution().searchInsert(nums, target)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, target = [1, 3, 5, 6], 5
    output = Solution().searchInsert(nums, target)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, target = [1, 3, 5, 6], 2
    output = Solution().searchInsert(nums, target)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, target = [1, 3, 5, 6], 7
    output = Solution().searchInsert(nums, target)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, target = [1, 3, 5, 6], 0
    output = Solution().searchInsert(nums, target)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
