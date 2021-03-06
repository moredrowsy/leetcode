"""
114. Flatten Binary Tree to Linked List
Medium
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
from tree_node import TreeNode


class Solution:
    def __init__(self) -> None:
        self.last_node = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.

        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        if root:
            if self.last_node:
                self.last_node.left = None
                self.last_node.right = root

            self.last_node = root
            right_node = root.right
            self.flatten(root.left)
            self.flatten(right_node)


if __name__ == "__main__":
    nodes = [1, 2, 5, 3, 4, None, 6]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    Solution().flatten(tree)
    output = tree.get_queue()
    expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None]
    expected = [TreeNode.find_node(tree, i) if i else None for i in expected]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
