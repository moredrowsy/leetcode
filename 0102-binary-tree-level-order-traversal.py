"""
102. Binary Tree Level Order Traversal
Medium
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        tree_output = []

        if root:
            queue = [root]

            while queue:
                level_output = []

                n = len(queue)
                for _ in range(n):
                    node = queue.pop(0)
                    level_output.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                tree_output.append(level_output)

        return tree_output

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        final_output = []
        queue = []

        if root:
            # init
            queue.append(root)
            final_output.append([root.val])
            right_most = root
            level_output = []

            while len(queue) != 0:
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                    level_output.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level_output.append(node.right.val)

                # check if this node is the right most node
                if node == right_most:
                    # add level output to final output if it is not empty
                    if level_output:
                        final_output.append(level_output)
                        level_output = []

                    # find new right most node
                    if node.right:
                        right_most = node.right
                    elif node.left:
                        right_most = node.left
                    elif len(queue):
                        right_most = queue[-1]

        return final_output


if __name__ == "__main__":
    print()
