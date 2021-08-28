"""
39. Combination Sum
Medium
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], combinations)
        return combinations

    def dfs(self, candidates: List[int], target: int, index: int, combination: List[int], combinations: List[int]):
        if target < 0:
            return

        if target == 0:
            combinations.append(combination[:])

        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target -
                     candidates[i], i, combination, combinations)
            combination.pop()


if __name__ == "__main__":

    candidates = [2, 3, 6, 7]
    target = 7
    output = Solution().combinationSum(candidates, target)
    expected = [[2, 2, 3], [7]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    candidates = [2, 3, 5]
    target = 8
    output = Solution().combinationSum(candidates, target)
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    candidates = [2]
    target = 1
    output = Solution().combinationSum(candidates, target)
    expected = []
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    candidates = [1]
    target = 2
    output = Solution().combinationSum(candidates, target)
    expected = [[1, 1]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
