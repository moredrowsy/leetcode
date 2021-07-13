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
    def __init__(self):
        self.last_node = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
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
    nodes = [TreeNode(node) for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    solution = Solution()
    solution.flatten(tree)
    answer = tree.get_queue()
    print(answer)
