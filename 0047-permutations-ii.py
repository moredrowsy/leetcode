"""
47. Permutations II
Medium
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []

        if nums:
            nums.sort()
            visited = [False] * len(nums)
            permutation = []
            self.dfs(nums, visited, permutation, output)

        return output

    def dfs(self, nums, visited, permutation, output):
        """
        Preorder traversal
        Not bruteforce to check for unique permutation
        """
        # base case
        # done with permutation when length is same as length of nums
        if len(nums) == len(permutation):
            output.append(list(permutation))
        else:
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                # visit node
                permutation.append(nums[i])
                visited[i] = True

                self.dfs(nums, visited, permutation, output)

                # undo so we can permute others
                visited[i] = False
                permutation.pop()

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        output = []

        if nums:
            visited = set()
            permutation = []
            self.dfs2(nums, visited, permutation, output)

        return output

    def dfs2(self, nums: List[int], visited, permutation, output):
        """
        Preorder traversal
        Bruteforce-ish to get for unique permutation
        """
        # base case
        # done with permutation when length is same as length of nums
        if len(nums) == len(permutation):
            # check for unique permutation
            if permutation not in output:
                # make new copy or else we use ref
                output.append(list(permutation))
        else:
            for i in range(len(nums)):

                # visit node
                if i not in visited:
                    permutation.append(nums[i])
                    visited.add(i)

                    # visit children
                    self.dfs2(nums, visited, permutation, output)

                    # undo so we can permute others
                    visited.remove(i)
                    permutation.pop()


if __name__ == "__main__":
    nums = [1, 1]
    output = Solution().permuteUnique(nums)
    expected = [[1, 1]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nums = [2, 1, 1]
    output = Solution().permuteUnique(nums)
    expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nums = [1, 2, 2]
    output = Solution().permuteUnique(nums)
    expected = [[1, 2, 2], [2, 1, 2], [2, 2, 1]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nums = [1, 2, 3]
    output = Solution().permuteUnique(nums)
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nums = [3, 3, 0, 3]
    output = Solution().permuteUnique(nums)
    expected = [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
