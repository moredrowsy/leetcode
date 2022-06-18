"""
217. Contains Duplicate
Easy
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List


class Solution:
    """
    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(n)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set(nums)

        return len(nums) != len(uniques)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    output = Solution().containsDuplicate(nums)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 2, 3, 4]
    output = Solution().containsDuplicate(nums)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    output = Solution().containsDuplicate(nums)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
