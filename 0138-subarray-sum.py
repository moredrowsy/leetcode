"""
138. Subarray Sum
Easy
https://www.lintcode.com/problem/138/

Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

NOTE
There is at least one subarray that it's sum equals to zero.
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        """
        The idea is to take advantage of a dip or spike whenever there are
        sequences of numbers that sum to zero.

        For example: [3, 2, -1, 1]
        Consecutive summation yields [3, 5, 4, 5].
        Notice there is a dip at index 2, where it starts from index 1 to 3.
        This is because whenever there is a seq of numbers that sum to zero,
        it will start to either dip/spike and then return back to the value
        before it dip/spike.

        Thus, all we need to find is two points where consecutive summation
        have the same value.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        prefix_hash = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum in prefix_hash:
                return prefix_hash[prefix_sum] + 1, i

            prefix_hash[prefix_sum] = i

        return -1, -1


if __name__ == "__main__":
    nums = [-3, 1, 2, -3, 4]
    output = Solution().subarraySum(nums)
    expected = [(0, 2), (1, 3)]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output in expected)

    nums = [-3, 1, -4, 2, -3, 4]
    output = Solution().subarraySum(nums)
    expected = [(1, 5)]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output in expected)

    nums = [3, 2, -1, 1]
    output = Solution().subarraySum(nums)
    expected = [(2, 3)]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output in expected)
