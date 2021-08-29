"""
40. Combination Sum II
Medium
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        if candidates:
            candidates.sort()
            self.dfs(candidates, target, 0, [], combinations)
        return combinations

    def dfs(self, candidates: List[int], target: int, index: int, combination: List[int], combinations: List[int]):
        if target < 0:
            return

        if target == 0:
            combinations.append(combination[:])

        for i in range(index, len(candidates)):
            if i != index and candidates[i] == candidates[i-1]:
                continue

            combination.append(candidates[i])
            self.dfs(candidates, target -
                     candidates[i], i+1, combination, combinations)
            combination.pop()


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    output = Solution().combinationSum2(candidates, target)
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    candidates = [2, 5, 2, 1, 2]
    target = 5
    output = Solution().combinationSum2(candidates, target)
    expected = [[1, 2, 2], [5]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    candidates = [7, 1, 2, 5, 1, 6, 10]
    target = 8
    output = Solution().combinationSum2(candidates, target)
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    candidates = [1, 1, 1]
    target = 2
    output = Solution().combinationSum2(candidates, target)
    expected = [[1, 1]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
