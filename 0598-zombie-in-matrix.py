"""
598. Zombie in Matrix
Medium
https://www.lintcode.com/problem/598/

Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.
"""
from collections import deque


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])

        if n == 0 or m == 0:
            return -1

        human = 0
        zombie = 1
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        # Each node is a tuple of (x, y)
        queue = deque([])
        for x in range(n):
            for y in range(m):
                if grid[x][y] == zombie:
                    queue.append((x, y))

        days = 0
        while queue:
            days += 1
            q_size = len(queue)

            for _ in range(q_size):
                x, y = queue.popleft()

                for dx, dy in directions:
                    next_x, next_y = x + dx, y + dy

                    if next_x >= 0 and next_x < n and \
                            next_y >= 0 and next_y < m and \
                            grid[next_x][next_y] == human:
                        grid[next_x][next_y] = zombie
                        queue.append((next_x, next_y))

        for x in range(n):
            for y in range(m):
                if grid[x][y] == 0:
                    return -1

        return days - 1


if __name__ == "__main__":
    grid = [[0, 1, 2, 0, 0],
            [1, 0, 0, 2, 1],
            [0, 1, 0, 0, 0]]
    output = Solution().zombie(grid)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]]
    output = Solution().zombie(grid)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    grid = [[0, 1, 2, 0, 0],
            [1, 2, 0, 2, 1],
            [1, 0, 0, 2, 1],
            [0, 1, 0, 0, 0]]
    output = Solution().zombie(grid)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    grid = [[0, 1, 2, 0, 0],
            [1, 2, 0, 2, 1],
            [1, 0, 2, 2, 1],
            [0, 1, 0, 0, 0]]
    output = Solution().zombie(grid)
    expected = -1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
