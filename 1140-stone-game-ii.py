"""
1140. Stone Game II
Medium
https://leetcode.com/problems/stone-game-ii/

NOTE
This problem is differrent from the lintcode version.

Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Constraints:
1 <= piles.length <= 100
1 <= piles[i] <= 104
"""
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * (n+1) for _ in range(n+1)]
        sum_ = [0] * (n+1)

        # Get sum from piles[i:]
        # ie, get sum at position i to end of piles
        for i in range(n-1, -1, -1):
            sum_[i] = sum_[i+1] + piles[i]

        # Assign sum to last column vertically
        for i in range(n+1):
            dp[i][n] = sum_[i]

        for i in range(n-1, -1, -1):  # i is the pile
            for j in range(n-1, 0, -1):  # j is the M
                x = 1
                while x <= 2*j and i+x <= n:
                    dp[i][j] = max(dp[i][j], sum_[i] - dp[i+x][max(j, x)])
                    x += 1

        return dp[0][1]


if __name__ == "__main__":
    piles = [2, 7, 9, 4, 4]
    output = Solution().stoneGameII(piles)
    expected = 10
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    piles = [1, 2, 3, 4, 5, 100]
    output = Solution().stoneGameII(piles)
    expected = 104
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
