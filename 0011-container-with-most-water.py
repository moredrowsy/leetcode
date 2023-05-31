"""
11. Container With Most Water
Medium
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxA = 0

        while left < right:
            area = (right-left) * min(height[left], height[right])
            maxA = max(maxA, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxA


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output = Solution().maxArea(height)
    expected = 49
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    height = [1, 1]
    output = Solution().maxArea(height)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    height = [1, 2, 4, 3]
    output = Solution().maxArea(height)
    expected = 4
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
