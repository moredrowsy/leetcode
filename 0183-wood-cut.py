"""
183. Wood Cut
Hard
https://www.lintcode.com/problem/183/

Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

The unit of length is centimeter.The length of the woods are all positive integers,you couldn't cut wood into float length.If you couldn't get >= k pieces, return 0.

Challenge
O(n log Len), where Len is the longest length of the wood.
"""


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        """
        Time Complexity
        ---------------
        O(n log n)

        Space Complexity
        ----------------
        O(1)
        """
        if L is None or not L:
            return 0

        left, right = 1, max(L)

        while left + 1 < right:
            mid = (left + right) // 2
            pieces = self.pieces_of_wood(L, mid)

            if pieces == k:
                left = mid
            elif pieces < k:
                right = mid
            else:
                left = mid

        if self.pieces_of_wood(L, right) >= k:
            return right
        elif self.pieces_of_wood(L, left) >= k:
            return left
        else:
            return 0

    def pieces_of_wood(self, L, length):
        pieces = 0
        for l in L:
            pieces += (l // length)
        return pieces


if __name__ == "__main__":
    L = [232, 124, 456]
    k = 7
    output = Solution().woodCut(L, k)
    expected = 114
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    L = [1, 2, 3]
    k = 0
    output = Solution().woodCut(L, k)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
