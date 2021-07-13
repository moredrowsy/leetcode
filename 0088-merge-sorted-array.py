"""
88. Merge Sorted Array
Easy
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""
from typing import List


class Solution:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Use mergesort's merge algorithm.

        Time Complexity
        ---------------
        O(2n)

        Space Complexity
        ----------------
        O(2n)
        """
        tmp = []
        i, j = 0, 0  # i is left walker, j is right walker

        # Merge left and right
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1

        # Merge leftover values on left side
        while i < m:
            tmp.append(nums1[i])
            i += 1

        # Merge leftover values on right side
        while j < n:
            tmp.append(nums2[j])
            j += 1

        # Copy tmp back into nums for in-place sorting
        p = len(tmp)
        for k in range(p):
            nums1[k] = tmp[k]


if __name__ == "__main__":
    nums1, m = [1, 2, 3, 0, 0, 0], 3
    nums2, n = [2, 5, 6], 3

    Solution().merge(nums1, m, nums2, n)
    print(nums1)
