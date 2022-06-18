"""
70. Climbing Stairs
Easy
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    """
    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(n)
    """

    def climbStairs(self, n: int) -> int:
        """
        Type: dynamic programming

        Explaination
        ------------
        The number of possibilities for n=1 stairs: 1
        The number of possibilities for n=2 stairs: 2
        The number of possibilities for n=3 stairs: 1+2=3
        The number of possibilities for n=4 stairs: 2+3=5
        The number of possibilities for n stairs is the previous two
        In other words, the fibonnaci sequence.
        """
        if n < 3:
            return n

        dp = [None] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]


if __name__ == "__main__":
    n = 1
    output = Solution().climbStairs(n)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 2
    output = Solution().climbStairs(n)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 3
    output = Solution().climbStairs(n)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 4
    output = Solution().climbStairs(n)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
