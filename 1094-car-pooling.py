"""
1094. Car Pooling
Medium
https://leetcode.com/problems/car-pooling/

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
"""
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_dest = max(trips, key=lambda x: x[2])[2]
        prefix = [0] * (max_dest + 1)

        for cap, start, end in trips:
            prefix[start] += cap
            prefix[end] -= cap

        if prefix[0] > capacity:
            return False

        n = len(prefix)
        for i in range(1, n):
            prefix[i] += prefix[i-1]

            if prefix[i] > capacity:
                return False

        return True


if __name__ == "__main__":
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    output = Solution().carPooling(trips, capacity)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
