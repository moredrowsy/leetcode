"""
347. Top K Frequent Elements
Medium
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity
        ---------------
        O(n log n)

        Space Complexity
        ----------------
        O(n)
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ans = [sorted_freq[i][0] for i in range(k)]

        return ans


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    output = Solution().topKFrequent(nums, k)
    expected = [1, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1]
    k = 1
    output = Solution().topKFrequent(nums, k)
    expected = [1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
