"""
437. Copy Books
Medium
https://www.lintcode.com/problem/437/

Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.

The sum of book pages is less than or equal to 2147483647
"""


class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        if pages is None or not pages:
            return 0

        left, right = max(pages), sum(pages)

        while left + 1 < right:
            mid = (left + right) // 2

            if self.min_copiers(pages, mid) <= k:
                right = mid
            else:
                left = mid

        if self.min_copiers(pages, left) <= k:
            return left
        else:
            return right

    def min_copiers(self, pages, time_limit):
        copiers = 0
        time_cost = 0
        for page in pages:
            if time_cost + page > time_limit:
                copiers += 1
                time_cost = 0

            time_cost += page

        return copiers + 1


if __name__ == "__main__":
    pages = [3, 2, 4]
    k = 2
    solution = Solution()
    answer = solution.copyBooks(pages, k)
    print(answer)

    pages = [3, 2, 4]
    k = 3
    solution = Solution()
    answer = solution.copyBooks(pages, k)
    print(answer)
