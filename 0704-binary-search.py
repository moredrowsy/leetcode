"""
704. Binary Search
Easy
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bs_recursion(nums, target, 0, len(nums)-1)

    def bs_recursion(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.bs_recursion(nums, target, mid, right)
            else:
                return self.bs_recursion(nums, target, left, mid)
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
            

    def bs_iteration(self, nums: List[int], target) -> int:
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
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


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 0
    solution = Solution()
    answer = solution.search(nums, target)
    print(answer)

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    solution = Solution()
    answer = solution.search(nums, target)
    print(answer)
