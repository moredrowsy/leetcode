"""
33. Search in Rotated Sorted Array
Medium
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time Complexity
        ---------------
        O(log n)

        Space Complexity
        ----------------
        O(1)
        """
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid
                else:
                    left = mid
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    output = Solution().search(nums, target)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    output = Solution().search(nums, target)
    expected = -1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1]
    target = 0
    output = Solution().search(nums, target)
    expected = -1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1]
    target = 1
    output = Solution().search(nums, target)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 3, 5]
    target = 5
    output = Solution().search(nums, target)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [3, 5, 1]
    target = 3
    output = Solution().search(nums, target)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [5, 1, 3]
    target = 3
    output = Solution().search(nums, target)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    output = Solution().search(nums, target)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
