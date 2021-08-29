"""
474. Lowest Common Ancestor II
Easy
https://www.lintcode.com/problem/474/

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The nearest common ancestor of two nodes refers to the nearest common node among all the parent nodes of two nodes (including the two nodes).

In addition to the left and right son pointers, each node also contains a father pointer, parent, pointing to its own father.
"""
from typing import List
from tree_node import ParentTreeNode, TreeNode


"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, p, q):
        """
        Get all parents from p to set. Go to q's parents and see if in p set.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        parents = set()

        node = p
        while node:
            parents.add(node)
            node = node.parent

        node = q
        while node:
            if node in parents:
                return node
            node = node.parent

        return None


def get_pq(root: 'ParentTreeNode', p: int, q: int, pq: List['ParentTreeNode']):
    """Parse input to prepare for solution arguments"""
    if root:
        if root.val == p:
            pq[0] = root
        if root.val == q:
            pq[1] = root

        get_pq(root.left, p, q, pq)
        get_pq(root.right, p, q, pq)


if __name__ == "__main__":
    nodes = [4, 3, 7, None, None, 5, 6]
    p = 3
    q = 5
    nodes = [ParentTreeNode(node) if node else None for node in nodes]
    tree = ParentTreeNode.get_parent_tree_from_treenode_list(nodes)
    p = ParentTreeNode.find_node(tree, p)
    q = ParentTreeNode.find_node(tree, q)
    output = Solution().lowestCommonAncestorII(tree, p, q)
    expected = 4
    expected = TreeNode.find_node(tree, expected)

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = 4, 3, 7, None, None, 5, 6
    p = 5
    q = 6
    nodes = [ParentTreeNode(node) if node else None for node in nodes]
    tree = ParentTreeNode.get_parent_tree_from_treenode_list(nodes)
    p = ParentTreeNode.find_node(tree, p)
    q = ParentTreeNode.find_node(tree, q)
    output = Solution().lowestCommonAncestorII(tree, p, q)
    expected = 7
    expected = TreeNode.find_node(tree, expected)

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
