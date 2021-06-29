"""
34. Find First and Last Position of Element in Sorted Array
Medium
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.bsearch_first_last_re(nums, target)

    def bsearch_first_last_iter(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1, -1]

        first = self.bsearch_first_iter(nums, target)
        end = self.bsearch_last_iter(nums, target)
        return [first, end]

    def bsearch_first_iter(self, nums: List[int], target) -> int:
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

    def bsearch_last_iter(self, nums: List[int], target) -> int:
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1

    def bsearch_first_last_re(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1, -1]

        first = self.bsearch_first_re(nums, target, 0, len(nums) - 1)
        last = self.bsearch_last_re(nums, target, 0, len(nums) - 1)
        return [first, last]

    def bsearch_first_re(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return self.bsearch_first_re(nums, target, left, mid)
            elif nums[mid] < target:
                return self.bsearch_first_re(nums, target, mid, right)
            else:
                return self.bsearch_first_re(nums, target, left, mid)

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

    def bsearch_last_re(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return self.bsearch_last_re(nums, target, mid, right)
            elif nums[mid] < target:
                return self.bsearch_last_re(nums, target, mid, right)
            else:
                return self.bsearch_last_re(nums, target, left, mid)

        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1


if __name__ == "__main__":
    nums = nums = [1, 4]
    target = 4
    solution = Solution()
    answer = solution.searchRange(nums, target)
    print(answer)

    nums = nums = [8, 8]
    target = 8
    solution = Solution()
    answer = solution.searchRange(nums, target)
    print(answer)

    nums = nums = [1]
    target = 1
    solution = Solution()
    answer = solution.searchRange(nums, target)
    print(answer)

    nums = nums = [1, 3]
    target = 1
    solution = Solution()
    answer = solution.searchRange(nums, target)
    print(answer)

    nums = nums = [1, 1, 2]
    target = 1
    solution = Solution()
    answer = solution.searchRange(nums, target)
    print(answer)

    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution = Solution()
    answer = solution.searchRange(nums, target)
    print(answer)

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    solution = Solution()
    answer = solution.searchRange(nums, target)
    print(answer)
