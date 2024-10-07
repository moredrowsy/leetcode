"""
1844 · subarray sum equals to k II
Medium
https://www.lintcode.com/problem/1844/

Given an array of integers and an integer k, you need to find the minimum size of continuous no-empty subarrays whose sum equals to k, and return its length.

if there are no such subarray, return -1.
"""
from typing import List

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        sum_to_idx = { 0: 0 }
        prefix_sum = self.get_prefix_sum(nums)
        ans = float('inf')
        n = len(nums)

        for end in range(n):
            # find prefix_sum[end + 1] - prefix_sum[start] = k
            # => prefix_sum[start] = prefix_sum[end + 1] - k
            if prefix_sum[end + 1] - k in sum_to_idx:
                length = end + 1 - sum_to_idx[prefix_sum[end + 1] - k]
                ans = min(ans, length)

            sum_to_idx[prefix_sum[end + 1]] = end + 1

        return -1 if ans == float('inf') else ans

    def get_prefix_sum(self, nums):
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        return prefix_sum

if __name__ == "__main__":
    nums = [1,1,1,2]
    k = 3
    output = Solution().subarray_sum_equals_k_i_i(nums, k)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [2,1,-1,4,2,-3]
    k = 3
    output = Solution().subarray_sum_equals_k_i_i(nums, k)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
