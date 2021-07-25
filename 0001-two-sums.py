"""
1. Two Sum
Easy
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Using dict to map values.

        Time Complexity
        ---------------
        O(2n)

        Space Complexity
        ----------------
        O(2n)
        """
        n = len(nums)

        # Map nums into dictionary as {value: [indices]}
        nums_map = {}
        for i in range(n):
            if nums[i] not in nums_map.keys():
                nums_map[nums[i]] = [i]
            else:
                nums_map[nums[i]].append(i)

            # Diff is the number we need to find
            diff = target - nums[i]

            # Diff found in map
            if diff in nums_map.keys():
                indices = nums_map[diff]

                # Check for index is not same as current
                for j in range(len(indices)):
                    if i != indices[j]:
                        return [i, indices[j]]

        return [-1, -1]  # Could not find

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Bruteforce

        Time Complexity
        ---------------
        O(n^2)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]


if __name__ == "__main__":
    nums, target = [-1, -2, -3, -4, -5], -8
    output = Solution().twoSum(nums, target)
    expected = [4, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, target = [2, 7, 11, 15], 18
    output = Solution().twoSum(nums, target)
    expected = [2, 1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, target = ([3, 3], 6)
    output = Solution().twoSum(nums, target)
    expected = [1, 0]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
