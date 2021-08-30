"""
264. Ugly Number II
Medium
https://leetcode.com/problems/ugly-number-ii/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Note that 1 is typically treated as an ugly number.

Constraints:
1 <= n <= 1690
"""
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Ugly number starts at 1.
        Next ugly number is ugly * one of [2,3,5] factors.

        For example,
        ugly = 1, next uglies = [1*2, 1*3, 1*5] = [2, 3, 5]
        ugly = 2, next uglies = [2*2, 2*3, 2*5] = [4, 6, 10]
        ugly = 3, next uglies = [3*2, 3*3, 3*5] = [6, 9, 15]
        ugly = 4, next uglies = [4*2, 4*3, 4*5] = [8, 12, 20]
        ugly = 5, next uglies = [5*2, 5*3, 5*5] = [10, 15, 20]

        After adding only unique:
        uglies = [1, 2, 3, 4, 5, 6, 8, 9, 10]

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        ugly = 1

        heap = [ugly]
        heapq.heapify(heap)
        visited = set(heap)
        factors = [2, 3, 5]

        for _ in range(n):
            ugly = heapq.heappop(heap)

            for f in factors:
                new_ugly = ugly*f

                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return ugly


if __name__ == "__main__":
    n = 1
    output = Solution().nthUglyNumber(n)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 9
    output = Solution().nthUglyNumber(n)
    expected = 10
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 10
    output = Solution().nthUglyNumber(n)
    expected = 12
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
