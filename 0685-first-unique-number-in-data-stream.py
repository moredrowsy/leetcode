"""
685. First Unique Number in Data Stream
Medium
https://www.lintcode.com/problem/685/

Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the terminating number is not found, return -1.
"""
from collections import defaultdict


class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

            if num == number:
                break
        else:
            return -1

        for num in nums:
            if counts[num] == 1:
                return num
            if num == number:
                break

        return -1


if __name__ == "__main__":
    nums = [1, 2, 2, 1, 3, 4, 4, 5, 6]
    number = 5
    output = Solution().firstUniqueNumber(nums, number)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 2, 2, 1, 3, 4, 4, 5, 6]
    number = 7
    output = Solution().firstUniqueNumber(nums, number)
    expected = -1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 2, 2, 1, 3, 4]
    number = 3
    output = Solution().firstUniqueNumber(nums, number)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
