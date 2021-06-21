"""
120. Triangle
Medium
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle:
            row = len(triangle)
            ans = [[0] * len(triangle[i]) for i in range(row)]

            # init
            ans[0][0] = triangle[0][0]

            for i in range(1, row):
                col = len(triangle[i])

                for j in range(col):
                    # left edge
                    if j == 0:
                        ans[i][j] = triangle[i][j] + ans[i-1][j]
                    # right edge
                    elif j == len(triangle[i]) - 1:
                        ans[i][j] = triangle[i][j] + ans[i-1][j-1]
                    else:
                        ans[i][j] = triangle[i][j] + min(
                            ans[i-1][j], ans[i-1][j-1]
                        )

            return min(ans[row-1])
        else:
            return 0


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    solution = Solution()
    answer = solution.minimumTotal(triangle)
    print(answer)
