"""
200. Number of Islands
Medium
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List, Set, Tuple
from collections import deque


class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Using dict to map values.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        islands = 0

        if grid and grid[0]:
            m, n = len(grid), len(grid[0])
            visited = set()

            for i in range(m):
                for j in range(n):
                    if (i, j) not in visited and grid[i][j] == '1':
                        islands += 1
                        visited.add((i, j))
                        self.bfs(grid, (i, j), visited)

        return islands

    def bfs(self, grid: List[List[str]], node: Tuple[int, int], visited: Set[Tuple[int, int]]):
        queue = deque([node])
        while queue:
            x, y = queue.popleft()
            for dx, dy in self.directions:
                next_x, next_y = x + dx, y + dy

                if (next_x, next_y) in visited:
                    continue

                if self.is_valid(grid, next_x, next_y):
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

    def is_valid(self, grid: List[List[str]], x: int, y: int):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
            return False
        return True


def convert_to_char_grid(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if type(grid[i][j]) is not str:
                grid[i][j] = str(grid[i][j])


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    convert_to_char_grid(grid)
    output = Solution().numIslands(grid)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    convert_to_char_grid(grid)
    output = Solution().numIslands(grid)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    convert_to_char_grid(grid)
    output = Solution().numIslands(grid)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    grid = [
        [1, 1]
    ]
    convert_to_char_grid(grid)
    output = Solution().numIslands(grid)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
