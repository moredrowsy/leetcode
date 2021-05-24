"""
283. Move Zeroes
Easy
https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
from typing import List


class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Use two walkers.
        First walker holds position for non-zero to move to.
        Second walker looks for non-zero to move to.

        tldr
        ----
        Move all non-zeroes to front; then replace everything after as zeroes.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        n = len(nums)

        i = -1  # First walker, position for non-zeroes to move to
        j = i + 1  # Second walker, walk until non-zero
        while j < n:
            if nums[j] != 0:
                i += 1
                nums[i] = nums[j]  # Move non-zero to first walker
            j += 1

        # All non-zeroes have been moved to front
        # So now replace everything after as zeroes
        i += 1
        while i < n:
            nums[i] = 0
            i += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)
