"""
55. Jump Game
Medium
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Time Complexity
        ---------------
        O(n^2)

        Space Complexity
        ----------------
        O(n^2)
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break

        return dp[n-1]


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    output = Solution().canJump(nums)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [3, 2, 1, 0, 4]
    output = Solution().canJump(nums)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [0, 2, 1, 0, 4]
    output = Solution().canJump(nums)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
