"""
46. Permutations
Medium
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        if nums:
            nums.sort()
            visited = set()
            permutation = []
            self.dfs(nums, visited, permutation, output)

        return output

    def dfs(self, nums: List[int], visited, permutation, output):
        """Preorder traversal"""
        # base case
        # done with permutation when length is same as length of nums
        if len(nums) == len(permutation):
            # make new copy or else we use ref
            output.append(list(permutation))
        else:
            for num in nums:

                # visit node
                if num not in visited:
                    permutation.append(num)
                    visited.add(num)

                    # visit children
                    self.dfs(nums, visited, permutation, output)

                    # undo so we can permute others
                    visited.remove(num)
                    permutation.pop()


if __name__ == "__main__":
    nums = [1, 2, 3]
    output = Solution().permute(nums)
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

    nums = [0, 1]
    output = Solution().permute(nums)
    expected = [[0, 1], [1, 0]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
    print(status)

    nums = [1]
    output = Solution().permute(nums)
    expected = [[1]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
