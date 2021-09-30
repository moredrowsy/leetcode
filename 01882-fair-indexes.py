"""
1882. Fair Indexes
Medium
https://www.lintcode.com/problem/1882/

You are given two arrays A and B consisting of N integers each.

Index K is named fair if the four sums(A[0]+...A[K-1]),(A[K]+...+A[N-1]),(B[0]+...+B[K-1]) and (B[K]+...+B[N-1]) are all equal, In other words, K is the index where the two arrays, A and B, can be split (into two non-empty arrays each) in such a way that the sums of the resulting arrays’ elements are equal.

For example, given arrays A = [4,-1, 0, 3] and B = [-2, 5, 0, 3], index K = 2 is fair. The sums of the subarrays are all equal: 4+(-1) = 3; 0+3 = 3; -2 + 5 = 3 and 0 + 3 = 3.

Now you have to figure out the number of fair indexes.

Contraints:
2<=N<=100000
-1000000000<=a[i],b[i]<=1000000000 (0<=i<N)
"""


class Solution:
    """
    @param A: an array of integers
    @param B: an array of integers
    @return: return a integer indicating the number of fair indexes.
    """

    def CountIndexes(self, A, B):
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        n = len(A)

        sumA = sum(A)
        sumB = sum(B)
        if sumA != sumB:
            return 0

        preA, preB = 0, 0
        index = 0

        for i in range(n):
            preA += A[i]
            preB += B[i]

            if preA == preB and sumA - preA == preA:
                index += 1

        return index


if __name__ == "__main__":
    A = [4, -1, 0, 3]
    B = [-2, 5, 0, 3]
    output = Solution().CountIndexes(A, B)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    A = [2, -2, -3, 3]
    B = [0, 0, 4, -4]
    output = Solution().CountIndexes(A, B)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
