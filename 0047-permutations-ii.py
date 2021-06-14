"""
47. Permutations II
Medium
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []

        if nums:
            visited = set()
            permutation = []
            self.dfs(nums, visited, permutation, output)

        return output

    def dfs(self, nums: List[int], visited, permutation, output):
        """Preorder traversal"""
        # base case
        # done with permutation when length is same as length of nums
        if len(nums) == len(permutation) and permutation not in output:
            # make new copy or else we use ref
            output.append(list(permutation))
        else:
            for i in range(len(nums)):

                # visit root
                if i not in visited:
                    permutation.append(nums[i])
                    visited.add(i)

                    # visit children
                    self.dfs(nums, visited, permutation, output)

                    # remove visited when we get out so we can permute
                    visited.remove(i)

                    # undo to get next slot for permutation
                    permutation.pop()


if __name__ == "__main__":
    nums = [1, 1, 2]
    solution = Solution()
    answer = solution.permuteUnique(nums)
    print(answer)

    nums = [1, 2, 3]
    solution = Solution()
    answer = solution.permuteUnique(nums)
    print(answer)
