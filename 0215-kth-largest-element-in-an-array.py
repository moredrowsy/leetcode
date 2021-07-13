"""
215. Kth Largest Element in an Array
Medium
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums:
            # quick_select gives k'th smallest, so reverse k to get kth largest
            k = len(nums) - k
            return self.quick_select(nums, 0, len(nums)-1, k)
        else:
            return -1

    def quick_select(self, nums, left, right, k):
        pivot = (left + right) // 2

        # Swap pivot to end; we're fixing the pivot at the end of list
        nums[pivot], nums[right] = nums[right], nums[pivot]

        count = left  # Counter to remember last swapped position
        walker = left  # Walks through list

        while walker < right:
            if nums[walker] < nums[right]:
                nums[walker], nums[count] = nums[count], nums[walker]
                count += 1
            walker += 1

        # Restore pivot
        nums[count], nums[right] = nums[right], nums[count]
        pivot = count

        if pivot == k:
            return nums[pivot]
        elif pivot < k:
            return self.quick_select(nums, pivot + 1, right, k)
        else:
            return self.quick_select(nums, left, pivot - 1, k)


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    answer = Solution().findKthLargest(nums, k)
    print(answer)
