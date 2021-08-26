"""
95. Validate Binary Search Tree
Medium
https://www.lintcode.com/problem/95/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
"""
from tree_node import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        """
        1. Max left must be smaller than node
        2. Min right must be greater than node

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        _, __, isValid = self.min_max_bst(root)
        return isValid

    def min_max_bst(self, node):
        """
        Return
        ------
        (min_node, max_node, isValid)
        """
        if not node:
            return None, None, True

        lmin, lmax, lvalid = self.min_max_bst(node.left)

        if not lvalid or (lmax and not lmax.val < node.val):
            return None, None, False

        rmin, rmax, rvalid = self.min_max_bst(node.right)

        if not rvalid or (rmin and not rmin.val > node.val):
            return None, None, False

        min_node = lmin if lmin else node
        max_node = rmax if rmax else node

        return (min_node, max_node, True)


if __name__ == "__main__":
    nodes = [2, 1, 4,  None, None, 3, 5]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().isValidBST(tree)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [-1]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().isValidBST(tree)
    expected = True
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [1, None, 2, 3]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    output = Solution().isValidBST(tree)
    expected = False
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
