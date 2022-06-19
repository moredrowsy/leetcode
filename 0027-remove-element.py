"""
27. Remove Element
Easy
https://leetcode.com/problems/remove-element/

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        if len(nums) == 0:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            while right >= 0 and nums[right] == val:
                right -= 1

            if left <= right and right >= 0 and nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

            left += 1

        return right + 1


if __name__ == "__main__":
    nums, val = [], 1
    output = Solution().removeElement(nums, val)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, val = [1], 1
    output = Solution().removeElement(nums, val)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, val = [3, 2, 2, 3], 3
    output = Solution().removeElement(nums, val)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
    output = Solution().removeElement(nums, val)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, val = [0, 4, 4, 0, 4, 4, 4, 0, 2], 4
    output = Solution().removeElement(nums, val)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, val = [2, 2, 3], 2
    output = Solution().removeElement(nums, val)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
