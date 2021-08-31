"""
612. K Closest Points
Medium
https://www.lintcode.com/problem/612/

Given some points and an origin in two-dimensional space,Find k points from points which are closest to origin Euclidean.Return to the answer from small to large according to Euclidean distance. If two points have the same Euclidean distance, they are sorted by x values. If the x value is the same, then we sort it by the y value.
"""
from point import Point
import math

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        return self.pq(points, origin, k)

    def pq(self, points, origin, k):
        """
        Time Complexity
        ---------------
        O(k + nlogn)

        Space Complexity
        ----------------
        O(n)
        """
        import heapq
        heap = []

        for p in points:
            dist = self.distance((p.x, p.y), (origin.x, origin.y))
            heapq.heappush(heap, (dist, p.x, p.y))

        kpoints = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            kpoints.append(Point(x, y))

        return kpoints

    def distance(self, point_a, point_b):
        """Find distance between two points where points are n-tuple"""
        return math.sqrt(sum((a - b)**2 for a, b in zip(point_a, point_b)))


if __name__ == "__main__":
    points = [[4, 6], [4, 7], [4, 4], [2, 5], [1, 1]]
    origin = [0, 0]
    k = 3
    points = [Point(x, y) for x, y in points]
    origin = Point(origin[0], origin[1])
    output = Solution().kClosest(points, origin, k)
    expected = [[1, 1], [2, 5], [4, 4]]
    expected = [Point(x, y) for x, y in expected]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    points = [[0, 0], [0, 9]]
    origin = [3, 1]
    k = 1
    points = [Point(x, y) for x, y in points]
    origin = Point(origin[0], origin[1])
    output = Solution().kClosest(points, origin, k)
    expected = [[0, 0]]
    expected = [Point(x, y) for x, y in expected]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
