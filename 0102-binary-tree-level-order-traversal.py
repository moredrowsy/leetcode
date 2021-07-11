"""
102. Binary Tree Level Order Traversal
Medium
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from typing import List


def build_tree_node(values):
    from collections import deque
    val_queue = deque(values)
    root_node = TreeNode(val_queue.popleft())
    node_queue = deque([root_node])

    while val_queue:
        node = node_queue.popleft()
        node.left = TreeNode(val_queue.popleft())
        node.right = TreeNode(val_queue.popleft())

        node_queue.append(node.left)
        node_queue.append(node.right)

    return root_node


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []

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

                output.append(level_output)
                level_output = []

        return output


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    root = build_tree_node(root)
    solution = Solution()
    answer = solution.levelOrder(root)
    print(answer)
