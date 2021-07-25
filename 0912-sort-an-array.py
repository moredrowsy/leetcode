"""
912. Sort an Array
Medium
https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order.

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.mergesort(nums, 0, len(nums))
        self.quicksort(nums, 0, len(nums))
        return nums

    def mergesort(self, nums: List[int], low: int, high: int):
        """
        Recursively sort array by halves; then merge the two sorted halves.

        Time Complexity
        ---------------
        O(nlogn)

        Space Complexity
        ----------------
        O(2n)
        """
        if low < high - 1:
            mid = (low + high) // 2
            self.mergesort(nums, low, mid)
            self.mergesort(nums, mid, high)
            self.merge(nums, low, mid, high)

    def merge(self, nums: List[int], low: int, mid: int, high: int):
        """
        Merge two sorted halves.

        Time Complexity
        ---------------
        O(2n)

        Space Complexity
        ----------------
        O(2n)
        """
        tmp = []
        i, j = low, mid  # i is left walker, j is right wlker

        # Merge left and right
        while i < mid and j < high:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1

        # Merge leftover values on left side
        while i < mid:
            tmp.append(nums[i])
            i += 1

        # Merge leftover values on right side
        while j < high:
            tmp.append(nums[j])
            j += 1

        # Copy tmp back into nums for in-place sorting
        for y, x in enumerate(range(low, high), 0):
            nums[x] = tmp[y]

    def quicksort(self, nums: List[int], low: int, high: int):
        """
        Pick a pivot. Move everything less than pivot to left.
        Recursively sort by pivot.

        Time Complexity
        ---------------
        Best : O(nlogn)
        Worst: O(n^2)
        Avg  : O(nlogn)

        Space Complexity
        ----------------
        O(n)
        """
        if low < high - 1:
            pivot = self.partition(nums, low, high)
            self.quicksort(nums, low, pivot)
            self.quicksort(nums, pivot + 1, high)

    def partition(self, nums: List[int], low: int, high: int):
        """
        Pick a pivot. Partition everything less than pivot to its left.

        Time Complexity
        ---------------
        O(n)
        """
        pivot = (low + high) // 2

        # Swap pivot to end; we're fixing the pivot at the end of list
        nums[pivot], nums[high-1] = nums[high-1], nums[pivot]

        count = low  # Counter to remember last swapped position
        walker = low  # Walks through list

        while walker < high - 1:
            if nums[walker] < nums[high - 1]:
                nums[walker], nums[count] = nums[count], nums[walker]
                count += 1
            walker += 1

        # Restore pivot
        nums[count], nums[high-1] = nums[high-1], nums[count]

        return count


if __name__ == "__main__":
    nums = [5, 1, 1, 2, 0, 0]
    output = Solution().sortArray(nums)
    expected = [0, 0, 1, 1, 2, 5]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
