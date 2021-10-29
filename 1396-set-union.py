"""
1396. Set Union
Medium
https://www.lintcode.com/problem/1396/

There is a list composed by sets. If two sets have the same elements, merge them. Returns the last remaining collection.

Constraints:
The number of sets n <=1000.
The number of elements for each set m <= 100.
The element must be a non negative integer and not greater than 100000.
"""


class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """

    def setUnion(self, sets):
        """
        The 'sets' is m x n matrix

        Time Complexity
        ---------------
        O(m^2 * n)

        Space Complexity
        ----------------
        O(m * n)
        """
        # Build the parents map
        parents = {}
        for s in sets:
            first = s[0]

            for x in s:
                if x not in parents:
                    parents[x] = first
                else:
                    first_parent = self.find(first, parents)
                    x_parent = self.find(x, parents)

                    if x_parent != first_parent:
                        parents[x_parent] = first_parent

        # Combine values to a common root parent
        for s in sets:
            for x in s:
                self.find(x, parents)

        # Get all unique parents
        unique_parents = {p for p in parents.values()}

        return len(unique_parents)  # num of unique parents is the answer

    def find(self, x, parents):
        """Find x's root parent and update it"""
        if x != parents[x]:
            parents[x] = self.find(parents[x], parents)
        return parents[x]


if __name__ == "__main__":
    sets = [[1, 2, 3], [3, 9, 7], [4, 5, 10]]
    output = Solution().setUnion(sets)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    sets = [[1], [1, 2, 3], [4], [8, 7, 4, 5]]
    output = Solution().setUnion(sets)
    expected = 2
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
