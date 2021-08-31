"""
75. Sort Colors
Medium
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        left, mid, right = 0, 0, len(nums)-1

        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            else:
                mid += 1

        return nums


if __name__ == "__main__":
    nums = [0]
    output = Solution().sortColors(nums)
    expected = [0]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1]
    output = Solution().sortColors(nums)
    expected = [1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [2, 0, 1]
    output = Solution().sortColors(nums)
    expected = [0, 1, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [2, 0, 2, 1, 1, 0]
    output = Solution().sortColors(nums)
    expected = [0, 0, 1, 1, 2, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 2, 0]
    output = Solution().sortColors(nums)
    expected = [0, 1, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
