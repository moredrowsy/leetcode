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
        Explanation
        -----------
        Compare last elements of nums1 and nums2
        a) Last item in nums1 is < than nums2's, then move nums2's to end
        b) Last item in nums1 is >= than nums2's, then move nums1's last to end
        c) If nums2 stil have items, copy from nums1 begining to end of nums2's

        Time Complexity
        ---------------
        O(m+n)

        Space Complexity
        ----------------
        O(1)
        """
        while m > 0 and n > 0:
            # if nums1 last is smaller than nums2 last, move nums2 last to end
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            # if nums1 last is larger than nums2 last, move nums1 last to end
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

        # if nums2 has items, copy to nums1 left -> right from index 0
        # if nums1 has items, than that means it's sorted; no action needed
        if n > 0:
            for i in range(n):
                nums1[i] = nums2[i]

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
    nums1, m = [6, 0, 0, 0, 0, 0], 1
    nums2, n = [1, 2, 2, 3, 5], 5
    Solution().merge(nums1, m, nums2, n)
    output = nums1
    expected = [1, 2, 2, 3, 5, 6]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums1, m = [1, 2, 0, 0, 0, 0], 2
    nums2, n = [2, 3, 5, 6], 4
    Solution().merge(nums1, m, nums2, n)
    output = nums1
    expected = [1, 2, 2, 3, 5, 6]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

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
