"""
238. Product of Array Except Self
Medium
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # setup the prefix array in solution
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        # suffix is going to be multiplied with prefix array to sol
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output

    def productExceptSelf_(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = self.get_prefix_prod(nums)
        suffix_prod = self.get_suffix_prod(nums)

        ans = []
        for i in range(n):
            ans.append(prefix_prod[i] * suffix_prod[i])

        return ans


    def get_prefix_prod(self, nums):
        prefix_prod = [1]

        for num in nums:
            prefix_prod.append(prefix_prod[-1] * num)

        return prefix_prod

    def get_suffix_prod(self, nums):
        n = len(nums)
        suffix_prod = [1] * (n + 1)
        n = len(nums)

        for i in range(n-2, -1, -1):
            suffix_prod[i] = suffix_prod[i + 1] * nums[i + 1]

        return suffix_prod

if __name__ == "__main__":
    nums = [1,2,3,4]
    output = Solution().productExceptSelf(nums)
    expected = [24,12,8,6]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [-1,1,0,-3,3]
    output = Solution().productExceptSelf(nums)
    expected = [0,0,9,0,0]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
