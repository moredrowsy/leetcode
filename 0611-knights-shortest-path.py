"""
611. Knight Shortest Path
Medium
https://leetcode.com/problems/minimum-knight-moves/
https://www.lintcode.com/problem/611/

Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

NOTE
x is rows and y is cols in grid
"""
from collections import deque


class Point:
    """
Definition for a point.
"""

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        # 360 degree direcions coverage for knight moves
        directions = [
            (-2, -1), (-2, 1), (-1, 2), (1, 2),
            (2, 1), (2, -1), (1, -2), (-1, -2),
        ]

        queue = deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()

            # exit case
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]

            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy

                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(grid, next_x, next_y):
                    continue

                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))

        return -1

    def is_valid(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False

        return grid[x][y] == 0


if __name__ == "__main__":
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    source = Point(2, 0)
    destination = Point(2, 2)
    answer = Solution().shortestPath(grid, source, destination)
    print(answer)

    grid = [[0, 1, 0],
            [0, 0, 1],
            [0, 0, 0]]
    source = Point(2, 0)
    destination = Point(2, 2)
    answer = Solution().shortestPath(grid, source, destination)
    print(answer)

    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
    source = Point(2, 0)
    destination = Point(2, 2)
    answer = Solution().shortestPath(grid, source, destination)
    print(answer)
