"""
133. Clone Graph
Medium
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            # get all old nodes
            old_nodes = self.get_nodes(node)

            # get new nodes as a map { val: new_node }
            new_nodes = {old_node.val: Node(old_node.val)
                         for old_node in old_nodes}

            for old_node in old_nodes:
                new_node = new_nodes[old_node.val]

                for neighbor in old_node.neighbors:
                    new_node.neighbors.append(new_nodes[neighbor.val])

            return new_nodes[node.val]

    def get_nodes(self, root):
        nodes = set()

        if root:
            nodes.add(root)
            queue = [root]

            while queue:
                node = queue.pop(0)

                for neighbor in node.neighbors:
                    if neighbor not in nodes:
                        nodes.add(neighbor)
                        queue.append(neighbor)

        return nodes
