"""
90. Subsets II
Medium
https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        if nums:
            nums.sort()
            self.dfs(nums, 0, [], subsets)

        return subsets

    def dfs(self, nums: List[int], index: int, subset: List[int], subsets: List[List[int]]):
        subsets.append(subset[:])

        for i in range(index, len(nums)):
            if i > index and nums[i-1] == nums[i]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i+1, subset, subsets)
            subset.pop()


if __name__ == "__main__":
    nums = [1, 2, 2]
    output = Solution().subsetsWithDup(nums)
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nums = [0]
    output = Solution().subsetsWithDup(nums)
    expected = [[], [0]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
