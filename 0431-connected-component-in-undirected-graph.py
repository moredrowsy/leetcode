"""
431. Connected Component in Undirected Graph
Medium
https://www.lintcode.com/problem/431/

Find connected component in undirected graph.

Each node in the graph contains a label and a list of its neighbors.

(A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

You need return a list of label set.

NOTE
Nodes in a connected component should sort by label in ascending order. Different connected components can be in any order.
"""
from graph_node import UndirectedGraphNode
from collections import deque


"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""


class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """

    def connectedSet(self, nodes):
        if not nodes:
            return []

        paths = []
        visited = set()

        for node in nodes:
            if node.label not in visited:
                self.bfs(node, visited, paths)

        return paths

    def bfs(self, root, visited, paths):
        queue = deque([root])
        visited.add(root.label)
        path = []

        while queue:
            node = queue.popleft()
            path.append(node.label)

            for neighbor in node.neighbors:
                if neighbor.label not in visited:
                    visited.add(neighbor.label)
                    queue.append(neighbor)

        path.sort()
        paths.append(path)


if __name__ == "__main__":
    nodes = "1,2,4#2,1,4#3,5#4,1,2#5,3"
    nodes = UndirectedGraphNode.input_to_undirected_graph_nodes(nodes)
    output = Solution().connectedSet(nodes)
    expected = [[1, 2, 4], [3, 5]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    nodes = "-15,4,-13,0,-8#-14,-3,10#-13,-15#-12,-4,-8#-11,-1#-10,13,6#-9#-8,-6,2,-15,-12#-7,6,-2,14#-6,-8#-5,-4#-4,-12,-5#-3,-14,1#-2,-7,4,9#-1,0,1,-11#0,-1,8,-15,3#1,-1,-3#2,-8,10#3,13,0#4,-15,-2#5,6,10#6,-7,-10,5#7#8,0#9,-2#10,11,5,-14,2#11,10#12#13,-10,3#14,-7,14,14"
    nodes = UndirectedGraphNode.input_to_undirected_graph_nodes(nodes)
    output = Solution().connectedSet(nodes)
    expected = [[-15, -14, -13, -12, -11, -10, -8, -7, -6, -5, -4, -3, -
                 2, -1, 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14], [-9], [7], [12]]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
