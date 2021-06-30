"""
852. Peak Index in a Mountain Array
Easy
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.peak_index_re(arr, 0, len(arr)-1)

    def peak_index_linear(self, arr: List[int]) -> int:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        i = 1
        while arr[i] < arr[i+1]:
            i += 1
        return i

    def peak_index_re(self, arr: List[int], left: int, right: int) -> int:
        """
        Time Complexity
        ---------------
        O(log n)

        Space Complexity
        ----------------
        O(1)
        """
        if left + 1 < right:
            mid = (left + right) // 2

            # Mountain peak
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            # ascending, go right
            elif arr[mid-1] < arr[mid]:
                return self.peak_index_re(arr, mid, right)
            # descending, go left
            else:
                return self.peak_index_re(arr, left, mid)

        # If we get to this point, we didn't find mountain peak (n=3)
        # At this point, n=1 or n=2
        # When n=1, left=right
        # When n=2, return max
        if arr[left] < arr[right]:
            return right
        else:
            return left

    def peak_index_iter(self, arr: List[int]) -> int:
        """
        Time Complexity
        ---------------
        O(log n)

        Space Complexity
        ----------------
        O(1)
        """
        left = 0
        right = len(arr) - 1

        # Either find mountain peak or reduces search to 1 or 2 elements
        while left + 1 < right:
            mid = (left + right) // 2

            # Mountain peak
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            # ascending, go right
            elif arr[mid-1] < arr[mid]:
                left = mid
            # descending, go left
            else:
                right = mid

        # If we get to this point, we didn't find mountain peak (n=3)
        # At this point, n=1 or n=2
        # When n=1, left=right
        # When n=2, return max
        if arr[left] < arr[right]:
            return right
        else:
            return left


if __name__ == "__main__":
    arr = [0, 1, 0]
    solution = Solution()
    answer = solution.peakIndexInMountainArray(arr)
    print(answer)

    arr = [0, 2, 1, 0]
    solution = Solution()
    answer = solution.peakIndexInMountainArray(arr)
    print(answer)

    arr = [0, 10, 5, 2]
    solution = Solution()
    answer = solution.peakIndexInMountainArray(arr)
    print(answer)

    arr = [3, 4, 5, 1]
    solution = Solution()
    answer = solution.peakIndexInMountainArray(arr)
    print(answer)

    arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    solution = Solution()
    answer = solution.peakIndexInMountainArray(arr)
    print(answer)
