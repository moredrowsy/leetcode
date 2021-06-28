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

    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    def longestContinuousIncreasingSubsequence2(self, matrix):
        if matrix:

            n, m = len(matrix), len(matrix[0])
            dp = [[0] * m for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    self.search(matrix, dp, i, j)

            return max(max(row) for row in dp)
        else:
            return 0

    def search(self, matrix, dp, x, y):
        # base case
        if dp[x][y] != 0:
            return dp[x][y]

        longest = 1
        for dx, dy in self.directions:
            next_x, next_y = x + dx, y + dy

            if not self.is_valid(matrix, next_x, next_y):
                continue
            if matrix[x][y] >= matrix[next_x][next_y]:
                continue

            longest = max(longest, self.search(matrix, dp, next_x, next_y) + 1)

        dp[x][y] = longest
        return dp[x][y]

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

    matrix = [
        [1, 2],
        [5, 3]
    ]
    solution = Solution()
    answer = solution.longestContinuousIncreasingSubsequence2(matrix)
    print(answer)
