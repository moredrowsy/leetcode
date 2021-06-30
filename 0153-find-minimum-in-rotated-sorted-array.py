"""
153. Find Minimum in Rotated Sorted Array
Medium
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
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

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid

        return nums[left] if nums[left] < nums[right] else nums[right]


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    solution = Solution()
    answer = solution.findMin(nums)
    print(answer)

    nums = [4, 5, 6, 7, 0, 1, 2]
    solution = Solution()
    answer = solution.findMin(nums)
    print(answer)

    nums = [11, 13, 15, 17]
    solution = Solution()
    answer = solution.findMin(nums)
    print(answer)

    nums = [5, 1, 2, 3, 4]
    solution = Solution()
    answer = solution.findMin(nums)
    print(answer)
