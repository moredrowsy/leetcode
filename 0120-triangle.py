"""
120. Triangle
Medium
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the rows below. More formally, if you are on index i on the current rows, you may move to either index i or index i + 1 on the next rows.
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle:
            rows = len(triangle)

            for i in range(1, rows):
                cols = len(triangle[i])

                for j in range(cols):
                    # left edge
                    if j == 0:
                        triangle[i][j] += triangle[i-1][j]
                    # right edge
                    elif j == cols - 1:
                        triangle[i][j] += triangle[i-1][j-1]
                    else:
                        triangle[i][j] += min(
                            triangle[i-1][j], triangle[i-1][j-1]
                        )

            return min(triangle[rows-1])
        else:
            return 0


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    solution = Solution()
    answer = solution.minimumTotal(triangle)
    print(answer)
