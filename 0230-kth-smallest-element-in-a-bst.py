"""
230. Kth Smallest Element in a BST
Medium
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
from tree_node import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []  # A list to keep all the smallest values

        # We only care about the smallest
        # Left side is the smaller than right so stack up the left side only
        while root:
            stack.append(root)
            root = root.left

        for _ in range(k - 1):
            node = stack[-1]  # Peak at the last element

            if not node.right:
                node = stack.pop(-1)
                # Keep popping stack on right branch and old nodes before
                while stack and stack[-1].right and stack[-1].right == node:
                    node = stack.pop(-1)
            else:
                node = node.right
                # Add the right node and it's left branch
                # Because the next left branch are the next smallest values
                while node:
                    stack.append(node)
                    node = node.left

        return stack[-1].val


if __name__ == "__main__":
    k = 1
    nodes = [3, 1, 4, None, 2]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    answer = Solution().kthSmallest(tree, k)
    print(answer)

    k = 3
    nodes = [5, 3, 6, 2, 4, None, None, 1]
    nodes = [TreeNode(node) if node else None for node in nodes]
    tree = TreeNode.get_tree_from_treenode_list(nodes)
    answer = Solution().kthSmallest(tree, k)
    print(answer)
