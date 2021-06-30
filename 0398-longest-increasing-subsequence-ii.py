"""
398. Longest Continuous Increasing Subsequence II
Hard
https://www.lintcode.com/problem/398/

Given an integer matrix. Find the longest increasing continuous subsequence in this matrix and return the length of it.

The longest increasing continuous subsequence here can start at any position and go up/down/left/right.

NOTE
x is rows and y is cols in grid
"""


class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """

    def longestContinuousIncreasingSubsequence2(self, matrix):
        if matrix is None or not matrix:
            return 0

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        n, m = len(matrix), len(matrix[0])
        dp = [[1] * m for _ in range(n)]
        points = [(x, y) for x in range(n) for y in range(m)]
        points = sorted(points, key=lambda p: matrix[p[0]][p[1]])

        for x, y in points:
            for dx, dy in directions:
                prev_x, prev_y = x + dx, y + dy

                if not self.is_valid(matrix, prev_x, prev_y):
                    continue
                if matrix[prev_x][prev_y] >= matrix[x][y]:
                    continue

                dp[x][y] = max(dp[x][y], dp[prev_x][prev_y] + 1)

        return max(max(row) for row in dp)

    def is_valid(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        else:
            return True


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [16, 17, 24, 23, 6],
        [15, 18, 25, 22, 7],
        [14, 19, 20, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    solution = Solution()
    answer = solution.longestContinuousIncreasingSubsequence2(matrix)
    print(answer)

    matrix = [[1, 2], [5, 3]]
    solution = Solution()
    answer = solution.longestContinuousIncreasingSubsequence2(matrix)
    print(answer)

    matrix = [[1, 5, 3], [4, 10, 9], [2, 8, 7]]
    solution = Solution()
    answer = solution.longestContinuousIncreasingSubsequence2(matrix)
    print(answer)
