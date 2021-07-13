"""
26. Remove Duplicates from Sorted Array
Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Constraints:

0 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

NOTE
----
Do not need to actually remove duplicates as long as the unique values are in front.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Use two walkers.
        First walker is fixed at unique value.
        Second walker walks until new unique value.
        Move new unique value after first walker.
        Essentially, this will move all unique values to the front while
        duplicates are in the back.

        tldr
        ----
        Move all unique values to the front while duplicates are in the back.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        n = len(nums)

        i = 0  # First walker, fixed at unique value
        j = i + 1  # Second walker, walks until new unique value
        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]  # Move new unique after old unique
            j += 1

        # del nums[i+1:]
        return i + 1

    def removeDuplicates1(self, nums: List[int]) -> int:
        """
        Bruteforce

        Time Complexity
        ---------------
        O(n^2)
        """
        for i in range(len(nums)):
            j = i + 1

            while j < len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                else:
                    j += 1

        return len(nums)


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    answer = Solution().removeDuplicates(nums)
    print(answer)
    print(nums)
