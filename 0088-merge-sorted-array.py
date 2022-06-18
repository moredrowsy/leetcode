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
        In-place merge sort

        Time Complexity
        ---------------
        O(m+n)

        Space Complexity
        ----------------
        O(1)
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Use mergesort's merge algorithm.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        left, right = 0, 0
        tmp = []

        while left < m and right < n:
            if nums1[left] < nums2[right]:
                tmp.append(nums1[left])
                left += 1
            else:
                tmp.append(nums2[right])
                right += 1

        while left < m:
            tmp.append(nums1[left])
            left += 1

        while right < n:
            tmp.append(nums2[right])
            right += 1

        for i in range(m+n):
            nums1[i] = tmp[i]

        return nums1


if __name__ == "__main__":
    nums1, m = [1, 2, 3, 0, 0, 0], 3
    nums2, n = [2, 5, 6], 3
    Solution().merge(nums1, m, nums2, n)
    output = nums1
    expected = [1, 2, 2, 3, 5, 6]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums1, m = [1, 5, 6,  0, 0, 0], 3
    nums2, n = [2,  2, 3], 3
    Solution().merge(nums1, m, nums2, n)
    output = nums1
    expected = [1, 2, 2, 3, 5, 6]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums1, m = [1], 1
    nums2, n = [], 0
    Solution().merge(nums1, m, nums2, n)
    output = nums1
    expected = [1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums1, m = [0], 0
    nums2, n = [1], 1
    Solution().merge(nums1, m, nums2, n)
    output = nums1
    expected = [1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
