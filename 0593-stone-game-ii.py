"""
593. Stone Game II
Medium
https://www.lintcode.com/problem/593

There is a stone game.At the beginning of the game the player picks n piles of stones in a circle.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.
"""


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def stoneGame2(self, A):
        n = len(A)
        if n < 1:
            return 0

        dp = [[float('inf')] * (2*n) for _ in range(2*n)]
        sum_ = [0]

        for i in range(2*n):
            sum_.append(sum_[-1] + A[i % n])
            dp[i][i] = 0

        for l in range(2, 2*n+1):
            for i in range(2*n):
                j = i + l - 1

                if j >= 2*n:
                    continue

                for k in range(i, j):
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] +
                                   sum_[j+1] - sum_[i], dp[i][j])

        stones = float('inf')
        for i in range(n):
            stones = min(stones, dp[i][i+n-1])

        return stones


if __name__ == "__main__":
    piles = [1, 1, 4, 4]
    output = Solution().stoneGame2(piles)
    expected = 18
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
