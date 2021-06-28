"""
630. Knight Shortest Path II
Medium
https://www.lintcode.com/problem/630/

Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.

NOTE
x is rows and y is cols in grid
"""


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        if grid is None or not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        directions = [
            (-2, -1), (-2, 1), (-1, 2), (1, 2),
            (2, 1), (2, -1), (1, -2), (-1, -2),
        ]

        n, m = len(grid), len(grid[0])
        dp = [[float("inf")] * m for _ in range(n)]
        dp[0][0] = 0

        for j in range(1, m):
            for i in range(n):
                if not grid[i][j]:
                    for dx, dy in directions:
                        next_x, next_y = i + dx, j + dy

                        if self.is_valid(grid, next_x, next_y):
                            dp[i][j] = min(dp[i][j], dp[next_x][next_y] + 1)

        return -1 if dp[n-1][m-1] == float("inf") else dp[n-1][m-1]

    def is_valid(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False

        return grid[x][y] == 0


if __name__ == "__main__":
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    solution = Solution()
    answer = solution.shortestPath2(grid)
    print(answer)

    grid = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
    solution = Solution()
    answer = solution.shortestPath2(grid)
    print(answer)
