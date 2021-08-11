"""
74. Search a 2D Matrix
Medium
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search version

        Time Complexity
        ---------------
        O(log n)

        Space Complexity
        ----------------
        O(1)
        """
        if not matrix or len(matrix) == 0 or not matrix[0] or len(matrix[0]) == 0:
            return False

        row, col = len(matrix), len(matrix[0])

        start, end = 0, row * col - 1
        while start + 1 < end:
            mid = (start + end) // 2
            num = matrix[mid // col][mid % col]

            if num == target:
                return True
            elif num > target:
                end = mid
            else:
                start = mid

        # Check if start is target
        if matrix[start // col][start % col] == target:
            return True
        # Check if end is target
        elif matrix[end // col][end % col] == target:
            return True
        else:
            return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    output = Solution().searchMatrix(matrix, target)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    output = Solution().searchMatrix(matrix, target)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    matrix = [[1, 4, 5], [6, 7, 8]]
    target = 8
    output = Solution().searchMatrix(matrix, target)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
