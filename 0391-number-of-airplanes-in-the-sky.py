"""
391. Number of Airplanes in the Sky
Medium
https://www.lintcode.com/problem/391/
Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?

Contraints:
If landing and taking off of different planes happen at the same time, we consider landing should happen at first.
"""
from interval import Interval

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        """
        Time Complexity
        ---------------
        O(n log n)

        Space Complexity
        ----------------
        O(n)
        """
        from collections import defaultdict

        time_to_airplanes = defaultdict(int)

        for airplane in airplanes:
            time_to_airplanes[airplane.start] += 1
            time_to_airplanes[airplane.end] -= 1

        keys = sorted(time_to_airplanes.keys())

        airplanes_count, max_airplanes = 0, 0
        for k in keys:
            airplanes_count += time_to_airplanes[k]
            max_airplanes = max(airplanes_count, max_airplanes)

        return max_airplanes


if __name__ == "__main__":
    airplanes = [(1, 10), (2, 3), (5, 8), (4, 7)]
    airplanes = [Interval(s, e) for s, e in airplanes]
    output = Solution().countOfAirplanes(airplanes)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    airplanes = [(1, 2), (2, 3), (3, 4)]
    airplanes = [Interval(s, e) for s, e in airplanes]
    output = Solution().countOfAirplanes(airplanes)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
