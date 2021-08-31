"""
577. Merge K Sorted Interval Lists
Medium
https://www.lintcode.com/problem/577/

Merge K sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.
"""
from interval import Interval
import heapq


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        """
        Given: Each interval list is sorted

        Two Intervals are merged if Interval_a.end >= Interval_b.start
            - Ex: (1, 2) and (1, 3) are merged b/c 2 is >= 1

        Two Intervals aer not merged if Interval_a.end < Interval_b.start
            - Ex: (4, 8) and (9, 10) are NOT merged b/c 8 < 9

        intervals is a 2d array:
            - x access the array in intervals
            - y access instance of Interval in array of x

        heap will store (start, end, x, y)
            - starting start, end will give us the min at the top of heapq
            - storing x will give us the array in intervals
            - storing y will give us the next instance of Interval in array of x
        """
        merged = []
        heap = []  # Holds the min Interval

        for i, arr in enumerate(intervals):
            if len(arr) > 0:
                heapq.heappush(heap, (arr[0].start, arr[0].end, i, 0))

        while heap:
            start, end, x, y = heapq.heappop(heap)
            self.append_and_merge(Interval(start, end), merged)
            if y + 1 < len(intervals[x]):  # Check if can add next item
                heapq.heappush(
                    heap, (intervals[x][y + 1].start, intervals[x][y + 1].end, x, y + 1))

        return merged

    def append_and_merge(self, interval, intervals):
        if not intervals:
            intervals.append(interval)
            return

        last_interval = intervals[-1]
        if last_interval.end < interval.start:
            intervals.append(interval)
            return

        last_interval.end = max(last_interval.end, interval.end)


if __name__ == "__main__":
    intervals = [
        [(1, 3), (4, 7), (6, 8)],
        [(1, 2), (9, 10)]
    ]
    intervals = [[Interval(s, e) for s, e in interval]
                 for interval in intervals]
    output = Solution().mergeKSortedIntervalLists(intervals)
    expected = [(1, 3), (4, 8), (9, 10)]
    expected = [Interval(s, e) for s, e in expected]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    intervals = [
        [(1, 2), (5, 6)],
        [(3, 4), (7, 8)]
    ]
    intervals = [[Interval(s, e) for s, e in interval]
                 for interval in intervals]
    output = Solution().mergeKSortedIntervalLists(intervals)
    expected = [(1, 2), (3, 4), (5, 6), (7, 8)]
    expected = [Interval(s, e) for s, e in expected]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
