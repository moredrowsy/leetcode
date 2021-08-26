"""
Sort matrix outside and then inside
"""


class Solution:
    def sort_matrix(self, matrix):
        """
        Sort outside and then sort inside

        Time Complexity
        ---------------
        O(n log n)

        Space Complexity
        ----------------
        O(n log n)
        """
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m-1
        left, right = 0, n-1

        while top <= bottom and left <= right:
            linear = self.spiral_to_linear(matrix, top, bottom, left, right)
            linear.sort()
            self.linear_to_spiral(linear, matrix, top, bottom, left, right)

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return matrix

    def spiral_to_linear(self, matrix, top, bottom, left, right):
        linear = []

        # top
        for i in range(left, right+1):
            linear.append(matrix[top][i])

        # right
        for i in range(top+1, bottom):
            linear.append(matrix[i][right])

        # bottom
        if top != bottom:
            for i in range(right, left-1, -1):
                linear.append(matrix[bottom][i])

        # left
        if left != right:
            for i in range(bottom-1, top, -1):
                linear.append(matrix[i][left])

        return linear

    def linear_to_spiral(self, linear, matrix, top, bottom, left, right):
        n = 0

        # top
        for i in range(left, right+1):
            matrix[top][i] = linear[n]
            n += 1

        # right
        for i in range(top+1, bottom):
            matrix[i][right] = linear[n]
            n += 1

        # bottom
        if top != bottom:
            for i in range(right, left-1, -1):
                matrix[bottom][i] = linear[n]
                n += 1

        # left
        if left != right:
            for i in range(bottom-1, top, -1):
                matrix[i][left] = linear[n]
                n += 1


if __name__ == "__main__":
    t = [2, 100, 6, 4, 5, 6, 5, 9, 10, -1, 3, 5, 7, 3]
    t.sort()
    print(t)
    u = [4, 5, 3, 1]
    u.sort()
    print(u)

    matrix = [
        [2, 4, 5, 6],
        [3, 3, 1, 5],
        [9, 3, 5, 7]
    ]
    output = Solution().sort_matrix(matrix)
    expected = [
        [2, 3, 3, 4],
        [9, 1, 3, 5],
        [7, 6, 5, 5]
    ]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    matrix = [
        [2, 100, 6, 4, 5, 6],
        [3, 4, 5, 3, 1, 5],
        [9, 10, -1, 3, 5, 7]
    ]
    output = Solution().sort_matrix(matrix)
    expected = [
        [-1, 2, 3, 3, 4, 5],
        [100, 1, 3, 4, 5, 5],
        [10, 9, 7, 6, 6, 5]
    ]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
