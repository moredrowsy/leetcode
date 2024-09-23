"""
78. Subsets
Medium
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # subsets = []
        # if nums:
        #     nums.sort()
        #     self.dfs(nums, 0, [], subsets)
        # return subsets
        return self.dfs_iter(nums)

    def dfs(self, nums: List[int], index: int, subset: List[int], subsets: List[List[int]]):
        if index == len(nums):
            subsets.append(subset[:])
            return

        subset.append(nums[index])
        self.dfs(nums, index+1, subset, subsets)

        subset.pop()
        self.dfs(nums, index+1, subset, subsets)

    def dfs_iter(self, nums):
        """
        Generation of node is from current index + 1 to end of array
        Do the same for subset
        At every loop, pop both subset and index.
        At end of loop, subset is your answer
        """
        subsets = []
        subset = []
        stack = [-1] # stack of indices
        n = len(nums)

        while stack:
            if stack:
              index = stack.pop()
            if subset:
              subset.pop()

            for i in range(index + 1, n):
                stack.append(i)
                subset.append(nums[i])

            subsets.append(subset[:])

        return subsets

if __name__ == "__main__":
    nums = [1, 2, 3]
    output = Solution().subsets(nums)
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nums = [0]
    output = Solution().subsets(nums)
    expected = [[], [0]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nums = [3, 9]
    output = Solution().subsets(nums)
    expected = [[], [3], [9], [3,9]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
