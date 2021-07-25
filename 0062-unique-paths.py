"""
62. Unique Paths
Medium
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Constraints:

1 <= m, n <= 100
It's guaranteed that the output will be less than or equal to 2 * 109.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time Complexity
        ---------------
        O(n^2)

        Space Complexity
        ----------------
        O(n)
        """
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]


if __name__ == "__main__":
    m, n = 3, 7
    output = Solution().uniquePaths(m, n)
    expected = 28
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    m, n = 3, 2
    output = Solution().uniquePaths(m, n)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    m, n = 7, 3
    output = Solution().uniquePaths(m, n)
    expected = 28
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    m, n = 3, 3
    output = Solution().uniquePaths(m, n)
    expected = 6
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
