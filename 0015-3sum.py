"""
15. 3Sum
Medium
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity
        ---------------
        O(n^2)

        Space Complexity
        ----------------
        O(n)
        """
        results = []

        n = len(nums)
        if n > 2:
            nums = sorted(nums)

            for i in range(n-2):
                # Skip duplicate numbers
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                target = -nums[i]
                left = i + 1
                right = n - 1
                self.two_sum(nums, left, right, target, results)

        return results

    def two_sum(self, nums: List[int], left: int, right: int, target: int, results: List[int]):
        while left < right:
            lr_sum = nums[left] + nums[right]

            if lr_sum < target:
                left += 1
            elif lr_sum > target:
                right -= 1
            else:
                results.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicates
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    output = Solution().threeSum(nums)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [0, 0, 0, 0]
    output = Solution().threeSum(nums)
    expected = [[0, 0, 0]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [-2, 0, 0, 2, 2]
    output = Solution().threeSum(nums)
    expected = [[-2, 0, 2]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [-2, 0, 1, 1, 2]
    output = Solution().threeSum(nums)
    expected = [[-2, 0, 2], [-2, 1, 1]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
