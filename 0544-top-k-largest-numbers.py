"""
544. Top k Largest Numbers
Medium
https://www.lintcode.com/problem/544/

Given an integer array, find the top k largest numbers in it.
"""


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        return self.pq(nums, k)

    def pq(self, nums, k):
        """
        Time Complexity
        ---------------
        O(n log k)

        Space Complexity
        ----------------
        O(k)
        """
        import heapq
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return list(reversed([heapq.heappop(heap) for _ in range(k)]))


if __name__ == "__main__":
    nums = [3, 10, 1000, -99, 4, 100]
    k = 3
    output = Solution().topk(nums, k)
    expected = [1000, 100, 10]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [8, 7, 6, 5, 4, 3, 2, 1]
    k = 5
    output = Solution().topk(nums, k)
    expected = [8, 7, 6, 5, 4]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
