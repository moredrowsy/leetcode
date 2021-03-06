"""
658. Find K Closest Elements
Medium
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = self.find_left_bound_to_x(arr, x)
        right = left + 1

        while right - left <= k:
            if self.find_closest_to_x(arr, x, left, right) == left:
                left -= 1
            else:
                right += 1

        return arr[left+1:right]

    def find_left_bound_to_x(self, arr, x):
        """
        Find the left boundary index to x.
        If there are duplicate x's, it will NOT be the leftmost but +1 to
        the leftmost index based on business logic.
        """
        left, right = 0, len(arr) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if arr[mid] == x:
                right = mid
            elif arr[mid] < x:
                left = mid
            else:
                right = mid

        return self.find_closest_to_x(arr, x, left, right)

    def find_closest_to_x(self, arr, x, left, right):
        """
        Find index closet to X from constraints.
        Assume that either left or right is valid index based on constraints.
        """
        if left < 0:
            return right
        elif right >= len(arr):
            return left
        elif abs(arr[left] - x) < abs(arr[right] - x):
            return left
        elif abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right]:
            return left
        else:
            return right


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    output = Solution().findClosestElements(arr, k, x)
    expected = [1, 2, 3, 4]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    output = Solution().findClosestElements(arr, k, x)
    expected = [1, 2, 3, 4]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    arr = [1]
    k = 1
    x = 1
    output = Solution().findClosestElements(arr, k, x)
    expected = [1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    arr = [-2, -1, 1, 2, 3, 4, 5]
    k = 7
    x = 3
    output = Solution().findClosestElements(arr, k, x)
    expected = [-2, -1, 1, 2, 3, 4, 5]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
