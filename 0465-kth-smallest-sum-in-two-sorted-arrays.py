"""
465. Kth Smallest Sum In Two Sorted Arrays
Hard
https://www.lintcode.com/problem/465/

Given two integer arrays sorted in ascending order and an integer k. Define sum = a + b, where a is an element from the first array and b is an element from the second one. Find the kth smallest sum out of all possible sums.

Challenge
Do it in either of the following time complexity:

O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
O( (m + n) log maxValue). where maxValue is the max number in A and B.
"""


class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """

    def kthSmallestSum(self, A, B, k):
        import heapq

        if not A or not B:
            return None

        n, m = len(A), len(B)
        minheap = [(A[0] + B[0], 0, 0)]
        visited = set([0])
        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(minheap)
            if x + 1 < n and (x + 1) * m + y not in visited:
                heapq.heappush(minheap, (A[x + 1] + B[y], x + 1, y))
                visited.add((x + 1) * m + y)
            if y + 1 < m and x * m + y + 1 not in visited:
                heapq.heappush(minheap, (A[x] + B[y + 1], x, y + 1))
                visited.add(x * m + y + 1)

        return num


if __name__ == "__main__":
    a = [1, 7, 11]
    b = [2, 4, 6]
    k = 3
    output = Solution().kthSmallestSum(a, b, k)
    expected = 7
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    a = [1, 7, 11]
    b = [2, 4, 6]
    k = 4
    output = Solution().kthSmallestSum(a, b, k)
    expected = 9
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    a = [1, 7, 11]
    b = [2, 4, 6]
    k = 8
    output = Solution().kthSmallestSum(a, b, k)
    expected = 15
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
