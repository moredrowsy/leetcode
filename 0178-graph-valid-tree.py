"""
178. Graph Valid Tree
Medium
https://www.lintcode.com/problem/178/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

NOTE
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        """
        Valid tree conditions
        ---------------------
        1. There is only one tree (no disconnected trees)
        2. Edges = vertices - 1
        3. Acyclic (no cycles)

        NOTE
        No duplicate edges

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        from collections import defaultdict, deque

        # Check condition 2 and 3 (implied by 2)
        if len(edges) != n - 1:
            return False

        neighbors = defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {}
        queue = deque([0])

        while queue:
            cur = queue.popleft()
            visited[cur] = True

            for node in neighbors[cur]:
                if node not in visited:
                    queue.append(node)

        # Check condition 1 and 3 (implied by 1 and 2)
        # Condition 1: One connected tree.
        # If disconnected, we can not visit all nodes
        return len(visited) == n


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    output = Solution().validTree(n, edges)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    output = Solution().validTree(n, edges)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 6
    edges = [[0, 1], [1, 2], [3, 4]]
    output = Solution().validTree(n, edges)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 6
    edges = [[0, 1], [1, 2], [3, 4], [3, 5], [4, 5]]
    output = Solution().validTree(n, edges)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
