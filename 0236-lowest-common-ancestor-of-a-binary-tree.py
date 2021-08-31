"""
236. Lowest Common Ancestor of a Binary Tree
Medium
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
from tree_node import TreeNode


"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        if not root or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None


if __name__ == "__main__":
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 1
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    p = TreeNode.find_node(tree, p)
    q = TreeNode.find_node(tree, q)
    output = Solution().lowestCommonAncestor(tree, p, q)
    expected = 3
    expected = TreeNode.find_node(tree, expected)

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 4
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    p = TreeNode.find_node(tree, p)
    q = TreeNode.find_node(tree, q)
    output = Solution().lowestCommonAncestor(tree, p, q)
    expected = 5
    expected = TreeNode.find_node(tree, expected)

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nodes = [1, 2]
    p = 1
    q = 2
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    p = TreeNode.find_node(tree, p)
    q = TreeNode.find_node(tree, q)
    output = Solution().lowestCommonAncestor(tree, p, q)
    expected = 1
    expected = TreeNode.find_node(tree, expected)

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
