"""
618. Search Graph Nodes
Medium
https://www.lintcode.com/problem/618/

Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.

There is a mapping store the nodes' values in the given parameters.

NOTE
It's guaranteed there is only one available solution
"""
from graph_node import UndirectedGraphNode
from collections import deque


"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        """
        values is a map of hashable graph node to label value
        """
        if graph:
            if values[node] == target:
                return node

            queue = deque([node])

            while queue:
                node = queue.popleft()

                for neighbor in node.neighbors:
                    if neighbor in values:
                        if values[neighbor] == target:
                            return neighbor

                        del values[neighbor]
                        queue.append(neighbor)

        return None


def get_values_map(graph, values):
    values_map = {}

    for node in graph:
        values_map[node] = values[node.label-1]

    return values_map


def find_node_in_graph(graph, value):
    for node in graph:
        if node.label == value:
            return node
    return None


if __name__ == "__main__":
    nodes = "1,2,3,4#2,1,3#3,1,2#4,1,5#5,4"
    values = [3, 4, 5, 50, 50]
    node = 1
    target = 50
    graph = UndirectedGraphNode.input_to_undirected_graph_nodes(nodes)
    values = get_values_map(graph, values)
    node = find_node_in_graph(graph, node)
    output = Solution().searchNode(graph, values, node, target)
    expected = UndirectedGraphNode(4)
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = "1,2#2,1"
    values = [0, 1]
    node = 1
    target = 1
    graph = UndirectedGraphNode.input_to_undirected_graph_nodes(nodes)
    values = get_values_map(graph, values)
    node = find_node_in_graph(graph, node)
    output = Solution().searchNode(graph, values, node, target)
    expected = UndirectedGraphNode(2)
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
