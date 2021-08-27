"""
77. Combinations
Medium
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.dfs(n+1, k, 1, [], combinations)
        return combinations

    def dfs(self, n, k, start, combination, combinations):
        if len(combination) == k:
            combinations.append(combination[:])

        for i in range(start, n):
            combination.append(i)
            self.dfs(n, k, i+1, combination, combinations)
            combination.pop()


if __name__ == "__main__":
    n = 4
    k = 2
    output = Solution().combine(n, k)
    expected = [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4], ]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    n = 1
    k = 1
    output = Solution().combine(n, k)
    expected = [[1]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
